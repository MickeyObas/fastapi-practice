from fastapi import FastAPI, status, HTTPException, Response
from fastapi.params import Body

from pydantic import BaseModel
from typing import Optional 
import psycopg2
from psycopg2.extras import RealDictCursor

from random import randrange
from pprint import pprint
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True: 
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='mickey', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        break
        print('Database connection was successful!')
    except Exception as e:
        print("Connecting to datatbase failed.")
        print("Error: ", e)
        time.sleep(3)


my_posts = [{"title": "The Suite Life of Zack and Cody", "content": "This is some content.", "id":1}, {"title": "Shrek 3", "content": "Hey now you a rockstar", "id":2}]

def find_post(id):
    for i in my_posts:
        if i['id'] == id:
            return i

def find_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# These are called path operations.

@app.get('/posts')
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    print(type(post))
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()

    conn.commit()

    return {"data": new_post}


@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The post with id:{} was not found.".format(id))
    return {"post-detail": post}


@app.delete('/posts/{id}')
def delete_post(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))

    conn.commit()

    deleted_post = cursor.fetchone()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The post with id:{} was not found.".format(id))

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
    conn.commit()
    
    updated_post = cursor.fetchone()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The post with id:{} was not found.".format(id))
    
    return {'message': "Post has been updated.", 'data': updated_post}