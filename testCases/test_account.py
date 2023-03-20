import requests
import pytest
from testCases.conftest import *
from Configurations import *
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from pageObjects.Accounts import AccountsPage
from testCases.test_Signin import Test_Signin
from pageObjects.Authentication import AuthPage
from testCases.conftest import *
from allure_commons.types import AttachmentType


class TestAccounts:

    def test_get_accounts(self,access_token,session_id):
        auth_page = AuthPage()
        read = ReadConfig()
        signin = Test_Signin()
        account_response = AccountsPage.get_accounts(access_token,read.get_accept(),read.get_x_device_id(),read.get_x_psu_ip_address(),session_id)
        assert account_response[1] == 510
        assert account_response[0]['errorCode'] == "1426", f"Expected {'1426'}, but got {account_response[0]['errorCode']}."

        if account_response[1] == 510 and account_response[0]['errorCode'] == "1426":
            for record in account_response[0]['links']:
                if record['rel'] == 'consent':
                    consent_url = record['href']

        print(consent_url)

        consent_response = auth_page.generate_consent_url(access_token,read.get_accept(),read.get_x_device_id(),read.get_x_psu_ip_address(),consent_url)

        consent_response[1] == 200

        for record in consent_response[0]['links']:
                if record['rel'] == 'consent':
                    bank_consent_url = record['href']

        print(bank_consent_url)

        consent_login_response = signin.test_login(bank_consent_url)

        assert 'You have successfully granted consent to JUSTNOKK' in consent_login_response

        account_response = AccountsPage.get_accounts(access_token,read.get_accept(),read.get_x_device_id(),read.get_x_psu_ip_address(),session_id)

        print(account_response)
        assert account_response[0][0]['accountName'] == read.get_username()
        account_id = account_response[0][0]['id']
        print(account_id)

    def test_get_transactions(self,access_token,session_id,account_id):







































