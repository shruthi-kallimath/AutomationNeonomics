import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\shivc\\PycharmProjects\\pythonProject3\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        URL = config.get('urls','base_url')
        return URL

    @staticmethod
    def get_session_url():
        session_url = config.get('urls', 'session_url')
        return session_url

    @staticmethod
    def get_access_token_url():
        accesstokenurl = config.get('urls', 'access_token_url')
        return accesstokenurl

    @staticmethod
    def get_accounts_url():
        accounts_url = config.get('urls', 'accounts_url')
        return accounts_url

    @staticmethod
    def get_banks_url():
        banks_url = config.get('urls', 'banks_url')
        return banks_url

    @staticmethod
    def get_username():
        username = config.get('credentials','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('credentials','password')
        return password

    @staticmethod
    def get_client_id():
        clientid =config.get('client id secrets','client_id')
        return clientid

    @staticmethod
    def get_client_secret():
        secretid = config.get('client id secrets', 'client_secret')
        return secretid

    @staticmethod
    def get_invalid_client_id():
        clientid = config.get('client id secrets', 'invalid_client_id')
        return clientid

    @staticmethod
    def get_invalid_client_secret():
        secretid = config.get('client id secrets', 'invalid_client_secret')
        return secretid

    @staticmethod
    def get_content_type():
        content_type = config.get('rest api headers', 'content_type')
        return content_type

    @staticmethod
    def get_grant_type():
        granttype = config.get('rest api headers', 'grant_type')
        return granttype

    @staticmethod
    def get_accept():
        accept = config.get('rest api headers', 'accept')
        return accept

    @staticmethod
    def get_session_content_type():
        session_content_type = config.get('rest api headers', 'session_content_type')
        return session_content_type

    @staticmethod
    def get_x_psu_ip_address():
        x_psu_ip_address = config.get('generic', 'x-psu-ip-address')
        return x_psu_ip_address

    @staticmethod
    def get_x_device_id():
        x_device_id = config.get('generic', 'x-device-id')
        return x_device_id





