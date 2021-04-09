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

class Invoice(BaseModel):
    name: str
    job: str

#URL = "http://httpbin.org/uuid"
callback_urlz = "https://reqres.in/api/users"
#URL = "https://gitlab.com/api/v4/projects/25478612/trigger/pipeline"

class InvoiceEvent(BaseModel):
    name: str
    job: str
#    id: str
#    createdAt: str

class InvoiceEventReceived(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

    

invoices_callback_router = APIRouter()

@invoices_callback_router.post(
    "{$callback_urlz}", response_model=InvoiceEventReceived
)

def invoice_notification(body: InvoiceEvent):
    pass


@app.post("/invoices/", callbacks=invoices_callback_router.routes)
def create_invoice(invoice: Invoice, callback_url: Optional[HttpUrl] = callback_urlz):
   # json = {"name":"Bhadoria","job":"SE"}
    json_resp = dict(invoice)
    x = requests.post(callback_urlz, data = json_resp)
    print(callback_urlz)
    print(x.text)
    """
    Create an invoice.
    This will (let's imagine) let the API user (some external developer) create an
    invoice.
    And this path operation will:

    * Send the invoice to the client.
    * Collect the money from the client.
    * Send a notification back to the API user (the external developer), as a callback.
        * At this point is that the API will somehow send a POST request to the
            external API with the notification of the invoice event
            (e.g. "payment successful").
    """
    # Send the invoice, collect the money, send the notification (the callback)
    return json.loads(x.text)


