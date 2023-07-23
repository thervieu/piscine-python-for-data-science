import os
import filetype
import numpy as np
from PIL import Image

def ft_load(path: str): # (you can return to the desired format)
    if os.path.isfile(path) is False:
        raise ValueError(f"{path} does not exist or is not a file")
    if (filetype.guess(path) is None
        or (filetype.guess(path).extension != 'jpg' and filetype.guess(path).extension != 'jpeg')):
        raise ValueError(f"{path} is not a jpg or jpeg image")
    
    image = np.asarray(Image.open(path))

    return image
