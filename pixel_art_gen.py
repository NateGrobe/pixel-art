#!/usr/bin/env python3

from PIL import Image
import os

# gets 10x10 squares of pixels, averages their colour and replaces those 100 pixels with 100 new pixels of the new colour
def merge_pixels(s1, s2,w):
    new_values = []
    R = 0
    G = 0
    B = 0

    for k in range(0,10):
        for h in range(s1,s1+10):
            new_values.append(pixel_values[h])
        s1 += w

    for value in new_values:
        R += value[0]
        G += value[1]
        B += value[2]

    R = round(R/100)
    G = round(G/100)
    B = round(B/100)

    avg = (R,G,B)

    for k in range(0,10):
        for h in range(s2,s2+10):
            pixel_values[h] = avg
        s2 += w

if __name__ == "__main__":
    # choose an image
    imgs = os.listdir("./imgs")
    print("Choose an image by typing its number: ")

    for i in range(0, len(imgs)):
        print(f"{i+1}. {imgs[i]}")

    choice = int(input('> '))
    img_choice = imgs[choice - 1]
    img = Image.open(f"./imgs/{img_choice}")

    # calculates number of rows and columns for new pixels
    pixel_values = list(img.getdata())
    width,height = img.size
    rows = height//10 + 1
    columns = width//10
    row_width = width*10

    # loops through the image calling the merge_pixels function
    cs = 0
    for r in range(1,rows):
        for c in range(0,columns):
            merge_pixels(cs,cs,width)
            cs+= 10
        cs = r*row_width

    # Puts image back together, displays, and creates new image
    img2 = Image.new(img.mode, img.size)
    img2.putdata(pixel_values)
    img2.show()
    img2.save(f'{img_choice.split(".")[0]}.png')
