#uvicorn main:app --reload
import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from spawn import spawnTools
from generic import init









#Set up the directory here
c2Directory = "tools" # modify this to change the directory
c2Template = "templates/" + c2Directory + ".html" # tools.html"
c2Slash = "/" + c2Directory
c2ReturnDirectory = c2Directory+".html"
init(c2Directory, c2Template)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount(c2Slash, StaticFiles(directory=c2Directory), name=c2Directory)




@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    spawnTools(c2Directory, c2Template) 
    return templates.TemplateResponse(c2ReturnDirectory, {"request": request})
