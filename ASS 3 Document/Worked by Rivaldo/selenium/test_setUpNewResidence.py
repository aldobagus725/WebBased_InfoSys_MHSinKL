# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSetUpNewResidence():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_setUpNewResidence(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1030, 543)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("aldobagus")
    self.driver.find_element(By.ID, "password").send_keys("12345678")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) p").click()
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys("Jakarta")
    self.driver.find_element(By.NAME, "numunits").send_keys("10")
    self.driver.find_element(By.NAME, "sizeperunits").send_keys("600 m2")
    self.driver.find_element(By.NAME, "monthlyrental").click()
    self.driver.find_element(By.NAME, "monthlyrental").send_keys("3000")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
