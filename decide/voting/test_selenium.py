from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from base.tests import BaseTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from base import mods

class QuestionsTests(StaticLiveServerTestCase):

    def setUp(self):
        # Load base test functionality for decide
        self.base = BaseTestCase()
        self.client = APIClient()
        self.token = None
        mods.mock_query(self.client)
        user = User(username='admin', is_superuser=True, is_staff=True)
        user.set_password('qwerty')
        user.save()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()

    def createClassicQuestion(self):
        self.driver.get(self.live_server_url+"/admin/voting/question/add/")
        
        self.driver.find_element(By.ID, "id_desc").click()
        self.driver.find_element(By.ID, "id_desc").send_keys('Classic Question')
        self.driver.find_element(By.ID, "id_type").click()
        self.driver.find_element(By.ID, "id_type").send_keys('classic')
        self.driver.find_element(By.NAME, "_save").click()
    
    def createRankedQuestion(self):
        self.driver.get(self.live_server_url+"/admin/voting/question/add/")
        
        self.driver.find_element(By.ID, "id_desc").click()
        self.driver.find_element(By.ID, "id_desc").send_keys('Ranked Question')
        self.driver.find_element(By.ID, "id_type").click()
        self.driver.find_element(By.ID, "id_type").send_keys('ranked')
        self.driver.find_element(By.NAME, "_save").click()

    def test_createClassicQuestion(self):
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1280, 720)

        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("qwerty", Keys.ENTER)

        self.driver.get(self.live_server_url+"/admin/voting/question/add/")
        
        self.driver.find_element(By.ID, "id_desc").click()
        self.driver.find_element(By.ID, "id_desc").send_keys('Test')
        self.driver.find_element(By.ID, "id_type").click()
        self.driver.find_element(By.ID, "id_type").send_keys('classic')
        self.driver.find_element(By.NAME, "_save").click()
        self.assertTrue(self.driver.current_url == self.live_server_url+"/admin/voting/question/")

    def test_createRankedQuestion(self):

        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1280, 720)

        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("qwerty", Keys.ENTER)

        self.driver.get(self.live_server_url+"/admin/voting/question/add/")
        
        self.driver.find_element(By.ID, "id_desc").click()
        self.driver.find_element(By.ID, "id_desc").send_keys('Ranked Question')
        self.driver.find_element(By.ID, "id_type").click()
        self.driver.find_element(By.ID, "id_type").send_keys('ranked')
        self.driver.find_element(By.NAME, "_save").click()
        self.assertTrue(self.driver.current_url == self.live_server_url+"/admin/voting/question/")

    def test_createClassicQuestionOption(self):
        
        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1280, 720)

        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("qwerty", Keys.ENTER)

        self.createClassicQuestion()
        self.driver.get(self.live_server_url+"/admin/voting/questionoption/add/")
        self.driver.find_element(By.ID, "id_question").click()
        self.driver.find_element(By.ID, "id_question").send_keys('Classic Question')
        self.driver.find_element(By.ID, "id_number").click()
        self.driver.find_element(By.ID, "id_number").send_keys('1')
        self.driver.find_element(By.ID, "id_option").click()
        self.driver.find_element(By.ID, "id_option").send_keys('test1')
        self.driver.find_element(By.NAME, "_save").click()
        self.assertTrue(self.driver.current_url == self.live_server_url+"/admin/voting/questionoption/")
        self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME, "success"))==1)

    def test_createRankedQuestionOption(self):

        self.driver.get(f'{self.live_server_url}/admin/login/?next=/admin/')
        self.driver.set_window_size(1280, 720)

        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").send_keys("qwerty", Keys.ENTER)

        self.createRankedQuestion()
        self.driver.get(self.live_server_url+"/admin/voting/questionoptionranked/add/")
        self.driver.find_element(By.ID, "id_question").click()
        self.driver.find_element(By.ID, "id_question").send_keys('Ranked Question')
        self.driver.find_element(By.ID, "id_number").click()
        self.driver.find_element(By.ID, "id_number").send_keys('1')
        self.driver.find_element(By.ID, "id_option").click()
        self.driver.find_element(By.ID, "id_option").send_keys('test1')
        self.driver.find_element(By.NAME, "_save").click()
        self.assertTrue(self.driver.current_url == self.live_server_url+"/admin/voting/questionoptionranked/")
        self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME, "success"))==1)