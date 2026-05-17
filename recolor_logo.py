from PIL import Image

try:
    img = Image.open('LogoRedesign.png')
    img = img.convert('RGBA')
    width, height = img.size
    
    pixels = img.load()
    
    # Target yellow color: #fbbf24 -> RGB: 251, 191, 36
    target_r, target_g, target_b = 251, 191, 36
    
    for x in range(width):
        if x <= 150:
            for y in range(height):
                r, g, b, a = pixels[x, y]
                # To maintain antialiasing but change color, we just set the new RGB.
                # If there is some color mixing from antialiasing against white instead of transparent, 
                # we might need to be careful, but usually changing RGB of a completely isolated shape is fine.
                if a > 0:
                    # Check if it's not mostly white (if it was antialiased against a white background, 
                    # but alpha is full, the edge pixels would be lighter blue. 
                    # Setting them to pure yellow might make the edge look jagged if they were mixed. 
                    # But since the user wants the sparkle yellow, we can just linearly interpolate 
                    # the "darkness" of the original blue to the yellow?
                    # No, let's just set the RGB and see. It usually works perfectly.
                    pixels[x, y] = (target_r, target_g, target_b, a)
                    
    img.save('LogoRedesign.png')
    print("Logo successfully updated.")
except Exception as e:
    print(e)
