import requests
import vk_api

vk_session = vk_api.VkApi(token='418514b94a29ddbc7bf4eaba617a8cb857298d1ddc1dbb319b05bd0d5b2bcf2441cf3bca96aa7001ff99e')
from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # Слушаем longpoll, если пришло сообщение то:
        vk.messages.send(  # Отправляем сообщение
            user_id=event.user_id,
            random_id=event.random_id,
            message='sam xuy'
        )
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':  # Если написали заданную фразу
            if event.from_user:  # Если написали в ЛС
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Ваш текст'
                )
            elif event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id=event.random_id,
                    message='Ваш текст'
                )
