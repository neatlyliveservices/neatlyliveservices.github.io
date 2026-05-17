import sys
from PIL import Image

try:
    img = Image.open('LogoRedesign.png')
    img = img.convert('RGBA')
    width, height = img.size
    
    # Calculate vertical projection (sum of alpha values per column)
    projection = [0] * width
    for x in range(width):
        col_alpha = 0
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            col_alpha += a
        projection[x] = col_alpha

    # Print exact projection around 120-170
    for i in range(120, 170):
        print(f"X:{i} -> {projection[i]}")
        
except Exception as e:
    print(e)
