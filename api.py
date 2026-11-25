from fastapi import FastAPI
from pydantic import BaseModel
from calculator_core import Calculate
from fastapi.responses import FileResponse

app = FastAPI()
calc = Calculate()                # one calculator, shared by every request

class SumRequest(BaseModel):
    a: float
    op: str
    b: float

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/calculate")
def calculate(req: SumRequest):
    result = calc.operation(req.a,req.op, req.b)
    return {"result": result}

@app.get("/history")
def history():
    return {"history": calc.get_history()}

@app.delete("/history")
def clear():
    calc.clear_history()
    return {"message": "History cleared"}