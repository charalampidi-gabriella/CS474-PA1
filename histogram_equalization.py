import numpy as np
import matplotlib.pyplot as plt

def hist_graph(data,title):
    plt.hist(data, bins = [0,20,40,60,80,100,120,140,160,180,200,220,240,260]) 
    plt.title(title) 
    plt.show()
    

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
        #Write header
        f.write(f"P5\n{width} {height}\n{maxval}\n".encode())
        #Write data
        for row in data:
            for pixel in row:
                #Clamp the pixel value within the 0-255 range
                clamped_pixel = max(0, min(255, int(pixel)))
                f.write(clamped_pixel.to_bytes(1, 'big'))

def apply_histogram_equalization(width, height, max_val, img_data):
    #Calculate the histogram
    hist, _ = np.histogram(img_data, bins=max_val + 1, range=(0, max_val))
    hist_graph(hist,"Before Histogram")
    #Calculate to cumulative distribution function (CDF)
    cdf = hist.cumsum()
    #Normalize the CDF to scale it to the full intensity range
    cdf_normalized = (cdf - cdf.min()) * max_val / (cdf.max() - cdf.min())
    #Map the original pixel values to their corresponding values in the equalized image
    equalized_img_data = cdf_normalized[img_data]
    hist_graph(equalized_img_data,"Equalizaed histogram")
    return equalized_img_data.astype(np.uint8)

def histogram_equalization(image):
    width, height, max_val, data = read_from_file(image)

    histo_data = apply_histogram_equalization(width,height,max_val,data)
    image = image[:len(image)-4]

    write_to_file(image + "_equalized.pgm",width,height,max_val,histo_data)

