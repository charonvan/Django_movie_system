from django.conf.urls import url

from movie import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^home/', views.home, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^userinfo_mod/(\d+)/', views.userinfo_mod, name='userinfo_mod'),
    url(r'^change/(\d+)/', views.change, name='change'),
    url(r'^collect/(\d+)/', views.collect, name='collect'),
    url(r'^set_collect/(\d+)/(\d+)/', views.set_collect, name='set_collect'),
    url(r'^del_collect/(\d+)/', views.del_collect, name='del_collect'),
    url(r'^checkuser/', views.check_user, name='check_user'),
    url(r'^checkemail/', views.check_email, name='check_email'),
]