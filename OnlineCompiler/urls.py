"""OnlineCompiler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from user_handler import views

urlpatterns = [
    path('admin/', admin.site.urls),
#---------User Handler---------#
    path('logout/', views.logout_page),
    path('login/', views.login_page),
    path('register-student/', views.registerstu),
    path('register-faculty/', views.registerfac),
    path('new_test', views.new_test),
    path('new_testcase', views.new_testcase),
    path('create-testcase', views.create_testcase),
    path('create-qs', views.create_qs),
    path('questions/', views.allques),
    path('searchquestion/', views.sq),
    path('attempted/<id>/', views.attempted),
#---------Compilers------------#
    path('', include('pycompiler.urls')),
    path('c/', include('C.urls')),
]
