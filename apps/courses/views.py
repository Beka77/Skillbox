from django.shortcuts import render
from .models import Courses
from apps.settings.views import Setting
from apps.categories.models import Category
# Create your views here.

def courses_detail(request, id):
    courses = Courses.objects.get(id = id)
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    context= {
        'courses' : courses,
        'setting': setting,
        'categories' : categories,
    }
    return render (request, 'blog-single-left-sidebar.html', context)