#!/usr/bin/python3

from config import Config
from api import API

import pathlib
import requests
import shutil
import os
import sys
import re

# To be able to change our wallpaper on Windows, we need this import!
if sys.platform == "win32":
  import ctypes

def getWorkingDir():
  if not os.path.exists(os.path.join(pathlib.Path.home(), "Wallpaper Roulette")):
    os.mkdir(os.path.join(pathlib.Path.home(), "Wallpaper Roulette"))
  return os.path.join(pathlib.Path.home(), "Wallpaper Roulette")

def getDownloadDir():
  if not os.path.exists(os.path.join(workingDir, "Downloads")):
    os.mkdir(os.path.join(workingDir, "Downloads"))
  return os.path.join(workingDir, "Downloads")

workingDir = getWorkingDir()
config = Config(workingDir)
downloadDir = getDownloadDir()
url = API(config).getURL()

def oldFileHandler():
  if config.getRemoveOld() is True: 
    for file in os.listdir(downloadDir):
      filePath = os.path.join(downloadDir, file)

      try:
        if os.path.isfile(filePath): 
          os.unlink(filePath)
      except Exception as e: 
        print('Failed to delete %s. Reason: %s' % (filePath, e))

def downloadImage(url, id):
  ext = re.search("\.[0-9a-z]+$", url)
  fileName = "{0}{1}".format(id, ext[0]) #url.split("/")[-1]

  if os.path.exists(os.path.join(downloadDir, fileName)):
    setWallpaper(os.path.join(downloadDir, fileName))
  else:
    req = requests.get(url, stream = True)
    if req.status_code == 200:
      req.raw.decode_content = True

      with open(os.path.join(downloadDir, fileName), 'wb') as file:
        shutil.copyfileobj(req.raw, file)

      setWallpaper(fileName)
    else:
      return False

def setWallpaper(filename):
  file = os.path.join(downloadDir, filename)

  # This works only on Windows 10
  if sys.platform == "win32":
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file , 0)

  # This works only on Linux when using Gnome.
  if sys.platform == "linux":
    os.system("gsettings set org.gnome.desktop.background picture-uri " + file)

def getRandomImage():
  req = requests.get(url)  
  downloadImage(req.json()[0]["file_url"], req.json()[0]["id"])

if __name__ == "__main__":
  oldFileHandler()
  getRandomImage()