# Teacher Explanation & Viva Guide
## PS No. 36: Personal Expense & Budget Manager

**Student Name:** [Your Name]  
**Roll No. / Enrollment:** [Your Roll No.]  
**Course:** Bachelor of Technology – Computer Science & Engineering (1st Year)  
**Institution:** Rungta International Skills University (School of CSE)  
**File Name:** `expense_manager.py`  
**Core Technologies:** Python 3, Pandas, CSV File Handling, Dictionaries, Functions  

---

## Table of Contents
1. [30-Second Elevator Pitch (Opening Statement)](#1-30-second-elevator-pitch)
2. [Project Architecture & Execution Flow](#2-project-architecture--execution-flow)
3. [Core Syllabus Concepts Demonstrated (High-Scoring Section)](#3-core-syllabus-concepts-demonstrated)
4. [Function-by-Function Code Breakdown](#4-function-by-function-code-breakdown)
5. [Live Demonstration Script for the Teacher](#5-live-demonstration-script-for-the-teacher)
6. [Top 15 Viva & Teacher Questions (With Answers)](#6-top-15-viva--teacher-questions-with-answers)
7. [5-Minute Quick Revision Cheat Sheet](#7-5-minute-quick-revision-cheat-sheet)

---

## 1. 30-Second Elevator Pitch

> *"Good morning / Good afternoon, Sir/Ma'am.*  
> *My project is **Personal Expense & Budget Manager** (PS No. 36).  
> It is a console application designed to help users control their monthly finances.  
> It allows users to set a spending limit, add daily expenses with strict date and amount validations, store records permanently in a CSV file, and analyze spending patterns category-wise using **Pandas `groupby()`**.  
> The system also includes an intelligent budget monitor that triggers proactive alerts at **80% budget utilization**, **100% full usage**, and **over-budget exceeding**."*

---

## 2. Project Architecture & Execution Flow

```text
       +---------------------------------------------+
       |             CLI User Interface              |
       |  (1. Set Budget | 2. Add | 3. Summary | 4. Report)
       +----------------------+----------------------+
                              |
                     Input Validation
          +-------------------+-------------------+
          |                                       |
    Date Check                              Amount Check
  (YYYY-MM-DD)                            (Positive Float)
          |                                       |
          +-------------------+-------------------+
                              |
                    Data Storage Layer
          +-------------------+-------------------+
          |                                       |
     budget.txt                              expenses.csv
  (Monthly Limit)                         (DictWriter: Date,
                                           Category, Amount)
                              |
                    Data Analysis Layer
                              |
                    Pandas DataFrame
         df.groupby("Category")["Amount"].sum()
                              |
                    Alert & Warning Engine
          +-------------------+-------------------+
          |                   |                   |
      < 80% Spent        >= 80% Spent          > 100% Spent
     (Normal State)    (Budget Warning)     (Budget Exceeded!)
```

### Key Workflow Steps:
1. **Input Phase:** User enters commands and values via an interactive menu loop.
2. **Validation Phase:** Strict regex/datetime parsing ensures data integrity before writing to disk.
3. **Storage Phase:** Data is written to `expenses.csv` (using Python's `csv.DictWriter`) and `budget.txt`.
4. **Analysis Phase:** Pandas reads the CSV into a DataFrame, groups data by Category, and computes aggregate sums.
5. **Monitoring Phase:** Percentage utilized = $(Total\ Spent / Budget) \times 100$. Appropriate warnings are displayed.

---

## 3. Core Syllabus Concepts Demonstrated

When the teacher asks: *"What programming concepts have you implemented in this project?"*, highlight these 5 points:

### 1. Functions & Modularity
- Instead of writing monolithic code, the project is divided into **10 modular functions** with single responsibilities:
  - Validation: `validate_date()`, `validate_amount()`
  - Persistence: `save_budget_to_file()`, `load_budget()`, `save_expense_to_csv()`
  - Analytics & Reporting: `get_spending_data()`, `print_budget_status()`, `show_category_summary()`, `show_report()`
  - Controller: `main()`, `set_budget()`, `add_expense()`

### 2. Dictionaries
- **Writing to CSV:** Expense records are modeled as key-value dictionaries:
  ```python
  expense_record = {"Date": date_str, "Category": category, "Amount": amount}
  ```
- **Aggregation Mapping:** Pandas series aggregated from `.groupby()` is transformed into a dictionary (`category_dict = grouped.to_dict()`) for fast lookups and clean printing.

### 3. File Handling & CSV Persistence
- Uses Python's native `csv` module with `csv.DictWriter`.
- Uses `mode="a"` (append mode) to add records without overwriting existing data.
- Handles headers dynamically: `writer.writeheader()` is called **only if the file is newly created or empty**.
- Persistent budget stored in `budget.txt` ensures state is remembered between runs.

### 4. Pandas Data Analysis
- Loads tabular data with `pd.read_csv("expenses.csv")`.
- Demonstrates advanced vectorized aggregation:
  ```python
  grouped = df.groupby("Category", sort=False)["Amount"].sum()
  ```
- Fast summation of the total amount spent: `float(df["Amount"].sum())`.

### 5. Exception Handling & Input Validation
- Prevents runtime crashes using `try-except` blocks (`ValueError`, `IOError`).
- Ensures year is 4 digits, month is 2 digits (01-12), and day is 2 digits (01-31).
- Prevents negative expenses and non-numeric characters.

---

## 4. Function-by-Function Code Breakdown

| Function Name | Lines in Code | Purpose | Explanation for Teacher |
|---|---|---|---|
| `load_budget()` | 24 - 34 | Reads saved budget | Checks if `budget.txt` exists. Reads and converts content to `float`. If missing or corrupt, returns `None`. |
| `save_budget_to_file(budget)` | 37 - 43 | Saves budget to disk | Opens `budget.txt` in `"w"` mode and saves the numeric budget so the user doesn't lose it upon exit. |
| `format_amount(value)` | 46 - 50 | Output formatting | If number is an integer (e.g. `1000.0`), it prints cleanly as `1000`; if it has decimal cents (e.g. `10.50`), it prints as `10.50`. |
| `validate_date(date_str)` | 53 - 66 | Validates date format | Splits by `-` to enforce exactly 4-digit year, 2-digit month, 2-digit day, and uses `datetime.strptime(date_str, "%Y-%m-%d")` to reject invalid calendar dates like `2026-02-30`. |
| `validate_amount(amount_str)` | 68 - 76 | Validates numeric value | Converts input to `float(amount_str)`. Checks if `val > 0`. Returns `(True, val)` or `(False, None)`. Rejects negatives and non-numbers. |
| `set_budget()` | 79 - 92 | Menu Option 1 | Prompts user for budget, validates it, updates global `monthly_budget`, and saves to `budget.txt`. |
| `save_expense_to_csv(...)` | 94 - 111 | Appends expense | Creates dictionary `{"Date": ..., "Category": ..., "Amount": ...}` and writes via `csv.DictWriter`. Automatically writes header on first record. |
| `get_spending_data()` | 113 - 129 | Core Pandas analytics | Reads `expenses.csv` into a DataFrame. Runs `.groupby("Category", sort=False)["Amount"].sum()` and returns `(df, total_spent, category_dict)`. |
| `print_budget_status(...)` | 131 - 148 | Threshold & warning checks | Calculates remaining budget and percentage. Triggers warnings at **>= 80%**, **100% full**, and **> 100% exceeded**. |
| `add_expense()` | 150 - 199 | Menu Option 2 | Supports both comma-separated input (`2026-10-05, Food, 500`) and step-by-step input. Validates both date and amount before saving. |
| `show_category_summary()` | 201 - 210 | Menu Option 3 | Calls `get_spending_data()` and formats category totals cleanly separated by `\|` (e.g., `Food: 3200 \| Travel: 1000`). |
| `show_report()` | 212 - 227 | Menu Option 4 | Displays complete financial summary: category breakdown, total spent, remaining balance, and warning status. |
| `main()` | 229 - 261 | Program controller | Infinite `while True` menu loop. Routes choices 1 to 5 with case-insensitive and numbered matching. |

---

## 5. Live Demonstration Script for the Teacher

1. **Set Budget (Option 1):** Enter `5000` $\to$ `Monthly budget set: 5000`.
2. **Input Validation (Option 2):**
   - Negative amount: `2026-10-05, Food, -200` $\to$ Rejects with `Invalid amount. Amount must be a positive number.`
   - Invalid date: `05-10-2026, Food, 200` $\to$ Rejects with `Invalid date. Use YYYY-MM-DD.`
3. **Add Multiple Expenses (Option 2):**
   - `2026-10-01, Food, 1500`
   - `2026-10-02, Travel, 1000`
   - `2026-10-03, Food, 1700`
   - Notice: Total is 4200 (84% of 5000) $\to$ Triggers `Warning: 84.00% of the budget used.`
4. **Category Summary (Option 3):** Displays `Food: 3200 | Travel: 1000` computed automatically by Pandas `.groupby()`.
5. **Full Report (Option 4):** Displays category breakdown, total spent, remaining balance, and warning status.

---

## 6. Top 15 Viva & Teacher Questions (With Answers)

### Q1: Why did you use Pandas instead of writing standard Python `for` loops?
**Answer:** *"Pandas is built in C and highly optimized for tabular data analysis. Using `df.groupby('Category')['Amount'].sum()` performs the split-apply-combine operation vectorially in a single line. It is faster, more concise, and handles large datasets much better than manual dictionary iteration."*

### Q2: How does `groupby()` work internally?
**Answer:** *"It follows the Split-Apply-Combine pattern: Split divides the rows into groups by 'Category', Apply computes `.sum()` on 'Amount', and Combine merges the totals into a unified Series."*

### Q3: Why did you use `csv.DictWriter` instead of standard `csv.writer`?
**Answer:** *"Standard `csv.writer` writes rows as indexed tuples, which can cause column-order mixups. `csv.DictWriter` maps dictionary keys directly to CSV headers (`Date`, `Category`, `Amount`), making the code clean, robust, and demonstrating dictionary concepts."*

### Q4: How is data persisted across multiple application runs?
**Answer:** *"`expenses.csv` stores transactional records in append mode (`'a'`). `budget.txt` stores the monthly budget limit so the user doesn't lose it when closing the app."*

### Q5: How do you prevent duplicate headers in the CSV file?
**Answer:** *"We check if the file exists and has size > 0 before calling `writer.writeheader()`. It only writes headers if the file is brand new or empty."*

### Q6: How is strict date validation implemented?
**Answer:** *"We verify 4-digit year and 2-digit month/day, followed by `datetime.strptime(date_str, '%Y-%m-%d')` to catch invalid calendar days like Feb 30."*

### Q7: What are your warning thresholds?
**Answer:** *"$\ge 80\%$ triggers an early warning, $100\%$ alerts budget fully used, and $> 100\%$ alerts budget exceeded."*

### Q8: What happens if `expenses.csv` does not exist yet?
**Answer:** *"`get_spending_data()` checks if the file exists; if not, it returns `(None, 0.0, {})` cleanly without crashing."*

### Q9: Why did you use `global monthly_budget`?
**Answer:** *"In a procedural script, it shares session state across menu functions. In an advanced version, this could be encapsulated inside a class."*

### Q10: How do you handle non-numeric inputs?
**Answer:** *"`validate_amount()` uses a `try-except ValueError` block when converting to `float`."*

### Q11: What is the purpose of `sort=False` in `groupby()`?
**Answer:** *"It preserves the order categories were added and avoids unnecessary sorting overhead."*

### Q12: Why create `format_amount()`?
**Answer:** *"To display clean whole numbers like `1000` instead of `1000.0`, while keeping decimals when cents exist."*

### Q13: What does `if __name__ == '__main__':` do?
**Answer:** *"It ensures `main()` executes only when run directly, not when imported by test scripts."*

### Q14: Can users enter expenses with or without commas?
**Answer:** *"Yes, `add_expense()` checks for commas. If present, it parses comma-separated inputs; otherwise, it asks step-by-step."*

### Q15: Future improvements?
**Answer:** *"Visual charts using Matplotlib, a Tkinter/Streamlit GUI, and SQLite database storage."*

---

## 7. 5-Minute Quick Revision Cheat Sheet
- **Course:** B.Tech CSE (1st Year)
- **Problem Statement:** PS No. 36 – Personal Expense & Budget Manager
- **Core Files:** `expense_manager.py`, `expenses.csv`, `budget.txt`, `README.md`
- **Key Formula:** $\text{percentage} = (\text{total\_spent} / \text{budget}) \times 100$
- **Pandas Grouping:** `df.groupby("Category", sort=False)["Amount"].sum().to_dict()`

