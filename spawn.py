import os
from pathlib import Path



def configBootStrap():
    '''
    <nav class="navbar navbar-expand navbar-dark bg-dark" aria-label="Second navbar example">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Always expand</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExample02">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>
        <form role="search">
          <input class="form-control" type="search" placeholder="Search" aria-label="Search">
        </form>
      </div>
    </div>
  </nav>
  '''




# If you need to modify the path modify the generic file
def spawnTools(path, templateName):
    #path = "tools"
    slashContent = "/" + path + "/"
    #templateName = "templates/tools.html"
    dir_list = os.listdir(path)
    f = open(templateName, "w")
    f.write("<!DOCTYPE html>" + "\n")
    track = 0
    for x in dir_list:
        holder = dir_list[track].rsplit(".", 1 )[0]
        content = '<a href="'+slashContent+dir_list[track]+'">'+holder+"</a>" + "<br>"
        track +=1
        f.write(content)
    f.write("</html>" + "\n")
    f.close()
