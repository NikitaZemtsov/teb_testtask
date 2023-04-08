from django.urls import path
from .views import LoginUser, registration, user_profile, logout_user

urlpatterns = [
        path('', registration, name="register"),
        path('login/', LoginUser.as_view(), name="login"),
        path('profile/', user_profile,  name="user_profile"),
        path('logout/', logout_user, name='logout'),
]