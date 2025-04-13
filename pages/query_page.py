from selene import browser, have
import allure


class QueryPage:
    def information_table(self):
        with allure.step('Open information page'):
            browser.element('[href="/2read/poezda/main/"]').click()

    def enter_search_query(self):
        with allure.step('Enter search query'):
            browser.element('#search').click().type('как получить визу').press_enter()

    def check_search_query(self):
        with allure.step('Check search query'):
            browser.element('.title_block').should(have.text('Результат поиска по запросу'))


query_page = QueryPage()
