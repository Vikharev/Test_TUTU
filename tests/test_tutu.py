import pytest
from allure_commons.types import Severity
import allure
from pages.authorization_page import authorization_page
from pages.edit_personal_data_page import edit_personal_data_page
from pages.search_avia_tickets_page import search_avia_ticket_page
from pages.query_page import query_page


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Authorization with valid login and password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_valid_authorization():
    authorization_page.open()
    authorization_page.open_authorization_page()
    authorization_page.select_password_auth()
    authorization_page.fill_email()
    authorization_page.fill_password()
    authorization_page.submit_authorization()
    authorization_page.skip_submit_telephone()
    authorization_page.should_have_person_circle()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Authorization with wrong password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_authorization_with_wrong_password():
    authorization_page.open()
    authorization_page.open_authorization_page()
    authorization_page.select_password_auth()
    authorization_page.fill_email()
    authorization_page.fill_wrong_password()
    authorization_page.submit_authorization()
    authorization_page.should_have_text('Неверный адрес почты или пароль.')


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.feature('Edit profile')
@allure.story('Profile')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_edit_personal_data():
    authorization_page.open()
    authorization_page.open_authorization_page()
    authorization_page.select_password_auth()
    authorization_page.fill_email()
    authorization_page.fill_password()
    authorization_page.submit_authorization()
    edit_personal_data_page.open_profile()
    edit_personal_data_page.edit_mode_on()
    edit_personal_data_page.type_first_name('Иван')
    edit_personal_data_page.type_middle_name('Иванович')
    edit_personal_data_page.type_last_name('Иванов')
    edit_personal_data_page.type_phone('1234567890')
    edit_personal_data_page.type_birthday('11.11.1989')
    edit_personal_data_page.confirm_agreement_form()
    edit_personal_data_page.submit_edit_form()
    edit_personal_data_page.check_successful_edit()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Search aviatickets')
@allure.story('Page aviatickets')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_avia_ticket():
    authorization_page.open()
    search_avia_ticket_page.choice_city_from()
    search_avia_ticket_page.choice_city_to()
    search_avia_ticket_page.choice_date_from()
    search_avia_ticket_page.choice_date_to()
    search_avia_ticket_page.submit_selection()
    search_avia_ticket_page.should_be_change_search_button()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.feature('Search query')
@allure.story('Page query')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_query():
    authorization_page.open()
    query_page.information_table()
    query_page.enter_search_query()
    query_page.check_search_query()
