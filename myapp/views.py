from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author,Book
from .forms import BookForm  # Import the custom form

def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'home.html')  # Render the template
def about(request):
    #return HttpResponse("About Page")  # Returns a simple HTTP response
     return render(request, 'about.html')

# List view to show all authors
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

# Detail view to show a single author's details
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

# Create view to add a new author
class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'last_name']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')

# Update view to edit an existing author
class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'last_name']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')

# Delete view to delete an existing author
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')


# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm  # Use the custom form
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
