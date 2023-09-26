class PGMImage:
    def __init__(self, width=0, height=0, maxval=255):
        self.width = width
        self.height = height
        self.maxval = maxval
        self.pixels = [[0 for _ in range(width)] for _ in range(height)]

    def read_from_file(self, filename):
        with open(filename, 'rb') as f:
            # Read header
            header = f.readline().decode().strip()
            print(header)
            if header != 'P5':
                raise ValueError('Not a PGM file')
            # Skip comments
            while True:
                line = f.readline().strip()
                if line and not line.startswith(b'#'):
                    break

            self.width, self.height = map(int, line.split())
            self.maxval = int(f.readline().strip())
            # Read pixel data
            self.pixels = [
                [int.from_bytes(f.read(1), 'big') for _ in range(self.width)]
                for _ in range(self.height)
            ]

    def write_to_file(self, filename):
        with open(filename, 'wb') as f:
            # Write header
            f.write(f"P5\n{self.width} {self.height}\n{self.maxval}\n".encode())
            # Write pixel data
            for row in self.pixels:
                for pixel in row:
                    f.write(int(pixel).to_bytes(1, 'big'))

    def get_pixel(self, x, y):
        return self.pixels[y][x]

    def set_pixel(self, x, y, value):
        self.pixels[y][x] = value



image = PGMImage()
image.read_from_file('aerial.pgm')

# Manipulate pixels (invert image in this example)
for y in range(image.height):
    for x in range(image.width):
        pixel_value = image.get_pixel(x, y)
        inverted_value = image.maxval - pixel_value
        image.set_pixel(x, y, inverted_value)

# Write the image back to a file
image.write_to_file('output.pgm')
