from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre, Language
from django.views import generic

# Create your views here.


def index(request):
    '''View function for homepage of site'''

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.all()
    # template_name = 'catalog/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
