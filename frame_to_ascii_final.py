from PIL import Image, ImageDraw

Color = "MNHQ$OC?7>!:-;. "
top_left = (0, 0)
dark = (0, 0, 0)


def brightness(pixel):
    r, g, b = pixel
    brightness_scale = int(0.21 * r + 0.72 * g + 0.07 * b)
    return brightness_scale


def img_to_ascii(img):
    ori_width, ori_height = img.size
    img = img.resize((ori_width // 5, ori_height // 10))
    width, height = img.size
    ascii_text = ""
    pix = img.load()
    out = Image.new("RGB", (ori_width, ori_height), (255, 255, 255))
    d = ImageDraw.Draw(out)
    for h in range(height):
        for w in range(width):
            index_in_color = brightness(pix[w, h])
            ascii_text += Color[int(index_in_color / 16)]

        ascii_text += '\n'
    d.multiline_text(top_left, ascii_text, fill=dark, spacing=0, align="center")
    return out
