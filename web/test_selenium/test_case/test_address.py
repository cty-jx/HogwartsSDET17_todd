from web.test_selenium.login_page.main_page import MainPage


class TestAddress:
    def test_add_member(self):
        main = MainPage()
        main.goto_address().add_member()