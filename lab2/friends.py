import baseclass
import get_id
import requests
import datetime
import matplotlib.pyplot as plt
today = datetime.datetime.today()
class friends(baseclass.BaseClient):
    def response_handler(self, id):
        t = requests.get('https://api.vk.com/method/friends.get?user_id=' + str(id) + '&fields=bdate&v=5.62').json()
        return t
    def getfriends(self, t,a):
        for i in t["response"]['items']:
            if ('bdate' not in i):
                continue
            if (len(i['bdate']) > 5):
                # print(i)
                d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
                # t=datetime.timedelta(d.day)
                y = int((str((today - d) / 365)[0:2]))


                a.append(y)
        return a


