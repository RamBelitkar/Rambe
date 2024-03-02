import random as rnd 
import pymysql.cursors
import prettytable as prettytable

# Constants
POPULATION_SIZE = 15
NUMB_OF_ELITE_SCHEDULE = 5
TOURNAMENT_SELECTION_SIZE = 6
MUTATION_RATE = 0.3
global thisdata

class Data:
    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        self._courses = []
        self._depts = []

    def fetch_data_from_database(self, connection):
        self._rooms = self.fetch_rooms(connection)
        self._meetingTimes = self.fetch_meeting_times(connection)
        self._instructors = self.fetch_instructors(connection)
        self._courses = self.fetch_courses(connection)
        self._depts = [Department("IT", self._courses)]

    def fetch_rooms(self, connection):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM rooms"
                cursor.execute(sql)
                rooms_data = cursor.fetchall()
                rooms = []
                for item in rooms_data:
                    seating_capacity = int(item["seatingCapacity"])
                    room = Room(item["number"], seating_capacity, item["lab"])
                    rooms.append(room)
                return rooms
        except Exception as e:
            print(f"Error fetching rooms: {e}")
            return []


    def fetch_instructors(self, connection):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM instructors"
                cursor.execute(sql)
                instructors_data = cursor.fetchall()
                instructors = [Instructor(item["id"], item["name"]) for item in instructors_data]
                return instructors
        except Exception as e:
            print(f"Error fetching instructors: {e}")
            return []

    def fetch_courses(self, connection):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM courses"
                cursor.execute(sql)
                courses_data = cursor.fetchall()
                courses = []
                for item in courses_data:
                    instructor_names = item["instructor"].split(',')
                    instructors = [Instructor(id, name) for id, name in enumerate(instructor_names, 1)]
                    # Convert capacity to an integer
                    capacity = int(item["capacity"])
                    course = Course(item["course_code"], item["course_name"], instructors, capacity)
                    courses.append(course)
                return courses
        except Exception as e:
            print(f"Error fetching courses: {e}")
            return []

    def fetch_meeting_times(self, connection):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM meeting_times"
                cursor.execute(sql)
                meeting_times_data = cursor.fetchall()
                meeting_times = [MeetingTime(item["id"], item["time"]) for item in meeting_times_data]
                return meeting_times
        except Exception as e:
            print(f"Error fetching meeting times: {e}")
            return []

    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors
    
    def get_depts(self):
        return self._depts
    
    def get_courses(self):
        return self._courses
    
    def get_meetingTimes(self):
        return self._meetingTimes
    
    def get_maxNumberOfClasses(self):
        return sum(len(dept.get_courses()) for dept in self._depts)

class DisplayMgr():
    def print_available_data(self, data):
        print("> All Available Data")
        self.print_dept(data)
        self.print_course(data)
        self.print_room(data)
        self.print_instructor(data)
        self.print_meeting_times(data)
    
    def print_dept(self, data):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            tempStr = "]"
            for j in range(0, len(courses) - 1):
                tempStr += str(courses[j]) + ","
            tempStr += str(courses[len(courses) - 1]) + "]"
            availableDeptsTable.add_row([depts[i].get_name(), tempStr])
        print(availableDeptsTable)

    
    def print_course(self, data):
        availableCoursesTable = prettytable.PrettyTable(['course-code', 'course-name', 'max # of students', 'instructors'])
        courses = data.get_courses()
        for course in courses:
            instructors = ", ".join([instructor.get_name() for instructor in course.get_instructors()])
            availableCoursesTable.add_row([course.get_course_code(), course.get_course_name(), str(course.get_capacity()), instructors])
        print(availableCoursesTable)


    def print_instructor(self, data):
        availabelInstructorTable = prettytable.PrettyTable(['ID', 'Name'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)): 
            availabelInstructorTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availabelInstructorTable)

    def print_room(self, data):
        availabelRoomsTable = prettytable.PrettyTable(['Room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availabelRoomsTable.add_row([rooms[i].get_number(), rooms[i].get_seatingCapacity()])
        print(availabelRoomsTable)

    def print_meeting_times(self, data):
        availabelmeetingTimeTable = prettytable.PrettyTable(['id', 'Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availabelmeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
        print(availabelmeetingTimeTable)
    
    def print_generation(self, population):
        table = prettytable.PrettyTable(['Schedule #', 'fitness', '# of conflicts', 'classes [dept,class,room,intructor,meetingtime]'])
        Schedule = population.get_Schedule()
        for i in range(0, len(Schedule)):
            table.add_row([str(i), round(Schedule[i].get_fitness(), 3), Schedule[i].get_numbOfConflicts(), Schedule[i]])
        print(table)

    def print_schedule_as_table(self, schedule, data):  
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(['Class #', 'Dept', 'Course (number , max # of students)', 'Room(Capacity)', 'Instructor', 'Meeting Time', 'Day'])

        for i in range(0, len(classes)):
            table.add_row([str(i), 
                        classes[i].get_dept().get_name(), 
                        classes[i].get_course().get_course_name() + "(" + str(classes[i].get_course().get_course_code()) + "," + str(classes[i].get_course().get_capacity()) + ")", 
                        classes[i].get_course().get_course_name() + "(" + str(classes[i].get_course().get_course_code()) + "," + str(classes[i].get_course().get_capacity()) + ")"
, 
                        classes[i].get_instructor().get_name() + "(" + str(classes[i].get_instructor().get_id()) + ")", 
                        classes[i].get_meetingTime().get_time() + "(" + str(classes[i].get_meetingTime().get_id())+ ")",
                        classes[i].get_day()])  # Add day here

        print(table)
    def print_timetable(self, schedule):
        timetable_headers = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        timetable_table = prettytable.PrettyTable(timetable_headers)

        time_slots = schedule.get_classes()

        for time_slot in time_slots:
            row = [time_slot.get_meetingTime().get_time()]
            for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
                matching_classes = [cls for cls in time_slots if cls.get_day() == day and cls.get_meetingTime().get_time() == time_slot.get_meetingTime().get_time()]
                if matching_classes:
                    class_info = f"{matching_classes[0].get_course().get_course_name()}({matching_classes[0].get_course().get_course_code()},{matching_classes[0].get_course().get_capacity()})"
                    row.append(class_info + " " + str(matching_classes[0].get_room().get_number()) + " " + matching_classes[0].get_instructor().get_name())
                else:
                    row.append('')
            timetable_table.add_row(row)

        return str(timetable_table)



class Population:
    def __init__(self, size, data):
        self._size = size
        self._data = data
        self._Schedule = []

        for i in range(0, size):
            self._Schedule.append(Schedule(self._data).initialize())

    def get_Schedule(self):
        return self._Schedule

class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))
    
    def _crossover_population(self, pop):
        crossover_pop = Population(0, pop._data)

        for i in range(NUMB_OF_ELITE_SCHEDULE):
            crossover_pop.get_Schedule().append(pop.get_Schedule()[i])

        i = NUMB_OF_ELITE_SCHEDULE

        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_Schedule()[0]
            schedule2 = self._select_tournament_population(pop).get_Schedule()[0]
            crossover_pop.get_Schedule().append(self._crossover_schedule(schedule1, schedule2))
            i += 1

        return crossover_pop
    
    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULE, POPULATION_SIZE):
            self._mutate_schedule(population.get_Schedule()[i])

        return population
    
    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule(schedule1._data).initialize()

        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.3:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]

        return crossoverSchedule
    
    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule(mutateSchedule._data).initialize()

        for i in range(0, len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]

        return mutateSchedule
    
    def _select_tournament_population(self, pop):
        tournament_pop = Population(0, pop._data)
        i = 0

        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_schedule = rnd.choice(pop.get_Schedule())
            tournament_pop.get_Schedule().append(tournament_schedule)
            i += 1

        tournament_pop.get_Schedule().sort(key=lambda x: x.get_fitness(), reverse=True)

        return tournament_pop


class Schedule:
    def __init__(self, data):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
    
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    
    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(self._data.get_meetingTimes()[rnd.randrange(0, len(self._data.get_meetingTimes()))])
                newClass.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))])
                newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])
                newClass.set_day(rnd.choice(days))  # Assign a random day
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            room_capacity = classes[i].get_room().get_seatingCapacity()
            course_capacity = classes[i].get_course().get_capacity()
            if room_capacity < course_capacity:
                self._numbOfConflicts += 1
            for j in range(0, len(classes)):
                if j >= i:
                    if (
                        classes[i].get_meetingTime() == classes[j].get_meetingTime()
                        and classes[i].get_day() == classes[j].get_day()  # Add day check
                        and classes[i].get_id() != classes[j].get_id()
                    ):
                        if classes[i].get_room() == classes[j].get_room():
                            self._numbOfConflicts += 1
                        if classes[i].get_instructor() == classes[j].get_instructor():
                            self._numbOfConflicts += 1
        return 1 / (1.0 * (self._numbOfConflicts + 1))


    def __str__(self):
        returnValue = ""

        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ","

        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue

class Course:
    def __init__(self, course_code, course_name, instructors, capacity):
        self._course_code = course_code    
        self._course_name = course_name  
        self._capacity = capacity
        self._instructors = instructors
    
    def get_course_code(self):
        return self._course_code      

    def get_course_name(self):
        return self._course_name 

    def get_instructors(self):
        return self._instructors   

    def get_capacity(self):
        return self._capacity

    def __str__(self):
        return self._course_name

class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name

class Room:
    def __init__(self, number, seatingCapacity, lab):
        self._number = number
        self._seatingCapacity = seatingCapacity
        self._lab = lab  # Assign lab parameter to self._lab

    def get_number(self):
        return self._number

    def get_seatingCapacity(self):
        return self._seatingCapacity
    
    def get_lab(self):
        return self._lab


class MeetingTime:
    def __init__(self, id, time): 
        self._id = id
        self._time = time

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time

class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_courses(self):
        return self._courses
    
    def get_name(self):
        return self._name

class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
        self._day = None

    def get_id(self):
        return self._id

    def get_dept(self):
        return self._dept

    def get_course(self):
        return self._course

    def get_instructor(self):
        return self._instructor

    def get_meetingTime(self):
        return self._meetingTime

    def get_room(self):
        return self._room

    def set_instructor(self, instructor):
        self._instructor = instructor

    def set_meetingTime(self, meetingTime):
        self._meetingTime = meetingTime

    def set_room(self, room):
        self._room = room
    
    def get_day(self):
        return self._day

    def set_day(self, day):
        self._day = day

    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_course_name()) + "," + str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(self._meetingTime.get_id())


def main():
    try:
        # Establish connection to the database
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='mysql',
                                    
                                    cursorclass=pymysql.cursors.DictCursor)

        # Create data object and fetch data from the database
        data = Data()
        data.fetch_data_from_database(connection)

    except Exception as e:
        print(f"Error: {e}")
    connection.close()

    displayMgr = DisplayMgr()
    displayMgr.print_available_data(data)
    
        # Create population
    population = Population(POPULATION_SIZE, data)
    population.get_Schedule().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_timetable(population.get_Schedule()[0])
    geneticAlgorithm = GeneticAlgorithm()
    generationNumber = 0

    while population.get_Schedule()[0].get_fitness() != 1.0:
        generationNumber += 1
        print("\n > Generation #", generationNumber)
        population = geneticAlgorithm.evolve(population)
        population.get_Schedule().sort(key=lambda x: x.get_fitness(), reverse=True)
        displayMgr.print_generation(population)
        print("\n\n")
        displayMgr.print_schedule_as_table(population.get_Schedule()[0], data)
        displayMgr.print_timetable(population.get_Schedule()[0])
        tdata= str(displayMgr.print_timetable(population.get_Schedule()[0]))
        print (tdata)
    return tdata 

if __name__ == '__main__':
    thisdata=main()
    
