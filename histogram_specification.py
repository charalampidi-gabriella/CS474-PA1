import numpy as np


def read_from_file(filename):
        with open(filename, 'rb') as f:
            # Read header
            header = f.readline().decode().strip()
            if header != 'P5':
                raise ValueError('Not a PGM file')
            # Skip comments
            while True:
                line = f.readline().strip()
                if line and not line.startswith(b'#'):
                    break

            width, height = map(int, line.split())
            maxval = int(f.readline().strip())
            # Read data
            pixels = [
                [int.from_bytes(f.read(1), 'big') for _ in range(width)]
                for _ in range(height)
            ]
            return width,height,maxval,pixels

def write_to_file(filename,width,height,maxval,data):
    with open(filename, 'wb') as f:
        # Write header
        f.write(f"P5\n{width} {height}\n{maxval}\n".encode())
        # Write data
        for row in data:
            for pixel in row:
                # Clamp the pixel value within the 0-255 range
                clamped_pixel = max(0, min(255, int(pixel)))
                f.write(clamped_pixel.to_bytes(1, 'big'))

def apply_histogram_specification(input_data, target_hist,max_val):
      # Calculate the histogram of the input image
    hist, _ = np.histogram(input_data, bins=max_val + 1, range=(0, max_val))

    # Calculate the CDF of the input histogram
    cdf = hist.cumsum()

    # Calculate the histogram of the target histogram
    target_hist, _ = np.histogram(target_hist, bins=max_val + 1, range=(0, max_val))

    # Calculate the CDF of the target histogram
    target_cdf = target_hist.cumsum()

    # Map the input pixel values to match the target CDF
    spec_data = np.interp(cdf[input_data], target_cdf, np.arange(max_val + 1))

    return spec_data.astype(np.uint8)

def histogram_specification(filename,target_file):
    width, height, max_val, data = read_from_file(filename)
    _width, _height, _max_val, target_data = read_from_file(target_file)

    histo_data = apply_histogram_specification(data,target_data,max_val)
        
    write_to_file(filename,width,height,max_val,histo_data)