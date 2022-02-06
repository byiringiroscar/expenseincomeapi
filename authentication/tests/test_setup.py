from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        # for dynamic data we using faker to help us to find dynamic data
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email().split('@')[0],
        }

        # this is static data for testing
        # self.user_data = {
        #     'email': 'byiringoroscar@gmail.com',
        #     'username': 'papaoscar',
        #     'password': 'password123',
        # }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
