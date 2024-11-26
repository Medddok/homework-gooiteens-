# homework 1 26.11.2024

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/calculate")
async def calculate(operation: str, num1: float, num2: float):
    if operation == "+":
        return {"result": num1 + num2}
    elif operation == "-":
        return {"result": num1 - num2}
    return {"error": "Invalid operation. Use '+' or '-'."}

if __name__ == "__main__":
    print("Server is running at: http://127.0.0.1:8000/calculate")
    uvicorn.run(app, host="127.0.0.1", port=8000)
