from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('checker',views.checker,name='checker'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout')
]