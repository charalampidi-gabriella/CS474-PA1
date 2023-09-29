from image import PGMImage  

image = PGMImage()  
image.read_from_file('images/peppers.pgm')  
print(f"Original size: {image.width}x{image.height}")  

image.sampling()  
print(f"After sampling: {image.width}x{image.height}")  

image.write_to_file('images/peppers_sampled_8.pgm')  
