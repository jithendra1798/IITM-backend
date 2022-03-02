from base64 import urlsafe_b64encode
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('badges/',views.show_badges,name='badges'),
    path('badge/verify',views.verify,name='verify'),
]