from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('regist/', Regist.as_view(), name="regist"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<str:id>/', Profile.as_view(), name="profile"),
    path('profile_update/', Profile_update.as_view(), name="profile_update"),
    path('passwordchange/', Password_change.as_view(), name="password_change")

]
