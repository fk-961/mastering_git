import csv
import json

def load_transactions_csv(filepath : str) -> list:
    with open(filepath, newline = '') as f:
        reader = csv.DictReader(f)
        transactions_csv = []
        for row in reader:
            row['amount'] = int(row['amount'])
            transactions_csv.append(row)
    return transactions_csv

def load_transactions_json(filepath : str) -> list:
    with open(filepath, "r") as f:
        data = json.load(f)
    return data
        
def save_transactions_json(
    transactions : list,
    filepath : str
) -> None:
    with open(filepath, "w") as f:
        json.dump(transactions, f)