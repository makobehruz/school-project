from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.person_list, name = 'list'),
    path('group/', views.person_create, name = 'group'),
    path('detail/<int:pk>/', views.person_detail, name='detail'),
    path('delete/<int:pk>/', views.person_delete, name='delete'),


]