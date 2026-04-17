from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.detail,name='detail'),
    path('add/',views.add_task,name='add'),
    path('update/<int:id>',views.update_task,name='update'),
    path('delete/<int:id>',views.delete_task,name='delete_task'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='list/login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('complete/<int:id>',views.complete_task,name='complete_task'),
]
