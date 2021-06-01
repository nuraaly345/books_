"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from main.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-book/', add_book, name='add-book'),
    path('mark-book/<id>/', mark_book, name='mark-book'),
    path('unmark-book/<id>/', unmark_book, name='unmark-book'),
    path('delete-book/<id>/', delete_book, name='delete-book'),
    path('open-book/<id>/', open_book, name='open-book'),
    path('page-book/', page_book, name='page-book'),
    path('contact/', contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
