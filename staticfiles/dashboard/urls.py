from django.urls import path
from .views import index
app_name='dahsboard'

urlpatterns=[
    path('dasboard/', index, name='index')
]