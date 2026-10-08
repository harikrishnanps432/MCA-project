from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
 path("",views.home,name="home"),
 path("register/",views.register,name="register"),
 path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
 path("logout/",auth_views.LogoutView.as_view(),name="logout"),
 path("transaction/add/",views.add_transaction,name="add_transaction"),
 path("bills/",views.bills,name="bills"),
 path("feedback/",views.feedback,name="feedback"),
]
