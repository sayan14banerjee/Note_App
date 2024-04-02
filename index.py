from fastapi import FastAPI
from routes.notes import note 
import uvicorn

app = FastAPI()

app.include_router(note)

if __name__ == "__main__":
    uvicorn.run("index:app", reload=True)