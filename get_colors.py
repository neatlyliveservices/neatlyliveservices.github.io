import sys
from PIL import Image
from collections import Counter

try:
    img = Image.open('LogoRedesign.png')
    img = img.convert('RGBA')
    pixels = img.getdata()
    
    # Filter out transparent or near-transparent pixels, and white/black if needed, but let's just get everything first
    valid_pixels = []
    for r, g, b, a in pixels:
        if a > 200 and not (r > 240 and g > 240 and b > 240): # ignore transparent and near white
            valid_pixels.append((r,g,b))
            
    counts = Counter(valid_pixels)
    for color, count in counts.most_common(10):
        print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} - Count: {count}")
except Exception as e:
    print(e)
