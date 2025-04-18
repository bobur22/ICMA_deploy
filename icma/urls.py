from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about_center/', about_center, name='about_center'),
    path('administration/', administration, name='administrarion'),
    path('articles/', articles, name='articles'),
    path('articles/<int:id>/', articles_detail, name='articles_detail'),
    path('contact_us/', contact_us, name='contact_us'),
    path('corruption/', corruption, name='corruption'),
    path('employees/', employees, name='employees'),
    path('infrostructure/', infrostructure, name='infrostructure'),
    path('monitoring/', monitoring, name='monitoring'),
    path('monitoring/<int:id>/', monitoring_detail, name='monitoring_detail'),
    path('news/', news, name='news'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('passport/', passport, name='passport'),

]
