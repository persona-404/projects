from django.urls import path

from .import views

app_name = 'item' # namespace for this app

urlpatterns = [
    path('', views.browse, name='browse'),
    path('new/', views.new, name='new'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
    path('<int:item_id>/edit/', views.edit, name='edit'),
]
