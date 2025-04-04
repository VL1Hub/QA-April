Feature: Gestión del Carrito en SauceDemo

  Background:
    Given el usuario está en la página de login
    And el usuario inicia sesión con "standard_user" y "secret_sauce"

  Scenario: Añadir un producto al carrito
    When selecciona el producto Sauce Labs Backpack
    Then el icono del carrito debe mostrar "1"

  Scenario: Remover un producto del carrito
    Given el producto "Sauce Labs Backpack" está en el carrito
    When el usuario remueve el producto
    Then el botón debe cambiar a "Add to cart"
    And el icono del carrito será "0"