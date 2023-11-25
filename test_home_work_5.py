import os
from selene import browser, have, be


def test_chek_form(browser_config):
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().should(be.blank).type('Mikhail')
    browser.element('#lastName').click().should(be.blank).type('Sidorkin')
    browser.element('#userEmail').click().should(be.blank).type('slvlimon@gmail.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').click().should(be.blank).type('89099099900')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1995"]')
    browser.element('[class*=day--028]').click()
    browser.element('#subjectsInput').click().should(be.blank).type('Math').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('[type=file]').send_keys(os.path.abspath('res/cat.png'))
    browser.element('#currentAddress').click().should(be.blank).type('Moscow street')
