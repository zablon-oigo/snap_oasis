from django.urls import path
from .views import (sign_in, sign_out, sign_up)
app_name='users'


urlpatterns=[
    path('Login/',sign_in, name='login'),
    path('Logout/',sign_out, name='logout'),
    path('Register/',sign_up, name='register')

]