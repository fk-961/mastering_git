from fastapi import FastAPI
from pydantic import BaseModel

from python_practice.transaction_logic import load_transactions_json, save_transactions_json

app = FastAPI()

transactions = load_transactions_json("./python_practice/transactions.json")

class Transaction(BaseModel):
    amount: int
    category: str
    
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

@app.post("/transactions")
def add_transaction(transaction: Transaction):
    transactions.append(transaction.model_dump())
    
    save_transactions_json(transactions, "./python_practice/transactions.json")
    
    return {
        "status" : "added",
        "transaction" : transaction
    }