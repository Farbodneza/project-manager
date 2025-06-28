from django.urls import path
from user.views import RegisterUserAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]