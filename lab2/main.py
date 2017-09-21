import friends
import get_id

import matplotlib.pyplot as plt
id =get_id.get_id()
id=id.getid(id._get_data("users.get"))
t=friends.friends()
t=t.response_handler(id)
a=[]
j=friends.friends()
j.getfriends(t,a)

plt.hist(
    a, # в зависимости от количества 1,2,3 строится гистограмма
    40 # а это как бы длина оси х
    )
plt.show()