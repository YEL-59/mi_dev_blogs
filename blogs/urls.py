from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.home),
    path('news/<int:pk>', views.home2, name='news')
]
