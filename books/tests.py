from django.test import Client
from django.test import TestCase
from django.urls import reverse

from books.models import Feedback


class FeedbackTestCase(TestCase):
    def setUp(self) -> None:
        """Creating test objects in the database"""
        Feedback.objects.create(text="I really adore this application")
        Feedback.objects.create(text="I do not know why it was created at all")

    def testTheMethod(self):
        """Testing the '__str__' method created in books.models'"""
        first_fb = Feedback.objects.get(text="I really adore this application")
        second_fb = Feedback.objects.get(text="I do not know why it was created at all")
        self.assertEqual("The text of the selected user's review: I really adore this application",
                         f"The text of the selected user's review: {first_fb.text}")
        self.assertEqual("The text of the selected user's review: I do not know why it was created at all",
                         f"The text of the selected user's review: {second_fb.text}")


class MainPageTestCase(TestCase):
    """Testcase for the main page and for the right status code(200)"""
    def test_main_page(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

