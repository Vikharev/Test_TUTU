from selene import browser, have, by
import allure


class SearchAviaTickets:
    def type_city_from(self, city_from):
        with allure.step('Select the city from'):
            browser.element('input').by_their(by.text('Откуда')).type(city_from).press_enter()

    def type_city_to(self, city_to):
        with allure.step('Select the city to'):
            browser.element(by.text('Куда')).type(city_to).press_enter()

    def type_date_from(self, date_from):
        with allure.step('Select the departure date'):
            browser.element('[data-ti="trip-dates"]').type(date_from).press_enter()

    def type_date_to(self, date_to):
        with allure.step('Select the date of the return ticket'):
            browser.element('[data-ti="trip-second-date"]').type(date_to).press_enter()

    def submit_selection(self):
        with allure.step('Submit selection'):
            browser.element('[data-ti="submit-button"]').click()

    def should_be_change_search_button(self):
        with allure.step('Check search result'):
            browser.element('[data-ti="icon"]').should(have.text('Изменить'))


search_avia_ticket_page = SearchAviaTickets()
