import requests

import config.config as cfg
from vk_api.longpoll import VkLongPoll, VkEventType
from photo_api import PhotoAPI
import threading

class BotVK(threading.Thread):
    def __init__(self,vk, longpoll):
        threading.Thread.__init__(self)
        self.vk = vk
        self.longpoll = longpoll

    def run(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                # Слушаем longpoll, если пришло сообщение то:
                self.vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='sam xuy'
                )
                if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':  # Если написали заданную фразу
                    if event.from_user:  # Если написали в ЛС
                        self.vk.messages.send(  # Отправляем сообщение
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message='Ваш текст'
                        )
                    elif event.from_chat:  # Если написали в Беседе
                        self.vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=event.random_id,
                            message='Ваш текст'
                        )
