# Claims Triangle Technical Test Submission

**Author:** Destiny Onyemerekwe

## Overview

This program reads incremental insurance claim data from a CSV file and produces a cumulative claims triangle as output.  
It sitmulates part of a reserving process used in insurance, estimating how much has been paid (and will be paid) for claims across multiple years and products.

### The program:
This program implements a structed approach to building cumulative claims triangles by:
- Reading and organising the incremental claim data by product and origin year using nested dictionaries
- Filling missing development years with zeros to complete each triangle
- Converting incremental values into cumulative totals using loops and running sums
- Writing the final cumulative triangles to an output CSV file for each review and analysis

It demonstrates practical use of Python's file handling, lists, and dictionaries to process structed data efficiently

---

## How to Run

### 1. Requirements
- Python 3.x installed

---

### 2. Files

Ensure the following files are in the same folder:
- `main.py`
- `input.csv`

---

### 3. Running the Program

Open a terminal in the project folder and run:

```bash
python main.py
```

The program will generate a new file:
`output.csv`

This file contains:
- The earliest origin year and total number of development years in the first line
- Cumulative claims data for each product in subsequent lines

Example:
Input (`input.csv`):
```
Product, Origin Year, Development Year, Incremental Value
Comp, 1992, 1992, 110.0
Comp, 1992, 1993, 170.0
Comp, 1993, 1993, 200.0
Non-Comp, 1990, 1990, 45.2
Non-Comp, 1990, 1991, 64.8
Non-Comp, 1990, 1993, 37.0
Non-Comp, 1991, 1991, 50.0
Non-Comp, 1991, 1992, 75.0
Non-Comp, 1991, 1993, 25.0
Non-Comp, 1992, 1992, 55.0
Non-Comp, 1992, 1993, 85.0
Non-Comp, 1993, 1993, 100.0
```

Output (`output.csv`):
```
1990, 4
Comp, 0, 0, 0, 0, 0, 0, 0, 110.0, 280.0, 200.0
Non-Comp, 45.2, 110.0, 110.0, 147.0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0
```
--- 

### Notes
- Missing incremental values are assumed to be 0
- The program supports multiple products (e.g. “Comp” and “Non-Comp”)
- Input data must contain headers in the following order:

Product, Origin Year, Development Year, Incremental Value
- Origin years and development years are expected to be integers
- Output is written as a plain CSV file, viewable in Excel or any text editor
