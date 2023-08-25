import pytest

import Pages.loginPage as ln
import MainPkg.base_class as bc


@pytest.mark.usefixtures("launch_driver")
class TestLoginLogout:
    def test_invalid_login(self):
        self.lgn = ln.LoginPages(self.driver)
        print(bc.Browser.data)
        username = bc.Browser.fetch_data('InValid', 'Username')
        password = bc.Browser.fetch_data('InValid', 'Password')
        result = self.lgn.login(username, password)
        if result:
            print("Successful login; valid credentials")
            self.lgn.logout()
        else:
            print("Unsuccessful Login")
        assert result == False

    def test_login(self):
        self.lgn = ln.LoginPages(self.driver)
        username = bc.Browser.fetch_data('Valid', 'Username')
        password = bc.Browser.fetch_data('Valid', 'Password')
        result = self.lgn.login(username, password)
        assert result == True
        if result:
            print("Successful Login")
            r2 = self.lgn.logout()
            if r2:
                print("Successful Logout")
        else:
            print("Unsuccessful Login")

