# Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token


server1 = Server(vk_api_token, 172998024, "server1")
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера

server1.test()

def start(self):
        for event in self.long_poll.listen():
            print(event)
server1.start()
