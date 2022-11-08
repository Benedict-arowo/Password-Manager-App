from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createFolder', views.createFolder, name='new-folder'),
    path('createItem', views.createItem, name='new-item'),
    path('item', views.item, name='item'),
    path('deleteFolder', views.deleteFolder, name='delete-folder'),
    path('editFolder/<uuid:id>', views.editFolder, name='edit-folder'),
    path('deleteItem', views.deleteItem, name='delete-item'),
]
