import subprocess
import requests
import urllib
import json

LYRICS_API = "http://lyric-api.herokuapp.com/api/find"

output = subprocess.check_output(['sh', 'lyr.sh'])
artist = output.split("\n")[0].strip()
title = output.split("\n")[1].strip()

url = "{0}/{1}/{2}".format(LYRICS_API, urllib.pathname2url(artist), urllib.pathname2url(title))  

reponse = requests.get(url=url)
data = json.loads(reponse.text)

print data['lyric']