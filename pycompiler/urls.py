
from django.urls import path, include

# import views

from . import views

urlpatterns = [
    path('ques/<id>/', views.index, name="indexpage"),
    path('', views.index, name="indexpage"),
    path('runcode/<id>/', views.runcode, name="runcode"),
    path('submitgg/<id>', views.submitgg),
    # path('login', views.login_page),
    # path('register-student/', views.registerstu),
    # path('register-faculty/', views.registerfac)

    # path('save', views.save)
]