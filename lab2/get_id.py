import baseclass
import requests
class get_id(baseclass.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = "users.get"
    def _get_data(self, name):

        #method="users.get"

        response = requests.get(get_id.BASE_URL+get_id.method+'?user_ids=' + name).json()
        if('error' in response):
            print('error in user id or smth else, try again')
            raise SystemExit
        return response

    def response_handler(self,response):
        id=response["response"][0]["uid"]
        return id