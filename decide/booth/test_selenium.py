from django.test import TestCase
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from django.utils import timezone

from base.tests import BaseTestCase
import time
from census.models import Census
from voting.models import Question, Voting, Auth
from django.contrib.auth.models import User


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class AdminTestCase(StaticLiveServerTestCase):

    def create_voting(self):
        q = Question(desc='test question', type='T')
        q.save()
        v = Voting(name='test voting', question=q)
        v.save()

        a, _ = Auth.objects.get_or_create(url=settings.BASEURL,
                                          defaults={'me': True, 'name': 'test auth'})
        a.save()
        v.auths.add(a)
        return v

    def get_or_create_user(self,pk):
        user, _ = User.objects.get_or_create(pk=pk)
        user.username = 'user{}'.format(pk)
        user.set_password('qwerty')
        user.save()
        return user

    def setUp(self):
        #Crea un usuario admin y otro no admin
        self.base = BaseTestCase()
        self.base.setUp()

        v = self.create_voting()
        v.question.save()
        self.v = v
        #Añadimos al usuario noadmin al censo y empezamos la votacion
        user = self.get_or_create_user(1)
        user.is_active = True
        user.save()
        c = Census(voter_id=user.id, voting_id=v.id)
        c.save()

        v.create_pubkey()
        v.start_date = timezone.now()
        v.save()
        #Opciones de Chrome
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()
    
    def test_commentquestion(self):

        self.driver.get(f'{self.live_server_url}/booth/{self.v.id}/')
        self.driver.set_window_size(910, 1016)

        time.sleep(1)
        self.driver.find_element(By.ID, "menu-toggle").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "goto-logging-button").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("noadmin")
        time.sleep(1)

        self.driver.find_element(By.ID, "password").send_keys("qwerty")
        time.sleep(1)

        self.driver.find_element(By.ID, "process-login-button").click()
        time.sleep(1)

        self.driver.find_element(By.ID, "floatingTextarea2").send_keys("Comentario de prueba")
        time.sleep(1)
        # Realizar la votación clickando en Vote 
        self.driver.find_element(By.ID, "send-vote").click()
        time.sleep(1)

        # Verificar que la votación se realizó correctamente
        success_alert = self.driver.page_source
        expected_text = "Congratulations. Your vote has been sent"
        self.assertTrue(expected_text in success_alert, "La alerta de éxito no está presente después de votar")
            