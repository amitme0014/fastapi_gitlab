from fastapi import FastAPI
from pydantic import BaseModel #yeh pojo class ki tarah kaam aata
import http3




#https://www.youtube.com/watch?v=kCggyi_7pHg

#Fast api comes automatically with swagger '/docs daalo bas ya fir /redoc'
app = FastAPI()

db=[]

class City(BaseModel):
    name: str
    timezone: str
     

@app.get('/')
def index():
    return{'key':'value'}

@app.get('/gitlab_hit')
def hitApi():
    
    return{"client_host":resp_recvd}

@app.get('/index')
def index():
    return{'key':'index_value'}

@app.get('/cities')
def get_cities():
    return db

#@app.get('/cities/{city_id}')

#iska matlab isko City type ka object chahiye
#db.append mein city type k object ko dictionary mein convert kiya gaya aur phir db list mein store kara diya
#db[-1] returns last item from list
@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return "deleted"