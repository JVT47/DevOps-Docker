import numpy as np
from fastapi import FastAPI

x = np.array([1,0])
A = np.array([[1,1],[1,0]])
w, V = np.linalg.eig(A)
Lambda = np.diag(w) 

def nth_fibonacci(n, Lambda, V):
    if (n < 0):
        return "n must be nonnegative"
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    try:
        return round((V@Lambda**(n-1)@V.T@x)[0])
    except:
        return "Fibonacci number too large"

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "send number to /n"}

@app.get("/{n}")
async def calculate(n: int):
    return {"fibonacci": nth_fibonacci(n, Lambda, V)}



