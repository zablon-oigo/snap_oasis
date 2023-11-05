from django.urls import path
from .views import product_detail,home

app_name='market' 

urlpatterns=[
    path('', home, name='home'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:item>/', product_detail, name='detail'),
    
]