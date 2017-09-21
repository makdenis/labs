import baseclass
import requests
class get_id(baseclass.BaseClient):
    def _get_data(self,method):

        #method="users.get"
        name = input()
        response = requests.get('https://api.vk.com/method/'+method+'?user_ids=' + name).json()
        return response

    def getid(self,response):
        id=response["response"][0]["uid"]
        return id