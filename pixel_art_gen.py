from PIL import Image

def merge_pixels(s1, s2):
    new_values = []
    R = 0
    G = 0
    B = 0

    for j in range(0,10):
        for i in range(s1,s1+10):
            new_values.append(pixel_values[i])
        s1 += 300

    for i in new_values:
        R += i[0]
        G += i[1]
        B += i[2]

    R = round(R/100)
    G = round(G/100)
    B = round(B/100)

    avg = (R,G,B)

    for j in range(0,10):
        for i in range(s2,s2+10):
            pixel_values[i] = avg
        s2 += 300


if __name__ == "__main__":
    cs = 0

    img = Image.open('bird.jpg','r')
    pixel_values = list(img.getdata())
    width, height = img.size

    for x in range(1,31):
        for i in range(0,30):
            merge_pixels(cs,cs)
            cs+= 10
        cs = x*3000

# Puts image back together and creates new image
    img2 = Image.new(img.mode, img.size)
    img2.putdata(pixel_values)
    img2.show()
    img2.save('bird2.png')
