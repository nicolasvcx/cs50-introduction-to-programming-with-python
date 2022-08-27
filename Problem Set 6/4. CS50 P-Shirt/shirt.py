import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".jpg"):
    sys.exit("Invalid output")
if not sys.argv[2].endswith(sys.argv[1][(len(sys.argv[1]) - 4): len(sys.argv[1])]):
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    input_image = ImageOps.fit(input_image, size)
    input_image.paste(shirt, shirt)
    input_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")