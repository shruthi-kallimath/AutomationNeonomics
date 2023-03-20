# AutomationNeonomics

**Introduction:**

A quick note on how to download and set up the necessary software to start using Selenium 4 with Python, PyCharm Code Editor with pytest framework dependencies and is intended for Windows operating system.

**Prerequisites:**

1. Python 3.6 or above
2. Pip (Python Package Manager)
3. Chrome/Firefox browser (depending on the browser you want to automate)
4. JDK (Java Development Kit) 8 or above
5. Requests (pip install requests)
 
**Download and install Selenium 4:Gui tests on consent url**

1. Open a command prompt/terminal window
2. Type the following command: pip install selenium==4.0.0
3. Press Enter to download and install Selenium 4

**Download and install PyCharm Code Editor:**

1. Go to https://www.jetbrains.com/pycharm/download/
2. Click on "Download" button for the "Community" version
3. Install the downloaded file by following the prompts

**Installing pytest Framework Dependencies:**

1. Open a command prompt/terminal window
2. Type the following command: pip install pytest
3. Press Enter to download and install pytest framework dependencies

**Download and install WebDriver modules:**

1. Go to the following URLs to download the appropriate driver for your browser:
for an instance,Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
2. Extract the downloaded file to a location on your computer
3. Add the location of the extracted file to your system's PATH environment variable.

**Pytest Framework:**

This Framework is for API testing using Pytest and the POM (Page Object Model) design pattern. 
The framework is designed to be flexible and scalable, so as to make it easy to write and maintain API tests for a different variety of endpoints.
pytest framework has been used to write tests for the web application and the same can be viewed in testCases folder for Authentication,Banks,Accounts.

**Reports Generation:**

Allure reports have been used to generate reports.

**Commands to run the tests:**

1. Open terminal/command prompt 
2. Execute:pytest test_api.py or pytest test_account.py
3. Link to the report generated : **https://frabjous-kitsune-b85c1e.netlify.app**
