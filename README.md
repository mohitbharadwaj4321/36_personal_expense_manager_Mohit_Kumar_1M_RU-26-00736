# 💰 Personal Expense & Budget Manager

### Smart Expense Tracking | Monthly Budget Monitoring | Financial Insights

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Storage-CSV-orange" />
  <img src="https://img.shields.io/badge/Project-PS%20No.%2036-success" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

## 📌 Project Information

| Details | Description |
|---|---|
| **Project Title** | Personal Expense & Budget Manager |
| **Problem Statement** | PS No. 36 |
| **Course** | B.Tech – Computer Science and Engineering |
| **Academic Year** | First Year |
| **Institution** | Rungta International Skills University |
| **School** | School of Computer Science and Engineering |
| **Programming Language** | Python 3 |
| **Libraries** | Pandas |
| **Data Storage** | CSV |

---

## 🚀 About The Project

The **Personal Expense & Budget Manager** is a Python-based console application designed to make personal financial management simple, organized, and efficient.

It enables users to record daily expenses, set monthly budgets, analyze category-wise spending, and monitor their financial activities through automated budget alerts.

The application uses **CSV file handling** for permanent data storage and **Pandas** for efficient expense analysis and category-wise calculations.

Whether tracking food expenses, travel costs, or everyday purchases, this application helps users understand where their money goes and maintain better spending habits.

## ✨ Key Features

- 📅 **Expense Tracking:** Record expenses with date, category, and amount.
- 💵 **Monthly Budget Management:** Set and monitor a monthly spending limit.
- 📊 **Category-wise Analysis:** Analyze expenses using Pandas `groupby()`.
- 💾 **Persistent Storage:** Automatically save expense records in `expenses.csv`.
- ⚠️ **Smart Budget Alerts:** Receive warnings when spending reaches 80% or exceeds 100% of the budget.
- 🛡️ **Input Validation:** Prevent invalid dates, negative amounts, and non-numeric inputs.
- 📈 **Financial Reports:** View total expenses, remaining balance, and spending percentage.
- 🔄 **Automatic CSV Management:** Create and update the expense file automatically.

---

## 🖥️ Application Menu

```text
========================================
     PERSONAL EXPENSE & BUDGET MANAGER
========================================

1. Set Budget
2. Add Expense
3. Category Summary
4. View Expense Report
5. Exit

========================================
Enter your choice:
```

## 📊 Budget Monitoring System

The application monitors spending against the user's monthly budget.

| Budget Usage | System Response |
|---|---|
| Below 80% | Normal spending status |
| 80% – 99.99% | ⚠️ Budget warning |
| Exactly 100% | 🔔 Budget fully used |
| Above 100% | 🚨 Budget exceeded |

**Example:**

```text
Monthly Budget : ₹5,000
Total Spent    : ₹4,200
Remaining      : ₹800
Budget Used    : 84.00%

⚠️ Warning: 84.00% of the budget used.
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core application development |
| Pandas | Data analysis and aggregation |
| CSV Module | Reading and writing expense records |
| Dictionaries | Managing structured expense data |
| Functions | Modular and reusable programming |
| Exception Handling | Managing invalid inputs and errors |

---

## 📂 Project Structure

```text
Personal-Expense-Budget-Manager/
│
├── expense_manager.py    # Main Python application
├── expenses.csv          # Persistent expense records
├── test_runner.py        # Automated test suite
│
└── README.md             # Project documentation
```

*Note: `expenses.csv` is automatically created when the application saves its first expense.*

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Personal-Expense-Budget-Manager.git
```

### 2. Navigate to the Project Directory

```bash
cd Personal-Expense-Budget-Manager
```

### 3. Install Required Dependencies

Make sure Python 3 is installed.

```bash
pip install pandas
```

### 4. Run the Application

```bash
python expense_manager.py
```

**For Windows users:**

```bash
py expense_manager.py
```

### 5. Run Automated Tests

```bash
python test_runner.py
```

---

## 🧪 Test Cases & Validation

The application was tested using normal, boundary, and invalid input scenarios.

| Test Case | Scenario | Expected Result | Status |
|---|---|---|---|
| TC-01 | Set budget to ₹5,000 | Budget successfully saved | ✅ PASS |
| TC-02 | Expense equals budget | 100% budget usage displayed | ✅ PASS |
| TC-03 | Enter negative expense | Invalid amount rejected | ✅ PASS |
| TC-04 | Enter incorrect date format | Invalid date rejected | ✅ PASS |
| TC-05 | Multiple category expenses | Correct category totals calculated | ✅ PASS |
| TC-06 | Spending reaches 80% or more | Budget warning displayed | ✅ PASS |
| TC-07 | Spending exceeds budget | Budget exceeded alert displayed | ✅ PASS |

### Example Test Scenario

**Input:**

```text
Monthly Budget = ₹5,000

Food   = ₹1,500
Travel = ₹1,000
Food   = ₹1,700
```

**Expected Report:**

```text
========== EXPENSE REPORT ==========

Category Summary:
Food   : ₹3,200
Travel : ₹1,000

Total Spent : ₹4,200
Remaining   : ₹800
Budget Used : 84.00%

Warning: 84.00% of the budget used.

====================================
```

**Test Result:** All listed test cases passed during verification.

---

## 🧠 Core Python Concepts Demonstrated

### 1. Functions
Used to divide the application into smaller, reusable modules such as:
- `set_budget()`
- `add_expense()`
- `save_expense_to_csv()`
- `get_spending_data()`
- `show_category_summary()`
- `show_report()`

### 2. Dictionaries
Used to organize expense records into structured key-value pairs.

### 3. CSV File Handling
Uses Python's `csv` module to store, retrieve, and update expense records.

### 4. Pandas Data Analysis
Uses Pandas DataFrames and `groupby()` to calculate category-wise expenditure.

```python
df.groupby("Category")["Amount"].sum()
```

### 5. Input Validation & Exception Handling
Uses validation logic and `try-except` blocks to handle incorrect user inputs without crashing the application.

---

## 🎯 Project Objectives

- Develop a practical application using Python fundamentals.
- Understand real-world CSV file handling.
- Apply dictionaries and functions in software development.
- Perform data analysis using Pandas.
- Implement budget monitoring and automated alerts.
- Improve logical thinking and problem-solving skills.

---

## 🔮 Future Enhancements

Some features that can be introduced in future versions:

- 📉 Graphical expense analysis using Matplotlib.
- 🖥️ User-friendly GUI using Tkinter.
- 📆 Monthly and yearly expense comparisons.
- 🔐 User authentication and personal accounts.
- 📤 Export financial reports to PDF and Excel.
- 🎯 Category-specific spending limits.
- ☁️ Cloud-based expense synchronization.

---

## 👨‍💻 Developed By

**Mohit Kumar**

🎓 B.Tech – Computer Science and Engineering  
🏛️ Rungta International Skills University  
🏫 School of Computer Science and Engineering

**Project:** PS No. 36 – Personal Expense & Budget Manager

---

## ⭐ Support

If you find this project useful or interesting, consider giving this repository a ⭐ on GitHub.

Your support and feedback are appreciated!

---

<p align="center">
  <b>Built with Python 🐍 | Designed for Smarter Expense Management 💰</b>
</p>
