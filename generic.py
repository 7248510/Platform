# Generic
import os
from spawn import spawnTools


def init(workingDirectory, workingTemplate):
    currentDir = os.getcwd()
    content = os.listdir(currentDir)
    templateDir = "templates"
    if workingDirectory not in content:
        try:
            os.mkdir(workingDirectory)
        except OSError as e:
            print(e)
    if templateDir not in content:
        try:
            os.mkdir(templateDir)
        except OSError as e:
            print(e)
    

    if len(os.listdir(templateDir)) == 0:
        spawnTools(workingDirectory, workingTemplate)
