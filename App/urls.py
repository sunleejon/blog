from django.urls import path, re_path

from App import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("mine/", views.mine, name="mine"),
    path("createarticle/", views.createarticle, name="createarticle"),
    path("comment/", views.comment, name="comment"),
    path("allblog/", views.allblog, name="allblog"),
    re_path("article/(?P<articleid>\d+)/", views.article, name="article"),



]