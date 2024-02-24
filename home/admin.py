from django.contrib import admin
from home.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')

admin.site.register(Student, StudentAdmin)