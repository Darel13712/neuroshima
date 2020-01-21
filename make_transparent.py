from PIL import Image
from glob import glob
from os.path import join

def make_transparent(path):
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 53 and item[1] == 50 and item[2] == 50:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(path, "PNG")

def cut_in_half(path):
    img = Image.open(path)
    w, h = img.size
    img.crop((0, 0, w, h // 2)).save(path, "PNG")

def process_tile(path):
    make_transparent(path)
    cut_in_half(path)

def process_folder(path):
    files = glob(join(path, '*'))
    for file in files:
        make_transparent(file)
        cut_in_half(file)

def get_back(path):
    img = Image.open(path)
    w, h = img.size
    img.crop((0, h // 2, w, h)).rotate(180).save(path, "PNG")

def cut_for_folder(path):
    files = glob(join(path, '*'))
    for file in files:
        cut_in_half(file)