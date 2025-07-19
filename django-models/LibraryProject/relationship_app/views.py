from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Library, Book, Librarian, Author
from django.contrib.auth import login
from .forms import LibrarianProfileForm, AdminProfileForm, MemberProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test



@user_passes_test
@login_required
def admin_view(request):
   if request.userprofile.role != "Admin":
       return HttpResponseForbidden("You do not have clearence to view this page")
   return render(request, 'relationship_app/admin_view.html')
@user_passes_test
@login_required
def librarian_view(request):
    if request.method == "POST":
        form = LibrarianProfileForm(request.POST)
        if form.is_valid():
            librarian = form.save(commit=False)
            librarian.user = request.user
            form.save()
            return redirect('librarian-detail', pk=librarian.pk )
    else:
        form = LibrarianProfileForm()
    return render(request, 'relationship_app/librarian_profile.html', {'form':form})

@user_passes_test
@login_required
def member_view(request):
    if request.method == "POST":
        form = MemberProfileForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = request.user
            form.save()
            return redirect('member-detail', pk=member.pk)
    else:
        form = MemberProfileForm()
    return render(request, 'relationship_app/member.html', {'form':form})

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

