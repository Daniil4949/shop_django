from django.test import Client
from django.test import TestCase, SimpleTestCase
from books.forms import FeedbackForm
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
    def setUp(self) -> None:
        self.client = Client
        self.list_url = reverse('home')

    def test_main_page(self) -> None:
        response = self.client.get(reverse('home'), {})
        self.assertEqual(response.status_code, 200)


class FeedbackFormTestCase(SimpleTestCase):
    """Text field of the model 'Feedback' is not nullable"""
    def test_expense_form_valid_data(self) -> None:
        form = FeedbackForm(data={
            'text': 'I adore this site!'
        })
        self.assertTrue(form.is_valid())

    def test_wrong_data_form(self) -> None:
        form = FeedbackForm(data={})
        self.assertFalse(form.is_valid())
