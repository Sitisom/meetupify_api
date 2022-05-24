from django.urls import path
from rest_framework_simplejwt import views as jwt

from auth.views import RegisterView

urlpatterns = [
    path('login/', jwt.TokenObtainPairView.as_view()),
    path('login/refresh/', jwt.TokenRefreshView.as_view()),
    path('signup/', RegisterView.as_view())
]