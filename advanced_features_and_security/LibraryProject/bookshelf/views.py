from django.shortcuts import render
from relationship_app.forms import BookForm
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.permissions', raise_exception=True)
def can_view(request):
    



# Create your views here.
