from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    SAVE_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')

