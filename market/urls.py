from django.urls import path
from .views import product_detail,home,search_items

app_name='market' 

urlpatterns=[
    path('', home, name='home'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:item>/', product_detail, name='detail'),
    path('search/',search_items, name='search'),
    
]