# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:15:13 2023

@author: suraj
"""


import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from tkinter import filedialog
import requests

def read_file_as_b64(image_path):
    with open(image_path, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string

def slect_image():
    filename = filedialog.askopenfilename()
    return filename

def view_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    image_buf = io.BytesIO(image_bytes)
    i = mpimg.imread(image_buf, format='JPG')
    plt.imshow(i, interpolation='nearest')
    plt.show()
    return

server = 'http://vcm-21170.vm.duke.edu'

def main():
    filename = slect_image()
    b64_str = read_file_as_b64(filename)
    in_data = {"image": b64_str,
               "net_id": 'su44',
               "id_no": 1}
    r = requests.post(server + "/add_image", json=in_data)
    print(r.status_code)
    print(r.text)
    
    r = requests.get(server + "/get_image/su44/1")
    print(r.status_code)
    print(r.text)
    view_b64_image(r.text)

if __name__ == "__main__":
    main()
