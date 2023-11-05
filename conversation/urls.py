from django.urls import path
from .views import new_conversation,inbox,detail

app_name='conversation'

urlpatterns=[
    path('', inbox,name='inbox'),
    path('detail/<int:pk>/',detail ,name='detail'),
    path('new/<int:item_pk>/',new_conversation, name='new' ),

]