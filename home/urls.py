from django.contrib import admin
from django.urls import path , include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name="home"),
    path('login', views.loginUser , name="login"),
    path('logout', views.logoutUser , name="logout"),
    path('task', views.task , name="task"),
    path('returnn', views.returnn , name="returnn"),
    path('favicon.ico', views.okay , name = "okay"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
