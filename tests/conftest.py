import pytest
import MainPkg.base_class as bc


@pytest.fixture(scope='class')
def launch_driver(request):
    _driver = ""
    bc.Browser.collect_data()
    browser = bc.Browser.select_browser()
    match browser:
        case "Chrome":
            _driver = bc.Browser.chrome_driver()
        case "Firefox":
            _driver = bc.Browser.firefox_driver()
    _driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    _driver.maximize_window()
    request.cls.driver = _driver
    yield
    _driver.close()