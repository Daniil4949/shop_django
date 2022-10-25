from django.test import TestCase
from django.test import Client
from django.test import TestCase, SimpleTestCase
from cart.forms import SearchBookForm
from django.urls import reverse


class SearchformTestCase(TestCase):
    def test_form_valid_data(self):
        form = SearchBookForm(data={
            "title": "Martin Eden"
        })
        self.assertTrue((form.is_valid()))
