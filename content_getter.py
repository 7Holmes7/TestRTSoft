from flask import current_app
from typing import Optional
from random import choice

COUNT_SHOW_MSG = 10


class ContentGetter:
    """
    Класс для получения контента
    """
    def __init__(self):
        self.msg = None
        self._suited_count = 0

    def get_by_categories(self, categories: list) -> Optional[str]:
        """
        Метод для получения картинки по категории
        """
        suited_images = []
        for image, image_info in current_app.content_dict.items():
            if image_info['show_count'] == 0:
                continue

            if set(image_info['categories']) & set(categories):
                suited_images.append(image)
                self._suited_count += image_info['show_count']

        if not suited_images:
            return None

        if self._suited_count < COUNT_SHOW_MSG:
            self.msg = 'There are few pictures left in such categories. Try others!'

        return self._get_image(suited_images)

    @staticmethod
    def _get_image(images: list) -> str:
        """
        Метод для получения картинки(возможно добавление поведения)
        """
        res_image = choice(images)
        current_app.content_dict[res_image]['show_count'] -= 1
        print(current_app.content_dict[res_image]['show_count'])
        return res_image
