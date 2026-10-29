from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('index.html', views.home, name='index'),
    path('archives.html', views.archives, name='archives'),
    path('demo.html', views.demo, name='demo'),
    path('page.html', views.page, name='page'),
    path('blog.html', views.blog, name='blog'),
    path('single.html', views.single, name='single'),
]