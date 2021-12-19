from django.contrib import admin
from django.urls import path

from . import views

app_name = 'umapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('umagirl/list/', views.UmaGirlListView.as_view(), name="UmaGirlList"),
    path('umagirl/<slug:slug>', views.UmaGirlDetailView.as_view(), name="UmaGirlDetail")
]
