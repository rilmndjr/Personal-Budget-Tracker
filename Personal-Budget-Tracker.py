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