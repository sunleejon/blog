import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from App.models import User, Article, Comment


def register(request):
    # 注册

    if request.method == "GET":
        data = {
            "title": "注册",
        }
        return render(request, 'user/register.html', context=data)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #print(username)
        #print(password)
        password = make_password(password)
        user = User()
        user.u_username = username
        user.u_password = password
        user.save()
        return redirect(reverse("blog:login"))
    else:
        return redirect(reverse("blog:register"))


def login(request):
    # 登录

    if request.method == "GET":
        error_message = request.session.get('error_message')

        data = {
            "title": "登录"
        }
        if error_message:
            del request.session["error_message"]
            data['error_message'] = error_message

        return render(request, 'user/login.html', context=data)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        users = User.objects.filter(u_username=username)
        if users.exists():
            user = users.first()
            if check_password(password, user.u_password):
                request.session["user_id"] = user.id
                #print(request.session)
                #print(request.session["user_id"])
                return redirect(reverse("blog:mine"))
            else:
                request.session["error_message"] = "password error"
                return redirect(reverse("blog:login"))
        else:
            #print("用户不存在")
            request.session["error_message"] = "user does not exist"
            return redirect(reverse("blog:login"))
    else:
        return redirect(reverse("bloh:login"))


def mine(request):
    user_id = request.session.get("user_id")
    #print(user_id)
    if user_id:
        try:
            #print("///////////")
            user = User.objects.get(pk=user_id)
            #user_name = user.u_username
            article = Article.objects.filter(a_user=user_id)
            #print(user)
            #print(article)

            #print(user_num)

            #print(article)

            data = {
                "user": user,
                "article": article,
                "status": 200,
                "msg": "ok",


            }
            return render(request, "main/mine.html", context=data)
        except:
            #print("*********")
            user = User.objects.get(pk=user_id)
            return render(request, "main/mine.html")



    return render(request, "main/mine.html")


def createarticle(request):
    if request.method == "POST":
        try:
            user_id = request.session.get("user_id")
            title = request.POST.get("title")
            article = request.POST.get("article")
            #print(user_id)
            #print(title)
            #print(article)
            articles = Article()
            articles.a_user = User.objects.get(pk=user_id)
            articles.a_title = title
            articles.a_desc = article
            articles.save()
            data = {
                "msg": "ok",
                "status": 200
            }
            return JsonResponse(data=data)
        except:
            data = {
                "msg": "error"
            }
            #print("error")
            return render(request, "main/mine.html")
            #return JsonResponse(data=data)
    elif request.method == "GET":





        return render(request, "main/create_article.html")


def article(request, articleid):
    if request.method == "GET":
        article = Article.objects.get(pk=articleid)
        author = User.objects.get(pk=article.a_user_id)
        #print(article)
        #comment = ""
        #print(len(comment))

        try:
            comment = Comment.objects.filter(c_article_id=article.id)
            #print(comment)
        except:
            comment = ""
        comments = []
        user_names = []
        # user_name = User.objects.get(pk=comment.c_user_id)
        # user_comment = comment.c_content
        user_id = Comment.objects.filter(c_article=article.id)
        #user_name_id = User.objects.filter(pk=user_id.c_user_id)
        #print(user_name_id)
        #print(user_id)
        for i in user_id:
            comments.append(i.c_content)
            user_names.append(User.objects.get(pk=i.c_user_id).u_username)
        #print(comments)
        #print(user_names)
        dict_comment = dict(map(lambda x,y:[x, y], comments, user_names))
        #print(dict_comment)
        #for i in
        request.session["article_id"] = articleid

        data = {
            "article": article,
            "comment": comment,
            "author": author,
            "comments": comments,
            "user_names": user_names,
            "dict_comment": dict_comment,

        }

        return render(request, "main/article.html", context=data)
    elif request.method == "POST":
        pass


def comment(request):
    c_content = request.POST.get("c_content")
    #c_article_id = request.POST.get("c_article_id")

    c_article_id = request.session.get("article_id")
    c_user_id = request.session.get("user_id")
    print(c_content)
    print(c_article_id)
    print(c_user_id)
    comment = Comment()

    comment.c_content = c_content
    comment.c_user_id = c_user_id
    comment.c_article_id = c_article_id
    comment.save()
    print(comment)

    data = {
             "status": 200,
             "msg": "ok",
         }

    return JsonResponse(data=data)


def allblog(request):
    article = Article.objects.all()
    art = []
    for i in article:
        art.append(i)
        #print(i)
        #print(art)
    data = {
        "art": art,
    }
    return render(request, "main/allblog.html", context=data)



















