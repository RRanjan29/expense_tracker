import csv
from datetime import datetime

FILENAME = "expenses.csv"

def load_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expense(expense):
    file_exists = False
    try:
        with open(FILENAME, mode='r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(FILENAME, mode='a', newline='') as file:
        fieldnames = ['date', 'amount', 'category', 'note']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense)

def add_expense():
    amount = input("Enter amount spent: ₹")
    category = input("Enter category (e.g., food, travel, etc.): ")
    note = input("Any note? (optional): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    expense = {
        'date': date,
        'amount': amount,
        'category': category,
        'note': note
    }
    save_expense(expense)
    print("✅ Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n----- All Expenses -----")
    for e in expenses:
        print(f"{e['date']} | ₹{e['amount']} | {e['category']} | {e['note']}")

def total_expenses():
    expenses = load_expenses()
    total = sum(float(e['amount']) for e in expenses)
    print(f"\n💸 Total Expenses: ₹{total:.2f}")

def filter_by_category():
    cat = input("Enter category to filter: ")
    expenses = load_expenses()
    filtered = [e for e in expenses if e['category'].lower() == cat.lower()]
    if not filtered:
        print("No expenses found for this category.")
        return
    print(f"\n--- Expenses in '{cat}' ---")
    for e in filtered:
        print(f"{e['date']} | ₹{e['amount']} | {e['note']}")

def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Filter by Category")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            print("Bye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
