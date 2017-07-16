from django.contrib import admin
from .models import University, Student

class UniversityAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'university']
    list_filter = [
        'university__name',
        'university__id', 
        'first_name', 
        'last_name',
        ]
    search_fields = ['university__name','first_name', 'last_name']

admin.site.register(University, UniversityAdmin)
admin.site.register(Student, StudentAdmin)

