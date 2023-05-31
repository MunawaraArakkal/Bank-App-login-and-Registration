from . import views
from django.urls import path
app_name = 'bankapp'

urlpatterns = [
    path("",views.home,name="home"),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('newpage/',views.newpage,name='newpage'),
    path('form/',views.form,name='form')
]