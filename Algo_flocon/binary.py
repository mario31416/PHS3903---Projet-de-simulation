
from PIL import Image

#read the image from path
image = Image.open(r'C:\Users\Florentin\PHS3903-Projet-de-simulation\figure_11_griffeath_kappa=0.0075.png')

#Convert it into the grayscale image
grayscale = image.convert('L')

#Converting the same image to black and white mode
BW= image.convert('1')

#save both the images
grayscale.save("grayscale_image.jpg")

