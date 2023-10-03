def histogram_equalization(pgm_image):
    histogram = [0] * (pgm_image.maxval + 1)
    for row in pgm_image.pixels:
        for pixel in row:
            histogram[pixel] += 1

    total_pixels = pgm_image.width * pgm_image.height
    cdf = [0] * (pgm_image.maxval + 1)
    cdf[0] = histogram[0]
    for i in range(1, pgm_image.maxval + 1):
        cdf[i] = cdf[i - 1] + histogram[i]

    for y in range(pgm_image.height):
        for x in range(pgm_image.width):
            pgm_image.pixels[y][x] = (cdf[pgm_image.pixels[y][x]] * pgm_image.maxval) // total_pixels
        
    write_to_file(image + "equalized.pgm",width,height,max_val,histo_data)
