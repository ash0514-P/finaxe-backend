from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Finaxe Backend is working!"}

