from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


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
    
    #Number of view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visists'] = num_visits+1
    
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_aviable': num_isntances_aviables,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    #Render the HTML template index.html with the data in the context variable
    return render(
        
        request=request,
        template_name='index.html',
        context=context
        
    )



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')    

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')



class BookListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    model = Book
    paginate_by = 10       
    # context_object_name = 'my_book_list' #your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] #get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html' #Specify your own template name/location
    
    # def get_context_data(self, **kwargs):
    #     #call the base implementation first to get the def get_context_data(self, **kwargs):
    #     context = super(BookListView,self).get_context_data(**kwargs)
    #     #create any data and add it to the context
    #     context['some_data'] = 'this is just some data'
        
    #     return context

class BookDetailView(generic.DetailView):
    """
    Generic class-based detail view for a book.
    """
    model = Book

    
class AuthorListView(generic.ListView):
    """
    Generic class-based view for a list of authors
    """
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    """
    Generic class-based detail view for a author.
    """        
    model = Author