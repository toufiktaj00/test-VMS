from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver


def pytest_configure(config):
    config._metadata['Project Name']= 'Vat Apex'
    config._metadata['Module Name'] = 'Basic Setup'
    config._metadata['Tester'] = 'Toufik'

#pytest -v -s -n=2 --html=Reports\report.html
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

