from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualize_tables, name='table_struct'),
    path('table', views.index, name='index'),

]