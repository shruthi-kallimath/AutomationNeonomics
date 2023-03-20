from pageObjects.Authentication import AuthPage
from selenium import webdriver
import pytest
from Configurations import *
from testCases import *
from Utilities.readProperties import ReadConfig
from pageObjects.Banks import BanksPage
from pageObjects.Accounts import AccountsPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture(scope='session')
def token_url():
    return "https://sandbox.neonomics.io/auth/realms/sandbox/protocol/openid-connect/token"


@pytest.fixture(scope='session')
def base_url():
    return 'https://sandbox.neonomics.io/ics/v3'


@pytest.fixture(scope='session')
def access_token():
    read = ReadConfig()
    auth_page = AuthPage()
    response = auth_page.generate_access_code(read.get_grant_type(), read.get_client_id(), read.get_client_secret())
    return response[0]['access_token']

@pytest.fixture(scope='session')
def justo_bankid(access_token):
    read = ReadConfig()
    Banks = BanksPage()
    bank_response = Banks.get_banks(access_token,read.get_accept(), read.get_x_device_id())
    for record in bank_response[0]:
        if record['bic'] == 'JUSTNOKK':
            return record['id']

@pytest.fixture(scope='session')
def session_id(access_token, justo_bankid):
    read = ReadConfig()
    session = BanksPage.gen_session(access_token, read.get_x_device_id(), read.get_session_content_type(), justo_bankid)
    assert session[1] == 201
    return session[0]['sessionId']


@pytest.fixture(scope='session')
def account_id(access_token, justo_bankid,):
    read = ReadConfig()
    account = AccountsPage.get_accounts(access_token, read.get_x_device_id(), read.get_session_content_type(), justo_bankid)
    assert account[1] == 200
    return account[0][0]['id']








