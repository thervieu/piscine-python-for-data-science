import numpy as np
import matplotlib.pyplot as plt


def ft_invert(image):
    """Inverts the color of the image received."""
    # Get the number of rows and columns in the original matrix
    rows = len(image)
    cols = len(image[0])

    # Create a new empty image with swapped dimensions
    inverted_image = [[255 - image[i][j] for j in range(cols)] for i in range(rows)]

    plt.imshow(inverted_image)
    # Show the plot
    plt.show()
    return


def ft_red(image):
    """Keeps the color red of the image received."""

    image = np.copy(image)
    # Get the red, green, and blue channels
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    # Set the green and blue channels to zero (i.e., remove red and blue colors)
    green_channel[:] = 0
    blue_channel[:] = 0

    # Merge the modified channels back together
    red_image = np.stack((red_channel, green_channel, blue_channel), axis=-1)
    plt.imshow(red_image)
    # Show the plot
    plt.show()


def ft_green(image):
    """Keeps the color green of the image received."""

    image = np.copy(image)
    # Get the red, green, and blue channels
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    # Set the green and blue channels to zero (i.e., remove red and blue colors)
    red_channel[:] = 0
    blue_channel[:] = 0

    # Merge the modified channels back together
    green_image = np.stack((red_channel, green_channel, blue_channel), axis=-1)
    plt.imshow(green_image)
    # Show the plot
    plt.show()


def ft_blue(image):
    """Keeps the color blue of the image received."""

    image = np.copy(image)
    # Get the red, green, and blue channels
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    # Set the green and blue channels to zero (i.e., remove red and blue colors)
    green_channel[:] = 0
    blue_channel[:] = 0

    # Merge the modified channels back together
    blue_image = np.stack((red_channel, green_channel, blue_channel), axis=-1)
    plt.imshow(blue_image)
    # Show the plot
    plt.show()


def ft_grey(image):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Create a new grayscale image with the same dimensions
    grey_image = [[0 for _ in range(width)] for _ in range(height)]

    # Convert the image to grayscale using the luminosity method (average of RGB values)
    for y in range(height):
        for x in range(width):
            r, g, b = image[y, x]
            grey_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grey_image[y][x] = [grey_value, grey_value, grey_value]

    plt.imshow(grey_image)
    # Show the plot
    plt.show()
