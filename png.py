from PIL import Image
import io

image = Image.open('cat_with_balloon.png')
byte_arr = io.BytesIO()
image.save(byte_arr, format="PNG")

with open('cat_in_cup.jpg', 'ab') as file:
    file.write(byte_arr.getvalue())