from PIL import Image, ImageOps

mode=int(raw_input('Input:'))

size = 100,100

img = Image.open('1.jpg')
img_with_border = ImageOps.expand(img,border=mode,fill='black')
img_with_border = ImageOps.solarize(img_with_border, threshold=128) 
if(mode > 0):
    img_with_border.thumbnail(size, Image.ANTIALIAS)
else:
    img_with_border = img_with_border.resize(size, Image.ANTIALIAS)
    

print("Image 1:",img.size)
print("Image 2:",img_with_border.size)

    
img_with_border.save('imaged-with-border.png')







