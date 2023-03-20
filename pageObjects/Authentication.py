import requests
from Utilities.readProperties import ReadConfig

class AuthPage:

        def generate_access_code(self,grant_type,client_id,client_secret):

            headers = {'Content-Type' : ReadConfig.get_content_type()}
            body = {'grant_type': grant_type, 'client_id': client_id,
                'client_secret': client_secret}

            response = requests.post(ReadConfig.get_access_token_url(),
                                 headers=headers, data=body)

            return response.json(),response.status_code

        def generate_consent_url(self,access_token,accept,x_device_id,x_psu_ip_address,url):

            headers = {'Authorization': f'Bearer ' + access_token ,'Accept': accept,'x-device-id': x_device_id,'x-psu-ip-address':x_psu_ip_address}   ##ReadConfig.get_authorization()

            response = requests.get(url,
                                 headers=headers)

            return response.json(),response.status_code









































#class AuthenticationPage:
    #def __init__(self, url):
     #   self.url = url

    #def get_token(self, content_type, grant_type, client_id, client_secret):
     #   response = requests.post(self.url, headers={'Content-Type': content_type},data ={'grant_type': grant_type, 'client_id': client_id, 'client_secret': client_secret})
      #  return response.status_code,response.json()

  #  def create_session(self, access_token, device_id, content_type, bank_id):
   #     response = requests.post(f'{self.url}/session', headers={'Content-Type': content_type, 'Authorization': 'Bearer ' + access_token, 'x-device-id': device_id},payload ={'bankId': bank_id})
    #    return response.status_code,response.json()
