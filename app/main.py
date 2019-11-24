import vk_api
import config.config as cfg

import threading

try:
    import thread
except ImportError:
    import _thread as thread
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token=cfg.VK_AUTH_TOKER)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

if __name__ == "__main__":
    from photo_api import PhotoAPI
    from bots.bot_main import BotVK

    bot = BotVK(vk, longpoll)
    bot.start()
    # server_thread = Thread(target=server_run)
    # server_thread.start()
    # with open('test/vcru.png', 'rb') as f:
    #     with open('test.png', 'wb') as d:
    #         d.write(f.read())
        # PhotoAPI.add_photo_in_album()
