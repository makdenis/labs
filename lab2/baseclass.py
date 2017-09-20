import requests
import datetime
class BaseClient:
    # URL vk api
    BASE_URL = None
    # метод vk api
    method = None
    # GET, POST, ...
    http_method = None

    # Получение GET параметров запроса
    def get_params(self):
        return None

    # Получение данных POST запроса
    def get_json(self):
        return None

    # Получение HTTP заголовков
    def get_headers(self):
        return None

    # Склейка url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = None
        r = requests.get('https://api.vk.com/method/users.get?user_ids=210700286 ')
        # todo выполнить запрос

        return r
            #self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )
#3e9b9487ad01869302822ad9352cfb578c3d99b4c6ee3d76062ed163b68d546ef0363d1988da134787455
name=input()
idd=requests.get('https://api.vk.com/method/users.get?user_ids='+name).json()["response"][0]["uid"]


#print(requests.get('https://api.vk.com/method/friends.get?user_id=210700286').text)
t=requests.get('https://api.vk.com/method/friends.get?user_id='+str(idd)+'&fields=bdate&v=5.62').json()
print(t)
print(len(t["response"]['items']))
i=0
for i in t["response"]['items']:
    if('bdate' not in i):
        continue
    if (len(i['bdate'])>5):
        print(i['bdate'][-4::1])

today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1