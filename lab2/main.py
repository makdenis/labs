import friends
import get_id
import datetime
import matplotlib.pyplot as plt
name=input()
today = datetime.datetime.today()
id =get_id.get_id()
id=id.response_handler(id._get_data(name))
t=friends.friends()
t=t.response_handler(t._get_data(id))
a=[]
for i in t:
    if ('bdate' not in i):
        continue
    if (len(i['bdate']) > 5):
        # print(i)
        d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
        # t=datetime.timedelta(d.day)
        y = int((str((today - d) / 365)[0:2]))

        a.append(y)




plt.hist(
    a, # в зависимости от количества 1,2,3 строится гистограмма
    40 # а это как бы длина оси х
    )
plt.show()