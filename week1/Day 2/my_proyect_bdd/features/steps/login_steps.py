from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('el usuario está en la página de login')
def step_impl(context):
        browser = webdriver.Firefox()
        browser.implicitly_wait(5)
        context.driver = browser
        context.driver.get('https://www.saucedemo.com/')
        context.driver.get('https://www.saucedemo.com/')

@when('ingresa "{username}" y "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then('debe ver el mensaje "{mensaje}"')
def step_impl(context,mensaje):
    assert mensaje in context.driver.find_element(By.CLASS_NAME, "title").text
    context.driver.quit()

