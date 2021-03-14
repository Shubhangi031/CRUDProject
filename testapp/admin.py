from django.contrib import admin
from testapp.models import Library

# Register your models here.
class LibraryView(admin.ModelAdmin):
    list_display=["name","city","book","date_of_issue","return_date",]




admin.site.register(Library,LibraryView)
