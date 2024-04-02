from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

note = APIRouter()

note.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

@note.get('/', response_class= HTMLResponse)
async def index(request: Request):
    docs = conn.Notes.Notes.find({})
    new_docs = []
    for doc in docs:
        new_docs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse('index.html', {"request":request, "new_docs": new_docs})

@note.post('/')
async def insert_note(request: Request):
    form = await request.form()
    dict_form = dict(form)
    dict_form["important"] = True if dict_form.get("important") == 'on' else False  # type: ignore
    note = conn.Notes.Notes.insert_one(dict_form)
    return {"success": True}
    

@note.get('/about', response_class= HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse('about.html', {"request":request})