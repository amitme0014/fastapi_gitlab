from typing import Optional

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, HttpUrl
from time import time
import httpx
import asyncio
import json
from fastapi.responses import JSONResponse
import requests

app = FastAPI()



@app.post('/cities')
def create_city():
    files = {
        'token': (None, '33e4d65cad947e3a8110555b310f1a'),
        'ref': (None, 'master'),
        'variables[SERVICE]': (None, 'Kajal')
    }
    response = requests.post('https://gitlab.com/api/v4/projects/25478612/trigger/pipeline', files=files)
    return json.loads(response.text)    