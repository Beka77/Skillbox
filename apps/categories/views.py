from django.shortcuts import render
from apps.categories.models import Category
from apps.settings.models import Setting
from apps.courses.models import Courses
#Create your views here .
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    courses = Courses.objects.filter(category_id =category.id)
    context = {
        'category' : category,
        'setting' : setting,
        'categories':categories,
        'courses':courses
    }
    return render(request, 'shop-category.html', context) 