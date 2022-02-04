from os import name
from . import views
from django.urls import path
app_name='reserve'
urlpatterns = [
    path('',views.ReserveView.as_view(),name='page-reserve'),
]
