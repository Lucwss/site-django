from django.urls import path
from blog import views
from .views import PostView

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]