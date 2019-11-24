import config as cfg
import requests

class PhotoAPI:
    """
    Класс для работы с фотографиями в ВК
    """

    @staticmethod
    def create_album(**kwargs):
        pass

    @staticmethod
    def get_all_photos_by_album(**kwargs):
        pass

    @staticmethod
    def get_photo_by_url(**kwargs):
        pass

    @staticmethod
    def add_photo_in_album(**kwargs):
        pass

    @staticmethod
    def get_url_for_add(**kwargs):
        json = {
            'album_id': kwargs.get('album_id'),
            'group_id': kwargs.get('group_id'),
            'v': cfg.VK_API_VERSION
        }

