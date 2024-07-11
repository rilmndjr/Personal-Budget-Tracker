def add_transaction(transactions):
    transaction_type = input("Enter transaction type (income/expense): ").lower()
    transaction_amount = float(input("Enter transaction amount: "))
    transaction_description = input("Enter transaction description: ")
    
    transaction = {
        "type": transaction_type,
        "amount": transaction_amount,
        "description": transaction_description
    }
    
    transactions.append(transaction)
    print("Transaction added successfully!")

def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
    else:
        for i, transaction in enumerate(transactions, start=1):
            print(f"{i}. Type: {transaction['type'].capitalize()}, Amount: {transaction['amount']}, Description: {transaction['description']}")

def update_transaction(transactions):
    view_transactions(transactions)
    index = int(input("Enter the transaction number to update: ")) - 1
    
    if 0 <= index < len(transactions):
        transaction_type = input("Enter new transaction type (income/expense): ").lower()
        transaction_amount = float(input("Enter new transaction amount: "))
        transaction_description = input("Enter new transaction description: ")
        
        transactions[index] = {
            "type": transaction_type,
            "amount": transaction_amount,
            "description": transaction_description
        }
        
        print("Transaction updated successfully!")
    else:
        print("Invalid transaction number.")

def delete_transaction(transactions):
    view_transactions(transactions)
    index = int(input("Enter the transaction number to delete: ")) - 1
    
    if 0 <= index < len(transactions):
        transactions.pop(index)
        print("Transaction deleted successfully!")
    else:
        print("Invalid transaction number.")

def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        elif transaction["type"] == "expense":
            balance -= transaction["amount"]
    
    print(f"Current balance: {balance}")

def display_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Calculate Balance")
    print("6. Exit")

def main():
    transactions = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            update_transaction(transactions)
        elif choice == '4':
            delete_transaction(transactions)
        elif choice == '5':
            calculate_balance(transactions)
        elif choice == '6':
            print("Exiting Personal Budget Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
