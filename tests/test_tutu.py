from allure_commons.types import Severity
import allure
from pages.authorization_page import authorization_page
from pages.edit_personal_data_page import edit_personal_data_page
from pages.search_avia_tickets_page import search_avia_ticket_page
from pages.query_page import query_page


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
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
    authorization_page.should_have_logout_form()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
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
@allure.label('owner', 'Annette-F')
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
    authorization_page.skip_submit_telephone()
    edit_personal_data_page.open_profile()
    edit_personal_data_page.type_first_name('Maria')
    edit_personal_data_page.type_middle_name('Ivanovna')
    edit_personal_data_page.type_last_name('Petrova')
    edit_personal_data_page.type_phone('1234567890')
    edit_personal_data_page.type_birthday('11.11.1989')
    edit_personal_data_page.confirm_agreement_form()
    edit_personal_data_page.submit_edit_form()
    edit_personal_data_page.check_successful_edit()
    edit_personal_data_page.open_main_page()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search aviatickets')
@allure.story('Page aviatickets')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_avia_ticket():
    authorization_page.open()
    search_avia_ticket_page.type_city_from('Москва')
    search_avia_ticket_page.type_city_to('Сочи')
    search_avia_ticket_page.type_date_from('15.05.2025')
    search_avia_ticket_page.type_date_to('18.05.2025')
    search_avia_ticket_page.count_adult_passengers()
    search_avia_ticket_page.select_class()
    search_avia_ticket_page.submit_selection()
    search_avia_ticket_page.should_be_change_search_button()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search query')
@allure.story('Page query')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_query():
    authorization_page.open()
    query_page.information_table()
    query_page.enter_search_query()
    query_page.check_search_query()
