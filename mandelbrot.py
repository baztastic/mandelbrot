import numpy as np
from pylab import imshow, show, savefig
from timeit import default_timer as timer


def mandel(x, y, max_iters, radius):
    """
      Given the real and imaginary parts of a complex number,
      determine if it is a candidate for membership in the Mandelbrot
      set given a fixed number of iterations.
    """
    c = complex(x, y)
    z = c
    for i in range(max_iters):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= radius * 2:  # default 4
            return i

    return max_iters


def create_fractal(image, iters, radius, min_x=-2.0, max_x=1.0, min_y=-1.0, max_y=1.0):
    """
      Generate the typical Mandelbrot set plot for a given number of
      iterations and radius
    """
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters, radius)
            image[y, x] = color


for r in np.arange(1, 2, 1):
    # set range and savefig to generate pictures at different radii

    image = np.zeros((1024, 1536), dtype=np.uint8)
    start = timer()
    # r = 0.01  # to manually set some value for r
    radius = r * 2.

    create_fractal(image, 20, radius, -2.0, 1.0, -1.0, 1.0)
    dt = timer() - start

    print("Mandelbrot with radius " + str(radius) + " created in %f s" % dt)
    imshow(image)
    # savefig(str(radius)+'.png')
    show()
