import os
import shutil

current = os.getcwd()
for i in os.listdir():

    try:
        dashat = i.index('-')
    except ValueError:
        dashat = -1

    if dashat == -1:
        continue

    try:
        os.mkdir(i[:dashat].strip())
    except FileExistsError:
        print('folder already exists')

    shutil.move(current+'//'+i, current+'//'+i[:dashat].strip())





