from PIL import Image


class ImageResizer:
    @staticmethod
    def resize_and_crop(image, target_size):
        image_ratio = image.width / image.height
        target_ratio = target_size[0] / target_size[1]

        if image_ratio > target_ratio:
            new_width = int(target_size[1] * image_ratio)
            image = image.resize((new_width, target_size[1]), Image.Resampling.LANCZOS)
            left = (new_width - target_size[0]) / 2
            image = image.crop((left, 0, left + target_size[0], target_size[1]))
        else:
            new_height = int(target_size[0] / image_ratio)
            image = image.resize((target_size[0], new_height), Image.Resampling.LANCZOS)
            top = (new_height - target_size[1]) / 2
            image = image.crop((0, top, target_size[0], top + target_size[1]))

        return image