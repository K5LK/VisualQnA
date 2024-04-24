from model import model_pipeline
from typing import Union
import requests
from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "app": "VisualQnA",
        "version": "1.0",
            }

@app.post("/test")
def test(text: str, image: str):
    response = requests.get(image) 
    # content = image.file.read()

    image = Image.open(io.BytesIO(response.content))

    #add model pipeline 
    result = model_pipeline(text, image)
    return {"answer": result}