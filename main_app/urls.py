from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('lighthouses/', views.lighthouses_index, name='index'),
path('lighthouses/<int:lighthouse_id>/', views.lighthouses_detail, name='detail'),
path('lighthouses/create/', views.LighthouseCreate.as_view(), name='lighthouses_create'),
path('lighthouses/<int:pk>/update/', views.LighthouseUpdate.as_view(), name='lighthouses_update'),
path('lighthouses/<int:pk>/delete/', views.LighthouseDelete.as_view(), name='lighthouses_delete'),
]