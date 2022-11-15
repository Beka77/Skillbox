from django.shortcuts import render, redirect
from apps.settings.models import Setting, News, Contact
from apps.categories.models import Category
from apps.courses.models import Courses
from apps.users.models import User

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    courses = Courses.objects.all()
    users = User.objects.all()
    news = News.objects.all()
    context = {
        'setting':setting,
        'courses': courses,
        'categories' : categories,
        'users': users,
        'news' : news
    }
    return render (request, 'index-mp-layout1.html', context) 
def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, email = email, message = message,)
        send_mail(
                    # title:
                    f"{setting.title}",
                    # message:
                    f"{name} спасибо за ваше сообщение. В скором времени мы вам ответим. Ваше сообщение {message}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
            )
        return redirect('thank_you')
    context = {
        'setting' : setting,
    }
    return render(request, 'page-contact-style1.html', context)



def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news_detail = News.objects.get(id = id)
    categories = Category.objects.all()
    context = {
        'setting' : setting, 
        'news' : news_detail,
        'categories' : categories,
    }
    return render (request, 'news_detail.html', context)

def news_index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    user = User.objects.latest('id')
    categories = Category.objects.all()
    context = {
        'setting' : setting,
        'news' : news,
        'user':user,
        'categories' : categories,
    }
    return render (request, 'news_index.html', context)

def user_not_found(request):
    return render (request, 'user_not_found.html')

def register_error(request):
    return render (request, 'register_error.html')