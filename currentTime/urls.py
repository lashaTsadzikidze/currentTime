from django.contrib import admin
from django.urls import path
from currTime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currenttime/', views.current_time),
]
