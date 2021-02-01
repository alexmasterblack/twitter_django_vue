"""twitter_django_vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from twitter_apps.base.views import startpage, signup
from twitter_apps.tweets.views import tweets
from twitter_apps.tweets.api import add_new_tweet
from twitter_apps.user_profile.views import user_profile, do_follow, do_unfollow, follows, followers, settings_user

urlpatterns = [
    # главная стартовая страница
    path('', startpage, name='startpage'),
    # регистрация
    path('signup/', signup, name='signup'),
    # выйти из аккаунта
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # залогиниться
    path('login/', views.LoginView.as_view(template_name='base/login.html'), name='login'),
    # страница с созданием твитов и их просмотром
    path('tweets/', tweets, name='tweets'),
    # создание нового твита, апи
    path('api/new_tweet/', add_new_tweet, name='add_new_tweet'),
    # профиль пользователя,
    path('u/<str:username>/', user_profile, name='user_profile'),
    path('u/<str:username>/settings_user/', settings_user, name='settings_user'),
    path('u/<str:username>/follow/', do_follow, name='do_follow'),
    path('u/<str:username>/unfollow/', do_unfollow, name='do_unfollow'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('u/<str:username>/followers/', followers, name='followers'),
    # админка
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
