from django.contrib import admin
from django.urls import path
from core.views import send_notification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', send_notification),
]
