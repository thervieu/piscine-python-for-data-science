import matplotlib.pyplot as plt
from load_image import ft_load

def zoom():
    img = ft_load('animal.jpeg')
    print(img)
    x, y, width, height = 450, 140, 400, 400
    zoomed_img = img[y:y+height, x:x+width]
    print(f'New shape after slicing: {zoomed_img.shape}')
    print(zoomed_img)
    plt.imshow(zoomed_img)
    plt.show()


if __name__=="__main__":
    zoom()