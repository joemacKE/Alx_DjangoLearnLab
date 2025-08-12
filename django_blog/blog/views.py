from django.shortcuts import render, redirect
from . models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.models import User

from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username} successfully")
            return redirect('login')
        else:
            form = UserRegisterForm()

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user.profile)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated succesfully")
            return redirect('blog/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'blog/profile.html')

class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all()
        return context
class PostDetailView(DetailView):
    model = Post
    paginate_by = 10
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'publication_date', 'author']
    template_name = 'blog/post_form.html'
    reverse_lazy = 'blog_home'

class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post

#blog/views.py doesn't contain: ["DetailView", "CreateView", 


# Create your views here.
