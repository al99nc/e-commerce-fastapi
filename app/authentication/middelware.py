import os
from fastapi import FastAPI, UploadFile

app = FastAPI()
uploadDir = "C:/Users/gt store/Desktop/e-commerce-fastapi/app/uploads"
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if not os.path.exists(uploadDir):
        os.makedirs(uploadDir)
    with open(f"{uploadDir}/{file.filename}", "wb") as img:
        img.write(await file.read())
    return {"filename": file.filename}