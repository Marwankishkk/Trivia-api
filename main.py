from fastapi import FastAPI
from services import fetch_trivia

app = FastAPI(
    title="Trivia API",
    description="A simple Trivia and Quiz API powered by Open Trivia Database",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to the Trivia API! Use `/trivia` to fetch trivia questions."}

@app.get("/trivia/")
def get_trivia(amount: int = 10, category: int = None, difficulty: str = "easy"):
    """
    Fetch trivia questions by amount, category, and difficulty.
    """
    questions = fetch_trivia(amount, category, difficulty)
    return {"questions": questions}
