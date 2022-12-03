import json
import requests
from PIL import Image
import shutil
import urllib
from tkinter import *
import threading

def json_full_search(lookup_key, json_dict, search_result = []):
    if type(json_dict) == dict:
        for key, value in json_dict.items():
            if key == lookup_key:
                search_result.append(value)
            json_full_search(lookup_key, value, search_result)
    elif type(json_dict) == list:
        for element in json_dict:
            json_full_search(lookup_key, element, search_result)
    return search_result

# function begin


data_file = './lol.json'
with open(data_file) as data_file:
    data = json.load(data_file)
    names = json_full_search('name', data)
    urls = json_full_search('url', data)

print(urls[5])


artist = names[0]
track = names[3]
album = names[1]

album_url = urls[5]

root = Tk()
root.title("Current Track")
root.geometry("300x100")

'''
#album_url = str(urls[0])

response = requests.get(album_url)

if response.status_code:
    fp = open('album_cover.png', 'wb')
    fp.write(response.content)
    fp.close()

album_cover_image = PhotoImage(file = 'album_cover.png')
imageLabel = Label(image = album_cover_image).pack()
'''

artistLabel = Label(root, text = 'Artist: ' + artist).pack()
trackLabel = Label(root, text = 'Track: ' + track).pack()
albumLabel = Label(root, text = 'Album: ' + album).pack()
root.mainloop()

# function end