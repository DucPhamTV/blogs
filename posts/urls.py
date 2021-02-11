from django.urls import path

from . import views

urlpatterns = [
    # /posts
    path('', views.index, name='index'),
    path('<slug:name>/', views.detail, name='detail'),
]
