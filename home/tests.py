from django.test import TestCase, SimpleTestCase


# Create your tests here.
# tự tạo test đơn giản
class SimpleTest(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get("/home")
        self.assertEquals(response.status_code, 301)
