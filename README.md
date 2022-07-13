# Platform
* Platform is a post-exploitation tool
* The fastapi_dir_browse is a skeleton implementation of directory browsing for fastapi
* The templates and tool folder will be created by default. In order to change the directory<br>change the c2Directory variable in main.py
* If you request the index page the folder will be refreshed

# Goal:
* Replace python3 -m http.server 8080

## Running platform
* uvicorn main:app --reload 
