from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware

import psycopg2
from psycopg2.extras import RealDictCursor

from . import models
from .database import engine, get_db
from .routers import posts, users, auth, vote

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


while True: 
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='mickey', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        break
    except Exception as e:
        print("Connecting to datatbase failed.")
        print("Error: ", e)
        time.sleep(3)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)






     
    

    
    
