

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from processor import VideoProcessor
import shutil

app = FastAPI()
processor = VideoProcessor()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_path = f"storage/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    results = processor.process(file_path)
    return results