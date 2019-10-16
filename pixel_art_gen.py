from PIL import Image
import os

def merge_pixels(s1, s2,w):
    new_values = []
    R = 0
    G = 0
    B = 0

    for k in range(0,10):
        for h in range(s1,s1+10):
            new_values.append(pixel_values[h])
        s1 += w

    for i in new_values:
        R += i[0]
        G += i[1]
        B += i[2]

    R = round(R/100)
    G = round(G/100)
    B = round(B/100)

    avg = (R,G,B)

    for k in range(0,10):
        for h in range(s2,s2+10):
            pixel_values[h] = avg
        s2 += w

if __name__ == "__main__":
    img = Image.open('zelda.jpg')
    pixel_values = list(img.getdata())
    width,height = img.size
    cs = 0
    rows = height//10 + 1
    columns = width//10
    row_width = width*10

    for r in range(1,rows):
        for c in range(0,columns):
            merge_pixels(cs,cs,width)
            cs+= 10
        cs = r*row_width

    # Puts image back together and creates new image
    img2 = Image.new(img.mode, img.size)
    img2.putdata(pixel_values)
    img2.show()
    img2.save('pixel_art.png')
