from PIL import ImageFont


class FontLoader:
    @staticmethod
    def load_custom_font(font_path, size):
        font = ImageFont.truetype(font_path, size=size)
        font_family = font.getname()[0]

        return font_family, size
