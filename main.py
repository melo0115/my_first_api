from fastapi import FastAPI 


app = FastAPI()

@app.get("/")
def home_page():
    return {"message":"Time is Real"}