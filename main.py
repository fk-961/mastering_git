from fastapi import FastAPI
from python_practice.transaction_logic import load_transactions_csv

app = FastAPI()

transactions = load_transactions_csv("./python_practice/transactions.csv")
    
@app.get("/total")
def total():
    return {"total" : sum(t["amount"] for t in transactions)}

@app.get("/transactions/{category}")
def filter(category : str):
    return [t for t in transactions if t["category"] == category]

@app.get("/summary")
def summary():
    result = {}
    
    for t in transactions:
        cat = t["category"]
        result[cat] = result.get(cat, 0) + t["amount"]
        
    return result