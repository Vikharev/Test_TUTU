from selene import browser, have
import allure


class ChangeLanguagePage:
    def select_eng_language(self):
        with allure.step('Change the page to English'):
            browser.element('.flag.eng').click()

    def check_change_english_language(self):
        with allure.step('The page is displayed in English'):
            browser.element('#uLoginLink').should(have.text('Sign In'))

    def select_rus_language(self):
        with allure.step('Change the page to Russian'):
            browser.element('.flag.rus').click()

    def check_change_russian_language(self):
        with allure.step('The page is displayed in Russian'):
            browser.element('#uLoginLink').should(have.text('Войти'))


change_language_page = ChangeLanguagePage()
