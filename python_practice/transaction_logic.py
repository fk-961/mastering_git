import csv

def load_transactions_csv(filepath : str) -> list:
    with open(filepath, newline = '') as f:
        reader = csv.DictReader(f)
        transactions_csv = []
        for row in reader:
            row['amount'] = int(row['amount'])
            transactions_csv.append(row)
    return transactions_csv