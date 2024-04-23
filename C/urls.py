from django.contrib import admin
from django.urls import path,include
from C import views


urlpatterns = [
path('runcode/<id>', views.runcode),
path('', views.homepage),
path('ques/<id>/', views.homepage, name="indexpage"),

]