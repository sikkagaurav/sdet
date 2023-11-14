
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Setup
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

def test_verify_page_title(driver):
    driver.get("http://webdriveruniversity.com/index.html")
    assert "WebDriverUniversity.com" in driver.title

def test_verify_dropdown_checkboxes_radiobuttons(driver):
    driver.find_element(By.ID, "dropdown-checkboxes-radiobuttons").click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    assert "Dropdown, Checkboxe(s), Radio Button(s)" in driver.title

def test_select_value_from_dropdown(driver):
    driver.find_element(By.ID, "dropdowm-menu-1").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='python']").click()
    selected_option = driver.find_element(By.ID, "dropdowm-menu-1").get_attribute("value")
    assert selected_option == "python"

def test_select_multiple_checkboxes(driver):
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for checkbox in checkboxes:
        checkbox.click()
    checked_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']:checked")
    unchecked_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']:not(:checked)")
    assert len(checked_checkboxes) == 3
    assert len(unchecked_checkboxes) == 2

def test_select_radio_button(driver):
    radio_button = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")
    radio_button.click()
    checked_radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']:checked")
    unchecked_radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']:not(:checked)")
    assert len(checked_radio_buttons) == 1
    assert len(unchecked_radio_buttons) == 2

