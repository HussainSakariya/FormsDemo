from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',reg,name='reg'),
    path('edit/<int:id>/',edit),
    path('delete/<int:id>/',delete),
    path('display/',display)
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)