from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    """
    View function for home page of site
    """
    
    #Generate counts of some of the main objects.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    #Aviable books (status='a').
    num_isntances_aviables = BookInstance.objects.filter(status__exact='a').count()
    
    #The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_aviable': num_isntances_aviables,
        'num_authors': num_authors,
    }
    
    #Render the HTML template index.html with the data in the context variable
    return render(
        
        request=request,
        template_name='index.html',
        context=context
        
    )