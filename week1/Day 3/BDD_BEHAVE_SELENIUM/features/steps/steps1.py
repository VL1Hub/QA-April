from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('el usuario está en la página de login')
def step_impl(context):
    context.driver.get('https://www.saucedemo.com/')


@given('el usuario inicia sesión con "{username}" y "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()


@when('selecciona el producto Sauce Labs Backpack')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()


@then('el icono del carrito debe mostrar "{num}"')
def step_impl(context, num):
    badge = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == num


@given('el producto "{producto}" está en el carrito')
def step_impl(context, producto):
    # Verificar que el producto está añadido desde la página principal
    if len(context.driver.find_elements(By.ID, "remove-sauce-labs-backpack")) == 0:
        context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Ir al carrito
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verificar producto en carrito
    item = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item_name"))
    )
    assert item.text == producto


@when('el usuario remueve el producto')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    ).click()


@then('el botón debe cambiar a "{texto_boton}"')
def step_impl(context, texto_boton):
    # Volver a la página de productos para ver el botón
    context.driver.find_element(By.ID, "continue-shopping").click()

    btn = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    assert btn.text.upper() == texto_boton.upper()


@then('el icono del carrito será "{cero}"')
def step_impl(context, cero):
    # Opción 1: Verificar que no existe ningún badge
    badges = context.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert not badges, f"Se encontraron {len(badges)} badges cuando se esperaba 0"
