from PIL import Image



def resize_image(image_path, resized_path):
    with Image.open(image_path) as img:
        img.thumbnail(tuple(x / 2 for x in img.size))
        img.save(resized_path)

