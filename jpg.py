# with open('cat_in_cup.jpg', 'ab') as image:
#     image.write(b"Hello from DarishkaAMS")


with open('cat_in_cup.jpg', 'rb') as image:
    content = image.read()
    offset = content.index(bytes.fromhex('FFD9'))
    image.seek(offset + 2)
    print(image.read())

