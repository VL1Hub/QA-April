from behave import *
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@given('el usuario está en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('ingresa "{username}" y "{password}" y pulsa el botón')
def step_impl(context, username, password):
    context.login_page.enter_credentials(username, password)
    context.login_page.submit()
    # Redirige a ProductsPage tras el login
    context.products_page = ProductsPage(context.driver)

@then('debe ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert context.products_page.is_title_displayed(mensaje)