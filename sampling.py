
def sampling(self):
    factor = 0
    while factor not in [2, 4, 8]:
        print("Select a sampling factor:")
        print("• 2")
        print("• 4")
        print("• 8")
        choice = input()
        if choice == "2":
            factor = 2
        elif choice == "4":
            factor = 4
        elif choice == "8":
            factor = 8
        else:
            print("Invalid choice. Please try again.")
    # Subsampling
    subsampled_array = []
    for row in range(0, self.height, factor):
        new_row = [self.get_pixel(col, row) for col in range(0, self.width, factor)]
        subsampled_array.append(new_row)
        
    # Resize
    resized_array = []
    for row in subsampled_array:
        expanded_row = []
        for pixel in row:
            expanded_row.extend([pixel] * factor)
        resized_array.extend([expanded_row] * factor)
    self.pixels = resized_array
    self.height = len(resized_array)
    self.width = len(resized_array[0]) if self.height > 0 else 0
