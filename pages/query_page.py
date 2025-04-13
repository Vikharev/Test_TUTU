from selene import browser, have
import allure


class QueryPage:
    def information_table(self):
        with allure.step('Open information page'):
            browser.element('[href="https://www.tutu.ru/2read/"]').click()

    def enter_search_query(self):
        with allure.step('Enter search query'):
            browser.element('#search').click().type('электронная регистрация').press_enter()

    def check_search_query(self):
        with allure.step('Check search query'):
            browser.element('.title_block').should(have.text('Результат поиска по запросу'))


query_page = QueryPage()
