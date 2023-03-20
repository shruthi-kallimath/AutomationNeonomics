import requests
from selenium import webdriver
import pytest
from testCases.conftest import *
from Configurations import *
from pageObjects.Authentication import AuthPage
from testCases import *
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from pageObjects.Banks import BanksPage
import allure
from allure_commons.types import AttachmentType


@allure.severity(allure.severity_level.CRITICAL)
class TestAccessCode:

        logger = LogGen.loggen()

        def test_access_code_generation(self):
            self.logger.info("Generation of Access Code")
            read = ReadConfig()
            auth_page = AuthPage()
            response = auth_page.generate_access_code(read.get_grant_type(),read.get_client_id(),read.get_client_secret())

            # Check that access code is generated successfully
            assert response[1] == 200
            Access_Token = response[0]['access_token']
            print(Access_Token)
            self.logger.info("Generation of Access Code is passed")

        def test_invalid_access_code_generation(self):
            read = ReadConfig()
            auth_page = AuthPage()
            response = auth_page.generate_access_code(read.get_grant_type(),read.get_invalid_client_id(),read.get_invalid_client_secret())

            # Check that access code is generated successfully
            assert response[1] == 510
            assert response[0]['error'] == "invalid_client"
            assert response[0]['error_description'] == "Invalid client credentials"


        def test_get_bankid(self,access_token):
            read = ReadConfig()
            Banks = BanksPage()
            bank_response = Banks.get_banks(access_token,read.get_accept(),read.get_x_device_id())
            assert bank_response[1] == 200

            for record in bank_response[0]:
                if record['bic'] == 'JUSTNOKK':
                    assert record['bankDisplayName'] == "Justo Bank"
                    justnok_bankid = record['id']

            print(justnok_bankid)

        def test_generate_session(self,access_token,justo_bankid):
            read = ReadConfig()
            session = BanksPage.gen_session(access_token,read.get_x_device_id(),read.get_session_content_type(),justo_bankid)
            assert session[1] == 201
            session_id = session[0]['sessionId']
            print(session_id)
            assert 'sessionId' in session[0]

























