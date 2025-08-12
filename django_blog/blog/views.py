from django.shortcuts import render, redirect
from . models import Post
from django.contrib import messages
from .forms import UserRegisterForm

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

# Create your views here.
