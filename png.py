from PIL import Image
import io

# Add PNG into JPG file
# image = Image.open('cat_with_balloon.png')
# byte_arr = io.BytesIO()
# image.save(byte_arr, format="PNG")
#
# with open('cat_in_cup.jpg', 'ab') as file:
#     file.write(byte_arr.getvalue())

# Subtract PNG from JPG file
with open('cat_in_cup.jpg', 'rb') as test_image:
    content = test_image.read()
    offset = content.index(bytes.fromhex('FFD9'))
    test_image.seek(offset + 2)

    new_image = Image.open(io.BytesIO(test_image.read()))
    new_image.save("new_Test_image.png")

