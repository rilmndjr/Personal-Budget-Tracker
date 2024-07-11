transactions = []

def add_transcations(transactions):
    type = input("Enter transaction type (income/expense): ").lower()
    amount = float(input("Enter transaction amount: "))
    description = input("Enter transaction description: ")

transactions = {
    "type": type,
    "amount": amount,
    "description": description
}

transactions.append(transactions)
print("Transaction added successfully!")

def view_transactions(transaction):
    if not transactions:
        print("No transactions found.")
    else:
        for i, transaction in enumerate(transaction, start=1):
            print(f"{i}. Type: {transaction['type'].capitaliza()}, Amount: {transaction['amount']}, Description: {['description']}")

def update_transaction(transactions):
    view_transactions(transactions)
    index = int(input("Enter new transaction type (income/expense): ")) -1

    if 0 <= index < len(transactions):
        type = input("Enter new transaction type (income/expense): ").lower()
        amount = float(input("Enter new transaction amount: "))
        description = input("Enter new transaction description: ")

        transactions[index] = {
            "type": type,
            "amount": amount,
            "description": description
        }
        print("Transaction updated successfully!")
    else:
        print("Invalid transaction number.")

def delete_transaction(transactions):
    view_transactions(transactions)
    index = int(input("Enter the transaction number to delete: ")) -1
    if 0 <= index < len(transactions):
        transactions.pop(index)
        print("Transaction deleted successfully!")
    else:
        print("Invalid transaction number.")