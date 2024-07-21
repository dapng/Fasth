from fastapi import FastAPI, Depends
from .check import check_flag
import logging
import uuid



app = FastAPI()


@app.get('/generate-uuid')
async def generate_uuid(x_falg: str = Depends(check_flag)):
    new_uuid = str(uuid.uuid4())
    if x_falg == "green":
        logging.info(f"Generated UUID: {new_uuid}, Green flag detected")
    elif x_falg == "red":
        logging.info(f"Generated UUID: {new_uuid}, Red flag detected")
    return {"uuid:", new_uuid}

