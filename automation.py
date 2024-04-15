from time import sleep
import playwright

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page(base_url='https://selenium.dunossauro.live/')

    page.goto('todo_list.html')

    page.locator('#todo-name').fill('Fazer Live #222')
    page.locator('#todo-desc').fill('Live de PW')
    page.locator('#todo-submit').click()
    sleep(2)
    page.locator('button.do').click()
    sleep(2)
    page.locator('button.do').click()

    page.screenshot(path='result.png', full_page=True)
    sleep(3)
    
    browser.close()
