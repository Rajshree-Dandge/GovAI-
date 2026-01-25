# For communication with frontend . This is Api Layer .It sends images to detective and brain

# ---1.importing lib-----
from fastapi import FastAPI,File,Form 
# fastapi tools for handling web request, files and text forms
from fastapi.middleware.cors import CORSMiddleware
# allow react frontend to talk to this py backend
import sqlite3
# py built in db to store complaints
import os
# lib to manage folders and file path on computer

# ---2.creating app object-----
app=FastAPI()
# creating app object to handle the incoming request

# ---3.cors middleware  to allow frontend to talk to backend  without any blocked---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow any website (react localhost) to connect
    allow_Credentials=True,
    # allow cookies or auth if needed further
    allow_methods=["*"],
    # allow all type of request
    allow_headers=["*"],
    # allow all headers
)

# ---4.db initialization-----
def init_db():
    conn=sqlite3.connect("grievance.db")
    # connects to(or creates) a file  named grievance.db
    cursor=conn.cursor()
    # cursor used to write commands in db

    # create a table if it does not exist yet
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS complaints(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   text_desc TEXT,
                   image_path TEXT,
                   status TEXT DEFAULT 'pending',
                   priority TEXT DEFAULT 'low'
                   )
''')
    conn.commit()
    conn.close()
    # save changes to db and terminate connection

init_db()

# ---5.ROUTES---
@app.get("/")
def home():
    return {"message":"Backend is running!!"}
# basic route to check if backend is running



