import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_title(driver):
    driver.get('http://webdriveruniversity.com/index.html')
    assert driver.title == 'WebDriverUniversity.com'

def test_new_tab(driver):
    driver.find_element(By.ID, "dropdown-checkboxes-radiobuttons").click()
    handles = driver.window_handles
    assert len(handles) == 2
    driver.switch_to.window(handles[1])
    
def test_drop_menu(driver):
    driver.find_element(By.ID, "dropdowm-menu-1").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='python']").click()
    selected_option = driver.find_element(By.ID, "dropdowm-menu-1").get_attribute("value")
    assert selected_option == "python"

def test_checkboxes(driver):
    boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for box in boxes:
        box.click()

    checked = len(driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']:checked"))
    unchecked = len(driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']:not(:checked)"))
    assert checked == 3
    assert unchecked == 1

def test_radio_buttons(driver):
    buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
    buttons[2].click()

    checked = len(driver.find_elements(By.CSS_SELECTOR, "input[type='radio']:checked"))
    unchecked = len(driver.find_elements(By.CSS_SELECTOR, "input[type='radio']:not(:checked)"))
    assert checked == 2
    assert unchecked == 6
