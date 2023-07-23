import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def transpose_matrix(matrix):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Input matrix should have uniform row lengths")

    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new empty matrix with swapped dimensions
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix


def zoom():
    img = ft_load('animal.jpeg')

    x, y, width, height = 450, 140, 400, 400
    zoomed_img = img[y:y+height, x:x+width]
    print(f'The shape of the image is {zoomed_img.shape}')
    print(zoomed_img)

    # Rotate the zoomed-in image
    rotated_zoomed_img = transpose_matrix(zoomed_img)
    print(f'New shape after rotation: {rotated_zoomed_img.shape}')
    print(rotated_zoomed_img)

    plt.imshow(rotated_zoomed_img)
    plt.title(f'Rotated Image (90 degrees)')
    plt.show()


if __name__=="__main__":
    zoom()