import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

def testing():
    phone = 'xiaomi mi 11 lite'
    driver.implicitly_wait(20)
    driver.get('https://rozetka.com.ua/')

    driver.find_element(By.CSS_SELECTOR, "input.search-form__input").send_keys(phone, Keys.ENTER)
    time.sleep(5)
    result = driver.find_element(By.CSS_SELECTOR, 'div.lite-tile__inner').text

    assert phone.lower() in result.lower(), 'This phone does not exist!'

    driver.quit()

testing()