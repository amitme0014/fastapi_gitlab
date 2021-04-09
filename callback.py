from typing import Optional

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, HttpUrl
from time import time
import httpx
import asyncio
import json
from fastapi.responses import JSONResponse

app = FastAPI()

#URL = "http://httpbin.org/uuid"
URL = "https://jsonplaceholder.typicode.com/comments"

async def request(client):
    response = await client.get(URL)
    return response.text


async def task():
    async with httpx.AsyncClient() as client:
        task = request(client)
       # tasks = [request(client) for i in range(1)]
        #result = await asyncio.gather(*tasks)
        result = await asyncio.gather(task)
        for i, resp in enumerate(result):
            with open(f"response.json", "w") as f:
                json.dump(resp, f)
        print(resp)
        print("*****************************")
        print(type(resp))
        print("*****************************")
        return json.loads(resp)


@app.get('/kajal')
async def f():
    start = time()
    return await task()
    #print("time: ", time() - start)
    

class Invoice(BaseModel):
    name: str
    job: str

class InvoiceEventReceived(BaseModel):
    ok: bool

class InvoiceEvent(BaseModel):
    description: str
    paid: bool


invoices_callback_router = APIRouter()

@invoices_callback_router.post(
    "{$callback_url}/", response_model=InvoiceEventReceived
)
def invoice_notification(body: InvoiceEvent):
    print("In notification")


@app.post("/invoices/", callbacks=invoices_callback_router.routes)
def create_invoice(invoice: Invoice, callback_url: Optional[HttpUrl] = None):
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
    print(callback_url)
    print(invoice)
    return {"msg": "Invoice received"}