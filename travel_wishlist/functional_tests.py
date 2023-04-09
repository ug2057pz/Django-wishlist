from selenium.webdriver.chrome.webdriver import webdriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super (). tearDownClass()

    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Travel Wishlist', self.selenium.title)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super (). tearDownClass()

    def test_add_new_place(self):
        self.selenium.get(self.live_server_urt)
        input_name = self.selenium.find_element_by_id(" id_name")
        input_name. send_keys ('Denver')
                               
        add_button = self.selenium.find_element_by_id('add-new-place')
        add_button.click()

        denver = self.selenium.find_element_by_id ('place-name-S')
        self.assertEqual('Denver', denver.text)

        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn( 'New York', self.selenium. page_source)
        self.assertIn('Tokyo', self.selenium.page_source)

        #this will error if Denver, pk=5 isn't there
        denver_db = Place.objects.get (pk=5)
        self.assertEqual('Denver', denver_db.name)
        self.assertTrue(denver_db.visited)