from selenium import webdriver

def before_scenario(context, scenario):
    # Inicializar Firefox antes de cada escenario
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Cerrar el navegador después de cada escenario
    context.driver.quit()