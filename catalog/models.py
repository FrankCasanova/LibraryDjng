from django.db import models
from django.db.models.base import Model
from django.urls import reverse
import uuid #required for unique book instances 

# Create your models here.

class Genre(models.Model):
    """
    Molde representing a book genre.
    """
    
    name = models.CharField(
        max_length=200,     
    )
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    
class Language(models.Model):
    """
    model representing a language (e.g English, French, Japanese, etc.)
    """
    name = models.CharField(
        max_length=200,
        help_text='Enter the book\'s natural language (e.g English, French, Japanese, etc.)'
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book)
    """
    
    title = models.CharField(max_length=200)

    #foreign key used becaus book can only have one author, but authos can have multiple books
    #authors as a string rather tha object becasu it hasn't been declared yet in the file
    #TRICK: if u not has declared a class yet, u can use the model name as a string to avoid conflicts!
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True
    )
    
    summary = models.TextField(
        max_length=1000,
        help_text='Enter a brief description of the book'
    )
        
    isbn = models.CharField(
        max_length=13,
        unique=True,
        help_text='13 character <a href="https://www.sbn-international.org/content/what-isbn">ISBN number </a>'
    )
        
    #ManyToManyField used because genre can contain many books, Books can cover many genres.
    #Gener class has already been defined so we can specify the object above.
    gener = models.ManyToManyField(
        Genre,
        help_text='Select a genre for this book'
    )
    
    language = models.ForeignKey(
        'Language',
        on_delete=models.SET_NULL,
        null=True
    )
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book
        """
        return reverse("book-detail", args=[str(self.id)])
#-----------------------------------------------------------------------------------------------    
    
    
class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed form the library.)
    """   
     
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique ID for this particular book across whole library'
    )
    
    book = models.ForeignKey(
        'Book',
        on_delete=models.RESTRICT,
        null=True
    )
    
    imprint = models.CharField(max_length=200)
    
    due_back = models.DateField(
        null=True,
        blank=True
    )

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Aviable'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book aviability'
    )
    
    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        """
        String for representing the Model object.
        """     
        
        return f'{self.id} ({self.book.title})'
#---------------------------------------------------------------------------------------------    

class Author(models.Model):
    """
    Model representing an author
    """
    
    first_name = models.CharField(
        max_length=100
    )
    
    last_name = models.CharField(
        max_length=100
    )
    
    date_of_bird = models.DateField(
        null=True,
        blank=True
    )    
    
    date_of_death = models.DateField(
        'Died',
        null=True,
        blank=True
    )
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    