from selene import browser, have, by
import allure


class SearchAviaTickets:
    def choice_city_from(self):
        with allure.step('Select the city from'):
            browser.element('[data-ti="fromHint"]').click()

    def choice_city_to(self):
        with allure.step('Select the city to'):
            browser.element('[data-ti="toHint"]').click()

    def choice_date_from(self):
        with allure.step('Select the departure date'):
            browser.element("//button[contains(text(), 'Сегодня')]").click()

    def choice_date_to(self):
        with allure.step('Select the date of the return ticket'):
            browser.element("//button[contains(text(), 'Послезавтра')]").click()

    def submit_selection(self):
        with allure.step('Submit selection'):
            browser.element('[data-ti="submit-button"]').click()

    def should_be_change_search_button(self):
        with allure.step('Check search result'):
            browser.element('[data-ti="icon"]').should(have.text('Изменить'))


search_avia_ticket_page = SearchAviaTickets()
