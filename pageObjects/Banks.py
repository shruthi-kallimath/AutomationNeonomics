import requests
from Utilities.readProperties import ReadConfig
from testCases.conftest import *

class BanksPage:

    def get_banks(self,access_token,accept,x_device_id):

        headers = {'Authorization': f'Bearer ' + access_token ,'Accept': accept,'x-device-id': x_device_id}   ##ReadConfig.get_authorization()


        bank_response = requests.get(ReadConfig.get_banks_url(),
                                 headers=headers)

        return bank_response.json(), bank_response.status_code

    #{f'Bearer' + 'Access_Token'}

    def gen_session(access_token,x_device_id,session_content_type,justo_bankid):

        headers = {'Authorization': f'Bearer ' + access_token ,'x-device-id':x_device_id,'session_content_type' :session_content_type}
        body = {"bankId" : justo_bankid}

        response = requests.post(ReadConfig.get_session_url(),headers = headers,json = body)

        return response.json(),response.status_code