from PIL import Image

def image_to_ascii(image_path, width=50):
    img = Image.open(image_path)
    img = img.resize((width, int(width * img.height / img.width)))
    img = img.convert('L')
    pixels = img.getdata()
    chars = "@%#*+=-:. "
    ascii_str = ''.join([chars[pixel//32] for pixel in pixels])
    ascii_str_len = len(ascii_str)
    img_ascii = "\n".join([ascii_str[index:index+width] for index in range(0, ascii_str_len, width)])
    print(img_ascii)

image_to_ascii("python.png")
