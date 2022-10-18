from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Book, Author, Rating, Comment
from django.views import View
from django.views.generic.edit import FormView
from .forms import FeedbackForm


#  TODO:
#    1. Improve design
#    2. Refactoring the code in books/views.py
#    Desired:
#    1. Use celery/redis
#    2. Use signals


class MainPage(ListView):
    """There are 4 books for each page."""
    paginate_by = 4
    model = Book
    template_name = "menu/main_page.html"


class Authors(ListView):
    """There are 4 authors for each page."""
    paginate_by = 4
    model = Author
    template_name = 'menu/authors.html'


class CategoryBook(ListView):
    """There are all the books of the selected category"""
    template_name = "menu/category_books_page.html"
    model = Book
    context_object_name = 'books'
    allow_empty = False

    def get_queryset(self):
        """Getting all the books of the selected category with slug"""
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        return Book.objects.filter(category=category)


class BookInfo(View):
    """Page for the selected book"""
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        """Here we make query for getting the book by slug and the comments for the selected book.
        There is try/except block. If user hasn't visited this page before the new 'rating' object would create for him.
         I also would like to use signals for that"""
        book = Book.objects.get(slug=self.kwargs['book_slug'])
        comments = Comment.objects.filter(book__slug=self.kwargs['book_slug'])
        if request.user.is_authenticated:
            try:
                rating = Rating.objects.get(user=self.request.user, book=book)
            except:
                Rating.objects.create(user=self.request.user, book=book)
                rating = Rating.objects.get(user=self.request.user, book=book)
            return render(request, 'menu/book.html', {'book': book, 'rating': rating, 'comments': comments})
        return render(request, 'menu/book.html', {'book': book, 'comments': comments})


class AuthorInfo(DetailView):
    """Page for the selected author"""
    template_name = "menu/author.html"
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'


class FeedBackForm(FormView):
    template_name = "menu/feedback.html"
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

