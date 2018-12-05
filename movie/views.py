import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from movie.models import UserModel, Movie, Collections
from movie.views_constant import HTTP_OK, HTTP_USER_EXIST


def hello(request):
    return HttpResponse("hello")


def home(request):
    all_movies = get_movies_image('https://www.vmovier.com/apiv3/index/getBanner')
    all_images = []
    for movie in all_movies:
        image = movie.get('image')
        images = str(image)
        all_images.append(images)

    movies = get_movies('https://www.vmovier.com/apiv3/post/getPostInCate?cateid=0&p=1')

    try:
        for movie in movies:
            m_movie = Movie()
            title = movie.get('title')
            m_movie.m_title = title

            ima = movie.get('image')
            m_movie.m_image = ima

            duration = movie.get('duration')
            m_movie.m_duration = duration

            appfutitle = movie.get('appfutitle')
            m_movie.m_appfutitle = appfutitle

            postid = movie.get("postid")
            m_movie.m_positid = postid
            m_movie.save()
    except Exception as e:
        a_movies = Movie.objects.all()
        return render(request, 'home.html', context=locals())
    a_movies = Movie.objects.all()
    return render(request, 'home.html', context=locals())


def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        s_password = request.POST.get('s_password')
        email = request.POST.get('email')
        icon = request.FILES.get("icon")
        if password != s_password:
            return render(request, 'register.html')
        else:
            try:
                user = UserModel()
                user.u_name = username
                user.u_password = password
                user.u_email = email
                user.u_icon = icon
                user.save()
            except Exception as e:
                return render(request, 'register.html')
            return render(request, 'login.html')


def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            return render(request, 'login.html')
        else:
            user = UserModel.objects.get(u_name=username)
            if user:
                if user.u_password == password:
                    #获取轮播图片
                    all_movies = get_movies_image('https://www.vmovier.com/apiv3/index/getBanner')
                    all_images = []
                    for movie in all_movies:
                        image = movie.get('image')
                        images = str(image)
                        all_images.append(images)
                    #获取全部电影
                    a_movies = Movie.objects.all()

                    y_icons_url = "/static/upload/"+user.u_icon.url
                    user = user
                    return render(request, 'home_logined.html', context=locals())
            else:
                return render(request, 'login.html')


def userinfo_mod(request, id):
    user = UserModel.objects.get(id=id)
    y_icons_url = "/static/upload/" + user.u_icon.url
    y_email = user.u_email
    y_name = user.u_name
    return render(request, 'userinfo_mod.html', context=locals())


def change(request, id):

    user = UserModel.objects.get(id=id)
    try:
        email = request.POST.get('email')
        icon = request.FILES.get('c_icon')
        if icon == '':
            return render(request, 'login.html')
        user.u_email = email
        user.u_icon = icon
        user.save()
    except Exception as e:
        return render(request, 'home_logined.html')
    y_icons_url = "/static/upload/" + user.u_icon.url
    user = user
    return render(request, 'home_logined.html', context=locals())


def collect(request, id):
    #获取轮播图片
    all_movies = get_movies_image('https://www.vmovier.com/apiv3/index/getBanner')
    all_images = []
    for movie in all_movies:
        image = movie.get('image')
        images = str(image)
        all_images.append(images)

    #收藏页的名字和姓名
    user = UserModel.objects.get(id=id)
    name = user.u_name
    y_icons_url = "/static/upload/" + user.u_icon.url
    #获取收藏的电影
    collections = Collections.objects.filter(c_id=id)
    for collection in collections:
        print(collection.c_image)


    return render(request, 'home_logined_collected.html', context=locals())


def set_collect(request, positid, id):
    try:
        #将收藏电影的信息保存到collection数据库
        movie = Movie.objects.get(m_positid=positid)
        collection = Collections()
        collection.c_positid = positid
        collection.c_id = id
        collection.c_image = movie.m_image
        collection.c_duration = movie.m_duration
        collection.c_title = movie.m_title
        collection.save()
    except Exception as e :
        return HttpResponse("收藏失败")
    return HttpResponse("收藏成功")

def del_collect(request, positid):
    try:
        del_movie = Collections.objects.get(c_positid=positid)
        del_movie.delete()
    except Exception as e :
        return HttpResponse("删除收藏失败啊啊 啊啊啊啊啊")
    return HttpResponse("删除收藏成功")




def get_movies_image(url):

    resp = requests.get(url)

    # print(resp.status_code)

    result = resp.json()

    movies = result.get("data")

    # print(movies)

    return movies

def get_movies(url):

    resp = requests.get(url)

    # print(resp.status_code)

    result = resp.json()

    movies = result.get("data")

    return movies

def check_user(request):

    username = request.GET.get("username")
    print(username)

    users = UserModel.objects.filter(u_name=username)

    data = {
        "status": HTTP_OK,
        "msg": 'user can use'
    }

    if users.exists():
        data['status'] = HTTP_USER_EXIST
        data['msg'] = 'user already exist'
    else:
        pass

    return JsonResponse(data=data)


def check_email(request):

    email = request.GET.get("email")

    users = UserModel.objects.filter(u_email=email)

    data = {
        "status": HTTP_OK,
        "msg": 'user can use'
    }

    if users.exists():
        data['status'] = HTTP_USER_EXIST
        data['msg'] = 'user already exist'
    else:
        pass

    return JsonResponse(data=data)


