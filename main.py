import pytesseract
from PIL import Image

image_path = 'a.jpeg'
image = Image.open(image_path)

# text = pytesseract.image_to_string(image)

# Specify the language (Spanish)
custom_config = r'--oem 3 --psm 6 -l spa'
text = pytesseract.image_to_string(image, config=custom_config)


print(text)
