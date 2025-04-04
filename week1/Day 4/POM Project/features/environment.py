from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
