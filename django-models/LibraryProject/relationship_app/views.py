from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LibrarianProfileForm, MemberProfileForm, BookForm
from django.contrib.auth.decorators import permission_required


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

#checks if user is librarian
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

# --- Views ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

#librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    if request.method == "POST":
        form = LibrarianProfileForm(request.POST)
        if form.is_valid():
            librarian = form.save(commit=False)
            librarian.name = request.user.username
            form.save()
            return redirect('librarian-view')
    
    else:
        return LibrarianProfileForm()
    return render(request, 'relationship_app/librarian_view.html', {'form':form})

#member view
@login_required
@user_passes_test
def member_view(request):
    if request.method == "POST":
        form = MemberProfileForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.name = request.user.username
            form.save()
            return redirect('member-view')
    else:
        return MemberProfileForm()
    return render(request, 'relationship_app/member_view.html', {'form':form})


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.cad_edit_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/edit_book.html', {'form':form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, isinstance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        BookForm()
    return render(request, 'relationship_app/delete_book.html', {'form':form})


def list_book(request):
    books = Book.objects.all()
    context = {'list_book': books}
    return render(request, 'relationship_app/list_books.html', context)

class BookListView(ListView):
    model = Library
    template_name = 'relationship_app/list_book.html'

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


#LibraryProject/relationship_app/views.py 
# doesn't contain: 
# ["from django.contrib.auth.decorators 
# import permission_required", 
# "relationship_app.can_add_book", 
# "relationship_app.can_change_book", 
# "relationship_app.can_delete_book"]



# Create your views here
# LibraryProject/relationship_app/views.py 
# doesn't contain: ["UserCreationForm()", "relationship_app/register.html"].

