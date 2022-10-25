from django.test import Client
from django.test import TestCase, SimpleTestCase
from books.forms import FeedbackForm
from django.urls import reverse
from books.models import Feedback


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

