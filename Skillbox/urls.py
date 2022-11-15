"""Skillbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from apps.settings.views import index, contact, news_detail,news_index, user_not_found, register_error
from apps.courses.views import courses_detail
from apps.users.views import account_update
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('account/update/<int:id>', account_update, name = "account_update"),
    path('course/<int:id>', courses_detail, name = "courses_detail"),
    path('contact/', contact, name="contact"),
    path('news/<int:id>', news_detail, name = 'news_detail' ),
    path('news/', news_index, name = "news_index"),
    path('category/', include('apps.categories.urls')),
    path('users/', include('apps.users.urls')),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = "logout"),
    path('accounts/', include('allauth.urls')),
]


urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)