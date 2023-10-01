def quantization(self):
    quantization_level = 0
    while quantization_level not in [2, 8,32,128]:
        print("Select a quantization_level:")
        print("• 128")
        print("• 32")
        print("• 8")
        print("• 2")
        choice = input()
        if choice == "128":
            quantization_level = 128
        elif choice == "32":
            quantization_level = 32
        elif choice == "8":
            quantization_level = 8
        elif choice == "2":
            quantization_level = 2
        else:
            print("Invalid choice. Please try again.")
    
    offset = 256 // quantization_level

    scaling_factor = 255 / (quantization_level - 1) if quantization_level > 1 else 255

    new_pixel_values = [round(i * scaling_factor) for i in range(quantization_level)]

    for row in range(self.height):
        for col in range(self.width):
            pixel_value = self.get_pixel(col, row)
            index = min(pixel_value // offset, quantization_level - 1)
            self.set_pixel(col, row, new_pixel_values[index])