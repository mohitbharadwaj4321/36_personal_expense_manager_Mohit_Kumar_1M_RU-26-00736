# ========================================================
# RUNGTA INTERNATIONAL SKILLS UNIVERSITY
# SCHOOL OF COMPUTER SCIENCE AND ENGINEERING
# Bachelor of Technology - Computer Science and Engineering
#
# PS No.        : 36
# Project Title : Personal Expense & Budget Manager
# Concepts Used : Functions, Dictionaries, CSV, Pandas
# ========================================================

import os
import csv
from datetime import datetime
import pandas as pd

# Files to store data permanently on disk
EXPENSES_FILE = "expenses.csv"
BUDGET_FILE = "budget.txt"

# Global variable to keep track of monthly budget in program memory
monthly_budget = None


def load_budget():
    """Load the saved budget from budget.txt when the program starts."""
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, "r") as file:
                data = file.read().strip()
                if data:
                    return float(data)
        except:
            return None
    return None


def save_budget_to_file(budget):
    """Save the budget value into budget.txt."""
    try:
        with open(BUDGET_FILE, "w") as file:
            file.write(str(budget))
    except:
        pass


def format_amount(val):
    """Format numbers cleanly: 1000 instead of 1000.0, but 10.50 for decimals."""
    if val == int(val):
        return str(int(val))
    else:
        return f"{val:.2f}"


def validate_date(date_str):
    """Check if date is strictly in YYYY-MM-DD format and is a real calendar date."""
    try:
        parts = date_str.split("-")
        # Check if there are 3 parts (Year, Month, Day)
        if len(parts) != 3:
            return False
        
        # Year must be 4 digits, Month must be 2 digits, Day must be 2 digits
        if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
            return False
        
        # Check if it is a valid date (e.g. rejects 2026-02-30)
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False


def validate_amount(amount_str):
    """Check if entered amount is a positive number."""
    try:
        val = float(amount_str)
        if val > 0:
            return True, val
        else:
            return False, None
    except:
        return False, None


def set_budget():
    """Menu Option 1: Ask user for monthly budget and save it."""
    global monthly_budget
    user_input = input("Enter monthly budget: ").strip()

    is_valid, val = validate_amount(user_input)
    if not is_valid:
        print("Invalid amount. Amount must be a positive number.")
        return

    monthly_budget = val
    save_budget_to_file(monthly_budget)
    print(f"Monthly budget set: {format_amount(monthly_budget)}")


def save_expense_to_csv(date_str, category, amount):
    """Save a new expense row to expenses.csv using a Python Dictionary."""
    file_exists = os.path.exists(EXPENSES_FILE) and os.path.getsize(EXPENSES_FILE) > 0

    # Using Python Dictionary concept to structure the record
    expense_dict = {
        "Date": date_str,
        "Category": category,
        "Amount": amount
    }

    # Open CSV in append mode ('a') so older records are not deleted
    with open(EXPENSES_FILE, mode="a", newline="") as file:
        headers = ["Date", "Category", "Amount"]
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write headers only if file is newly created or empty
        if not file_exists:
            writer.writeheader()
            
        writer.writerow(expense_dict)


def get_spending_data():
    """Read expenses.csv using Pandas and calculate sums using groupby()."""
    # If file doesn't exist or has 0 bytes, return empty values
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        return None, 0.0, {}

    df = pd.read_csv(EXPENSES_FILE)
    if df.empty:
        return df, 0.0, {}

    # Using Pandas groupby() concept to sum amount by category
    grouped = df.groupby("Category", sort=False)["Amount"].sum()
    category_dict = grouped.to_dict()

    total_spent = float(df["Amount"].sum())
    return df, total_spent, category_dict


def print_budget_status(total_spent, budget):
    """Show spent amount, remaining budget, and warning alerts."""
    if budget is None or budget <= 0:
        print(f"Total spent: {format_amount(total_spent)}")
        return

    remaining = budget - total_spent
    print(f"Total spent: {format_amount(total_spent)} | Remaining: {format_amount(remaining)}")

    percentage = (total_spent / budget) * 100.0

    # Check alert conditions
    if percentage > 100.0:
        print(f"Budget exceeded! ({percentage:.2f}% of the budget used).")
    elif percentage == 100.0:
        print(f"Budget fully used ({percentage:.2f}%).")
    elif percentage >= 80.0:
        print(f"Warning: {percentage:.2f}% of the budget used.")


def add_expense():
    """Menu Option 2: Add an expense with validation and show budget status."""
    raw_input = input("Enter expense (Date, Category, Amount or Date): ").strip()
    if not raw_input:
        print("Input cannot be empty.")
        print("Expense not saved.")
        return

    # Check if user entered all 3 values separated by comma
    if "," in raw_input:
        parts = [p.strip() for p in raw_input.split(",")]
        if len(parts) >= 3:
            date_str = parts[0]
            category = parts[1]
            amount_str = parts[2]
        else:
            print("Invalid format. Use: Date, Category, Amount")
            print("Expense not saved.")
            return
    else:
        # Otherwise take input step by step
        date_str = raw_input
        if not validate_date(date_str):
            print("Invalid date. Use YYYY-MM-DD.")
            print("Expense not saved.")
            return
        category = input("Enter category: ").strip()
        amount_str = input("Enter amount: ").strip()

    # Validate date
    if not validate_date(date_str):
        print("Invalid date. Use YYYY-MM-DD.")
        print("Expense not saved.")
        return

    # Validate amount
    is_valid, amount = validate_amount(amount_str)
    if not is_valid:
        print("Invalid amount. Amount must be a positive number.")
        print("Expense not saved.")
        return

    # Save data to CSV
    save_expense_to_csv(date_str, category, amount)
    print("Expense saved.")

    # Show updated total and budget status
    _, total_spent, _ = get_spending_data()
    print_budget_status(total_spent, monthly_budget)


def show_category_summary():
    """Menu Option 3: Display category-wise totals using Pandas groupby result."""
    _, _, category_dict = get_spending_data()
    if not category_dict:
        print("No expenses recorded yet.")
        return

    parts = []
    for cat, amt in category_dict.items():
        parts.append(f"{cat}: {format_amount(amt)}")
    print(" | ".join(parts))


def show_report():
    """Menu Option 4: Full report with category breakdown, total spent, and budget warnings."""
    _, total_spent, category_dict = get_spending_data()
    if not category_dict:
        print("No expenses recorded yet.")
        if monthly_budget is not None:
            print(f"Monthly budget: {format_amount(monthly_budget)} | Remaining: {format_amount(monthly_budget)}")
        return

    # Display category breakdown
    parts = []
    for cat, amt in category_dict.items():
        parts.append(f"{cat}: {format_amount(amt)}")
    print(" | ".join(parts))

    # Display total, remaining and warning message
    print_budget_status(total_spent, monthly_budget)


def main():
    global monthly_budget
    # Load previously saved budget if it exists
    monthly_budget = load_budget()

    # Main menu loop
    while True:
        print("\n==========================================")
        print("   PERSONAL EXPENSE & BUDGET MANAGER")
        print("==========================================")
        print("1. Set budget")
        print("2. Add expense")
        print("3. Category summary")
        print("4. Report")
        print("5. Exit")
        print("------------------------------------------")

        choice = input("Enter your choice (1-5): ").strip().lower()

        if choice in ["1", "1.", "set budget", "set"]:
            set_budget()
        elif choice in ["2", "2.", "add expense", "add"]:
            add_expense()
        elif choice in ["3", "3.", "category summary", "summary"]:
            show_category_summary()
        elif choice in ["4", "4.", "report"]:
            show_report()
        elif choice in ["5", "5.", "exit", "quit", "q"]:
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


# Run the program only when executed directly
if __name__ == "__main__":
    main()
