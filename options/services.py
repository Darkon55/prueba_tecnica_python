import requests

from options.models import Endpoint


class EdnpointService:

    def __init__(self, table_name): 
        self.table_name = table_name

    def post_login(self, params):
        try:
            auth_data = {'usuario': params.username, 'contrasena': params.password}
            resp = requests.post(params.url, json=auth_data)

            return resp
        except Exception as ex:
            raise Exception(ex)