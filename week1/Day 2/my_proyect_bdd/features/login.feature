Feature: Login de usuario
  Scenario: Login exitoso
    Given el usuario está en la página de login
    When ingresa "standard_user" y "secret_sauce"
    Then debe ver el mensaje "Products"