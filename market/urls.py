from django.urls import path
from .views import product_detail,home,search_items,update_Item,add_Item,delete_Item

app_name='market' 

urlpatterns=[
    path('', home, name='home'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:item>/', product_detail, name='detail'),
    path('search/',search_items, name='search'),
    path('add-Item/',add_Item, name='addItem' ),
    path('update-Item/<int:pk>/', update_Item, name='updateItem'),
    path('delete-Item/<int:pk>/', delete_Item, name='deleteItem'),
    
]