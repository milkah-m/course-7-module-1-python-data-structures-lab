# Student Data Management System

A Python-based system for storing, filtering, and processing student records efficiently using core Python data structures.

## Setup

1. Clone the repository and navigate to the project folder
2. Install dependencies:
```bash
pipenv install
```
3. Activate the virtual environment:
```bash
pipenv shell
```

## Usage

Run each module individually to see its output:

```bash
python student_data.py       # View raw student records
python filter.py             # Filter students by major
python data_processing.py    # Display formatted student data
python set_operations.py     # View unique majors
python data_generator.py     # Generate students by major lazily
```

## Features

| Module | Description |
|---|---|
| `student_data.py` | Defines student records as a list of tuples |
| `filter.py` | Filters students by major using list and dictionary comprehensions |
| `data_processing.py` | Formats and displays student data using a dictionary structure |
| `set_operations.py` | Extracts unique majors using set comprehension |
| `data_generator.py` | Generates students by major lazily using a generator expression |

## Data Structure Decisions

- **Tuples** — used for individual student records since student data should not change
- **Lists** — used to hold the full collection of students since the collection may grow
- **Sets** — used to track unique majors, automatically handling duplicates
- **Dictionary** — used inside formatting to make student fields explicitly named and readable
- **Generator** — used for filtering by major to avoid loading all records into memory at once