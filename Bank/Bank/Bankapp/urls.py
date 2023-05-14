from django.contrib import admin
from django.urls import path, include
from. import views
app_name='Bankapp'

# urlpatterns = [
#     path('register', views.register, name='register'),
#     path('login', views.login, name='login'),
#     path('logout', views.logout, name='logout'),
#     path('new', views.new, name='new'),
#
#     path('', views.demo, name='demo'),
#
# ]
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.demo,name='demo'),
    # path('new', views.new, name='new'),
    path('empty', views.empty, name='empty'),
    path('new', views.PersonCreateView.as_view(), name='new'),
    path('message', views.message, name='message'),



]