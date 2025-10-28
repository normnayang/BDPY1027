from urllib.request import urlopen
from PIL import Image

URL = "https://www.python.org/static/img/python-logo.png"
fileToSave = urlopen(URL)
originalImage = Image.open(fileToSave)
originalImage.save("images/logo.png")
halfSize = (originalImage.size[0]//2,originalImage.size[1]//2)
print(halfSize)
halfImage=originalImage.resize(halfSize)
halfImage.save("images/half_logo.png")
r90 = originalImage.transpose(Image.ROTATE_90)
r90.save("images/r90.png")

r180 = originalImage.transpose(Image.ROTATE_180)
r180.save("images/r180.png")