from .test_setup import TestSetup
# from ..models import User
from authentication.models import User


class TestViews(TestSetup):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        # import pdb
        # pdb.set_trace()
        self.assertAlmostEqual(res.status_code, 400) # this number is like status we can except from our request

    def test_user_can_register_with_data(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertAlmostEqual(res.data['email'], self.user_data['email'])
        self.assertAlmostEqual(res.data['username'], self.user_data['username'])
        self.assertAlmostEqual(res.status_code, 201)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertAlmostEqual(res.status_code, 401) # it will be failure because user is not verified

    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified=True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertAlmostEqual(res.status_code, 200)
