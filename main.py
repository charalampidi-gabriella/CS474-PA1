from image import PGMImage  

def get_user_choice():
    print("Which function do you want to test?")
    print("1. Sampling")
    print("2. Quantization")
    print("3. Histogram Equalization")
    print("4. Histogram Specification")
    
    choice = input("Enter the number of your choice: ")
    return choice

image = PGMImage()
image.read_from_file('images/peppers.pgm')

choice = get_user_choice()

if choice == "1":
    image.sampling()
    new_file_name = 'images/peppers_sampled.pgm'
elif choice == "2":
    image.quantization()
    new_file_name = 'images/peppers_quantized.pgm'
elif choice == "3":
    image.histogram_equalization()  
    new_file_name = 'images/peppers_hist_eq.pgm'
elif choice == "4":
    image.histogram_specification()  
    new_file_name = 'images/peppers_hist_spec.pgm'
else:
    print("Invalid choice.")
    exit()


image.write_to_file(new_file_name)
print(f"New image written to {new_file_name}")
