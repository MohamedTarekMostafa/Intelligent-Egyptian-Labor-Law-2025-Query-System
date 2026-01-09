from fastapi import FastAPI
from engine import rag_Chain
import pydantic
from pydantic import BaseModel
class question_Schema(BaseModel):
    question : str
bot = rag_Chain()
app   = FastAPI()
@app.post("/ask")
def Request(request:question_Schema):
    response = bot.invoke(request.question)
    return {"answer":response}

