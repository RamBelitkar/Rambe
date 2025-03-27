# 🕒 Intelligent Timetable Scheduler 📅

## 🌟 Project Overview

An intelligent course scheduling system powered by Genetic Algorithms, designed to create optimal timetables with minimal conflicts and maximum efficiency.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![Genetic Algorithm](https://img.shields.io/badge/Algorithm-Genetic-green?style=for-the-badge)

## ✨ Key Features

- 🤖 **Intelligent Scheduling**: Uses advanced Genetic Algorithm
- 🗓️ **Flexible Timetabling**: Supports multiple departments, courses, and constraints
- 💡 **Smart Conflict Resolution**: Minimizes scheduling conflicts
- 📊 **Database-Driven**: Seamless MySQL integration

## 🚀 How It Works

The scheduler uses a sophisticated Genetic Algorithm to:
- 🔍 Evaluate scheduling possibilities
- 🧬 Evolve optimal solutions
- 🏆 Minimize scheduling conflicts

### Optimization Criteria
- Room capacity matching
- Instructor availability
- Time slot distribution
- Course requirements

## 🛠️ Technical Stack

- **Language**: Python 3.8+
- **Database**: MySQL
- **Key Libraries**:
  - `pymysql`
  - `prettytable`
  - `random`

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/timetable-scheduler.git

# Install dependencies
pip install pymysql prettytable

# Setup MySQL Database
# Import the required schema and data
```

## 🔧 Configuration

1. Update database connection parameters in `main()`:
   ```python
   connection = pymysql.connect(
       host='localhost',
       user='your_username',
       password='your_password',
       db='your_database'
   )
   ```

2. Adjust Genetic Algorithm parameters:
   ```python
   POPULATION_SIZE = 15
   MUTATION_RATE = 0.3
   TOURNAMENT_SELECTION_SIZE = 6
   ```

## 🎯 Usage

```python
# Run the scheduler
python timetable_scheduler.py
```

## 📈 Performance Metrics

- **Initial Solution Quality**: Randomly generated
- **Optimization Goal**: Fitness Score of 1.0
- **Conflict Resolution**: Minimized through evolutionary process



⭐ Don't forget to star the repository if you find it helpful! 🌟
