from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Book, Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'

# --- Views ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')




def book_list(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class BookDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    
class SignUpView(CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/login'






# Create your views here
# LibraryProject/relationship_app/views.py 
# doesn't contain: ["UserCreationForm()", "relationship_app/register.html"].

