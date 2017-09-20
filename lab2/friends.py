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
id =get_id.get_id.getid(get_id.get_id._get_data('users.get'))
t=friends.response_handler(id)
a=[]
friends.getfriends(t,a)

plt.hist(
    a, # в зависимости от количества 1,2,3 строится гистограмма
    40 # а это как бы длина оси х
    )
plt.show()
