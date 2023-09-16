from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from typing import List
import uvicorn


app = FastAPI()

# Pydantic model for request body


# Initialize the classifier once, outside of the endpoint, for better performance

@app.get("/")
        return {"hello world"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
