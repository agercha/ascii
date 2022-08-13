import sys
from PIL import Image, ImageOps, ImageEnhance

def print_pix(x):
    if x < 32:
        return(" ")
    elif x < 64:
        return(".")
    elif x < 96:
        return("-")
    elif x < 128:
        return("~")
    elif x < 160:
        return("*")
    elif x < 192:
        return("o")
    elif x < 224:
        return("O")
    else:
        return("#")

if __name__ == '__main__':
    try:
        img_file_name = sys.argv[1]
        new_w = int(sys.argv[2])
        contrast_factor = float(sys.argv[3])
        img = Image.open(img_file_name)
        (w, h) = img.size
        factor = 2.15 if new_w < 400 else 2.75
        new_h = int((new_w * h) / (w  * factor))
        img = img.resize((new_w, new_h))
        img = ImageOps.grayscale(img)
        img = (ImageEnhance.Contrast(img)).enhance(contrast_factor)
        for row in range(new_h):
            current_row = ""
            for col in range(new_w):
                new_px_original = (img.getpixel((col, row)))
                new_px_toprint = print_pix(new_px_original)
                current_row += new_px_toprint
            print(current_row)
    except:
        print("Sorry, this image doesn't exist!")
