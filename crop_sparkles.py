from PIL import Image

try:
    img = Image.open('LogoRedesign.png')
    img = img.convert('RGBA')
    
    # Crop the left side where the sparkles are (X <= 145)
    sparkles = img.crop((0, 0, 145, img.height))
    
    # Get bounding box of non-transparent pixels
    bbox = sparkles.getbbox()
    if bbox:
        sparkles = sparkles.crop(bbox)
        sparkles.save('menu-sparkles.png')
        print("Successfully created menu-sparkles.png")
    else:
        print("No sparkles found.")
except Exception as e:
    print(e)
