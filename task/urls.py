from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('update/<id>', views.update),
    path('delete/<id>', views.delete),
]