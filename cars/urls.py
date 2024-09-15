# from django.urls import path
# from . import views
# from .views import CarListAPIView, CarDetailAPIView, CommentListAPIView
#
# urlpatterns = [
#     path('', views.car_list, name='car_list'),
#     path('cars/<int:pk>/', views.car_detail, name='car_detail'),
#     path('cars/add/', views.add_car, name='add_car'),
#     path('cars/<int:pk>/edit/', views.edit_car, name='edit_car'),
#     path('cars/<int:pk>/delete/', views.delete_car, name='delete_car'),
#     path('cars/<int:pk>/comments/add/', views.add_comment, name='add_comment'),
#     path('api/cars/', CarListAPIView.as_view()),
#     path('api/cars/<int:pk>/', CarDetailAPIView.as_view()),
#     path('api/cars/<int:pk>/comments/', CommentListAPIView.as_view()),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
    path('add/', views.add_car, name='add_car'),
    path('<int:pk>/edit/', views.edit_car, name='edit_car'),
    path('<int:pk>/delete/', views.delete_car, name='delete_car'),
    path('<int:pk>/comments/add/', views.add_comment, name='add_comment'),
    path('profile/', views.profile, name='profile'),
]