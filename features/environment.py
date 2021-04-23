from selenium import webdriver
 
def before_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser = webdriver.Chrome('C:/chromedriver.exe') 
    context.browser.implicitly_wait(10)
 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()