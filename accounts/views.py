from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm, RegistrationForm
from users.models import *
from django.views import View
from cart.models import Payment
from books.models import Rating
from django.shortcuts import get_object_or_404


class RegisterUser(CreateView):
    """View class for the registration"""
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = "registration/registration.html"


class LoginUser(LoginView):
    """View class for the authentication"""
    form_class = LoginUserForm
    template_name = "registration/login.html"
    model = CustomUser
    success_url = reverse_lazy('home')


class Profile(View):
    """Here You can see try/except block for
        getting all the data about the user, if there are no information
        about the user, we just cannot get it, we do not have it in the 'context'
        dict. But if there are some information about the user, we can get
        the purchased books and the most rated books. """
    def get(self, request, *args, **kwargs):
        context = {}
        try:
            rated_books = Rating.objects.filter(user=self.request.user).order_by('score')[:5]
            purchased_books = Payment.objects.filter(user=self.request.user)[:5]
            context['purchased_books'] = purchased_books
            if rated_books[0].score > 0:
                context['rated_books'] = rated_books[::-1]
        except:
            pass
        return render(request, 'menu/profile.html', context)
# Create your views here.
