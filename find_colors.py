import sys
from PIL import Image
from collections import Counter

try:
    img = Image.open('LogoRedesign.png')
    img = img.convert('RGBA')
    pixels = img.getdata()
    
    valid_pixels = []
    for r, g, b, a in pixels:
        if a > 50: # ignore mostly transparent
            # ignore near white/black
            if not (r > 240 and g > 240 and b > 240) and not (r < 15 and g < 15 and b < 15):
                # ignore navy #243160 (36, 49, 96) and its close variants
                if not (abs(r - 36) < 30 and abs(g - 49) < 30 and abs(b - 96) < 30):
                    valid_pixels.append((r,g,b))
            
    counts = Counter(valid_pixels)
    for color, count in counts.most_common(15):
        print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} - Count: {count}")
except Exception as e:
    print(e)
