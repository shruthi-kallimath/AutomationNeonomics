import requests
from Utilities.readProperties import ReadConfig
from testCases.conftest import *

class AccountsPage:

    def get_accounts(access_token,accept,x_device_id,x_psu_ip_address,x_session_id):

        headers = {'Authorization': f'Bearer ' + access_token ,'Accept': accept,'x-device-id': x_device_id,'x-psu-ip-address':x_psu_ip_address,'x-session-id' : x_session_id}


        account_response = requests.get(ReadConfig.get_accounts_url(),
                                 headers=headers)

        return account_response.json(),  account_response.status_code



    def get_transactions(access_token,accept,x_device_id,x_psu_ip_address,x_session_id):


        headers = {'Authorization': f'Bearer ' + access_token, 'Accept': accept, 'x-device-id': x_device_id,
                   'x-psu-ip-address': x_psu_ip_address, 'x-session-id': x_session_id}

        transaction_response = requests.get(ReadConfig.get_accounts_url(),
                                        headers=headers)

        return transaction_response.json(), transaction_response.status_code


#https: // sandbox.neonomics.io / ics / v3 / accounts / < ACCOUNT_ID > / transactions