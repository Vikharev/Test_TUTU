from selene import browser, have
import allure


class EditPersonalData:
    def open_profile(self):
        with allure.step('Open profile page'):
            browser.open('https://www.tutu.ru/user/profile/')

    def type_first_name(self, first_name):
        with allure.step('Fill First name'):
            browser.element('#editDForm_first_name').clear().type(first_name)

    def type_middle_name(self, middle_name):
        with allure.step('Fill Middle name'):
            browser.element('#editDForm_middle_name').clear().type(middle_name)

    def type_last_name(self, last_name):
        with allure.step('Fill Last name'):
            browser.element('#editDForm_last_name').clear().type(last_name)

    def type_phone(self, phone):
        with allure.step('Fill Phone'):
            browser.element('#editDForm_phone').clear().type(phone)

    def type_birthday(self, birthday):
        with allure.step('Fill Birthday'):
            browser.element('#editDForm_birthday').clear().type(birthday).click()

    def confirm_agreement_form(self):
        with allure.step('Check the consent to the processing of personal data'):
            browser.element('#editDForm_agree').click()

    def submit_edit_form(self):
        with allure.step('Submit editing profile'):
            browser.element('#editDForm_submit').click()

    def check_successful_edit(self):
        with allure.step('Сheck for successful saving of changes'):
            browser.element('#editDataMessage').should(have.text('Личные данные сохранены'))

    def open_main_page(self):
        with allure.step('Back to the main page'):
            browser.element('.jUzldXN___logoLink').click()


edit_personal_data_page = EditPersonalData()
