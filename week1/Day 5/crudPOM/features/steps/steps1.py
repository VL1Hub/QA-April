from behave import *
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@given('el usuario está en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@given('el usuario inicia sesión con "{username}" y "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_credentials(username, password)
    context.login_page.submit()
    context.products_page = ProductsPage(context.driver)

@when('selecciona el producto Sauce Labs Backpack')
def step_impl(context):
    context.products_page.add_to_cart()

@then('el icono del carrito debe mostrar "{num}"')
def step_impl(context, num):
    assert context.products_page.get_cart_badge_text() == num

@given('el producto "{producto}" está en el carrito')
def step_impl(context, producto):
    context.products_page.add_to_cart()
    context.products_page.go_to_cart()
    assert context.cart_page.verify_product_in_cart() == producto

@when('el usuario remueve el producto')
def step_impl(context):
    context.cart_page.remove_product()

@then('el botón debe cambiar a "{texto_boton}"')
def step_impl(context, texto_boton):
    context.cart_page.go_back_to_products()
    assert context.products_page.get_button_text().upper() == texto_boton.upper()

@then('el icono del carrito será "{cero}"')
def step_impl(context, cero):
    assert not context.products_page.get_cart_badge_text() == cero