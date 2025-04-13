from selene import browser, have
import allure


class SearchAviaTickets:
    def type_city_from(self, city_from):
        with allure.step('Select the city from'):
            browser.element('[name="city_from"]').type(city_from).press_enter()

    def type_city_to(self, city_to):
        with allure.step('Select the city to'):
            browser.element('[name="city_to"]').type(city_to).press_enter()

    def type_date_from(self, date_from):
        with allure.step('Select the departure date'):
            browser.element('[name="date_from"]').type(date_from).press_enter()

    def type_date_to(self, date_to):
        with allure.step('Select the date of the return ticket'):
            browser.element('[name="date_back"]').type(date_to)

    def count_adult_passengers(self):
        with allure.step('Select the number of adult passengers'):
            browser.element('.counter_adult_wrp').element('[class="increase"]').click()

    def select_class(self):
        with allure.step('Select class'):
            browser.element('.j-dropdown').click()
            browser.element('[data-value="C"]').click()

    def submit_selection(self):
        with allure.step('Submit selection'):
            browser.element('.button_wrp.j-buttons_block').click()

    def should_be_change_search_button(self):
        with allure.step('Check search result'):
            browser.element('[data-ti="icon"]').should(have.text('Изменить'))


search_avia_ticket_page = SearchAviaTickets()
