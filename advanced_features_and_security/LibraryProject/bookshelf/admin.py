from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager
from .models import CustomUser, CustomUserManager

admin.site.register(CustomUser, CustomUserManager)
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')



#oesn't contain: ["admin.site.register(CustomUser, CustomUserAdmin)"]