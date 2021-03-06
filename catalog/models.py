from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    '''Model representing a Book genre.'''
    name = models.CharField(
        max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        '''String for representing the Model object.'''
        return self.name


class Language(models.Model):
    '''Model representing a Language'''
    name = models.CharField(
        max_length=200, help_text='Enter the book\'s natural language')

    def __str__(self):
        '''String for representing the Model object'''
        return self.name


class Book(models.Model):
    '''Model representing a book (but not a specific copy of a book).'''
    title = models.CharField(max_length=200)

    # Foreign key used because book can only have one author, but authors can have multiple books
    # Author as String rather than object
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character')

    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this book')

    def __str__(self):
        '''String for representing the Model object'''
        return self.title

    def get_absolute_url(self):
        '''Returns a URL to access detailed record for this book.'''
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    'Model representing a specific copy of a book (i.e that can be borrowed from the library).'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique Id for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        '''String for representing the Model object'''
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    '''Model representing an author.'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        '''Returns the url to a particular author instance.'''
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        '''String for representing the Model object'''
        return f'{self.last_name}, {self.first_name}'


# class MyModelName(models.Model):
#     """A typical class defining a model, derived from the Model class."""

#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')

#     # Metadata
#     class Meta:
#         ordering = ['-my_field_name']

#     # Methods
#     def get_absolute_url(self):
#         '''Returns the url to a particular instance of MyModelName.'''
#         return reverse('model_detail_view', args=[str(self.id)])

#     def __str__(self):
#         '''String for representing the MyModelName Object (in Admin site etc.).'''
#         return self.my_field_name
