import csv
import os

# Define the file name for storing expenses
file_name = 'expenses.csv'

def add_expense(date, description, amount):
    """Add a new expense to the CSV file."""
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("Expense added successfully!")

def view_expenses():
    """View all expenses stored in the CSV file."""
    if os.path.exists(file_name):
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            print("Date\t\tDescription\t\tAmount")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}")
    else:
        print("No expenses recorded yet.")

def main():
    """Main function to run the expense tracker."""
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(date, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
