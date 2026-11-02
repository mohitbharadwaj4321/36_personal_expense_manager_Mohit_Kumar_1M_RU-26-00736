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

# File names
EXPENSES_FILE = "expenses.csv"
BUDGET_FILE = "budget.txt"

# Global variable to store monthly budget in memory
monthly_budget = None


def load_budget():
    """Load previously saved monthly budget if budget.txt exists."""
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, "r", encoding="utf-8") as f:
                data = f.read().strip()
                if data:
                    return float(data)
        except (ValueError, IOError):
            return None
    return None


def save_budget_to_file(budget):
    """Save the monthly budget to budget.txt."""
    try:
        with open(BUDGET_FILE, "w", encoding="utf-8") as f:
            f.write(str(budget))
    except IOError:
        pass


def format_amount(value):
    """Helper to format numbers cleanly (e.g. 1000 instead of 1000.0 when whole number)."""
    if value == int(value):
        return str(int(value))
    return f"{value:.2f}"


def validate_date(date_str):
    """Validate that date is strictly in YYYY-MM-DD format."""
    try:
        parts = date_str.split("-")
        if len(parts) != 3:
            return False
        # Year must be 4 digits, month and day must be 2 digits
        if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
            return False
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount_str):
    """Validate that amount is a valid positive number."""
    try:
        val = float(amount_str)
        if val > 0:
            return True, val
        return False, None
    except ValueError:
        return False, None


def set_budget():
    """Menu Option 1: Lets user set monthly budget."""
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
    """Append a new expense record using a dictionary and CSV writer."""
    file_exists = os.path.exists(EXPENSES_FILE) and os.path.getsize(EXPENSES_FILE) > 0
    
    # Using dictionary concept to structure the expense record
    expense_record = {
        "Date": date_str,
        "Category": category,
        "Amount": amount
    }

    with open(EXPENSES_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["Date", "Category", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense_record)


def get_spending_data():
    """Read expenses with Pandas DataFrame and compute totals using groupby()."""
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        return None, 0.0, {}

    df = pd.read_csv(EXPENSES_FILE)
    if df.empty:
        return df, 0.0, {}

    # Category-wise spending using groupby()
    # Preserving the first appearance order of categories
    grouped = df.groupby("Category", sort=False)["Amount"].sum()
    category_dict = grouped.to_dict()

    total_spent = float(df["Amount"].sum())
    return df, total_spent, category_dict


def print_budget_status(total_spent, budget):
    """Display total spent, remaining budget and warnings (80% warning and >100% exceeded)."""
    if budget is None or budget <= 0:
        print(f"Total spent: {format_amount(total_spent)}")
        return

    remaining = budget - total_spent
    print(f"Total spent: {format_amount(total_spent)} | Remaining: {format_amount(remaining)}")

    percentage = (total_spent / budget) * 100.0

    if percentage > 100.0:
        print(f"Budget exceeded! ({percentage:.2f}% of the budget used).")
    elif percentage == 100.0:
        print(f"Budget fully used ({percentage:.2f}%).")
    elif percentage >= 80.0:
        print(f"Warning: {percentage:.2f}% of the budget used.")


def add_expense():
    """Menu Option 2: Add expense with input validation and budget status."""
    raw_input = input("Enter expense (Date, Category, Amount or Date): ").strip()
    if not raw_input:
        print("Input cannot be empty.")
        print("Expense not saved.")
        return

    # Check if user entered comma-separated input or step-by-step
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
        date_str = raw_input
        # Validate date early if entering step-by-step
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
    is_valid_amount, amount = validate_amount(amount_str)
    if not is_valid_amount:
        print("Invalid amount. Amount must be a positive number.")
        print("Expense not saved.")
        return

    # Save to CSV
    save_expense_to_csv(date_str, category, amount)
    print("Expense saved.")

    # Show total spent and remaining budget
    _, total_spent, _ = get_spending_data()
    print_budget_status(total_spent, monthly_budget)


def show_category_summary():
    """Menu Option 3: Display category-wise spending using groupby()."""
    _, _, category_dict = get_spending_data()
    if not category_dict:
        print("No expenses recorded yet.")
        return

    summary_parts = [f"{cat}: {format_amount(amt)}" for cat, amt in category_dict.items()]
    print(" | ".join(summary_parts))


def show_report():
    """Menu Option 4: Full report with category breakdown, total spent, and budget warnings."""
    _, total_spent, category_dict = get_spending_data()
    if not category_dict:
        print("No expenses recorded yet.")
        if monthly_budget is not None:
            print(f"Monthly budget: {format_amount(monthly_budget)} | Remaining: {format_amount(monthly_budget)}")
        return

    # Category summary line
    summary_parts = [f"{cat}: {format_amount(amt)}" for cat, amt in category_dict.items()]
    print(" | ".join(summary_parts))

    # Total spent, remaining budget, and warnings
    print_budget_status(total_spent, monthly_budget)


def main():
    global monthly_budget
    # Load previously stored budget if any
    monthly_budget = load_budget()

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


if __name__ == "__main__":
    main()

