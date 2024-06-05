import os.path
import tkinter.font as TkFont
from PIL import ImageFont
import customtkinter as ctk

from config import FONT_LOCATION

DEFAULT_FONT_PATH = os.path.join(FONT_LOCATION, 'DOSMyungjo.ttf')


class GlobalFont:
    @staticmethod
    def get_font(font_path=DEFAULT_FONT_PATH, font_size=18):
        font = ImageFont.truetype(font_path, size=font_size)
        font_family = font.getname()[0]

        return font_family, font_size

    @staticmethod
    def get_global_font(font_path=DEFAULT_FONT_PATH, font_size=18, use_type='tk'):
        font_family, size = GlobalFont.get_font(font_path, font_size)

        if use_type == 'tk':
            default_font = TkFont.Font(family=font_family, size=font_size)
        else:
            default_font = ctk.CTkFont(family=font_family, size=font_size)

        return default_font
