from django.db import models

class UserModel(models.Model):
    u_name = models.CharField(max_length=16, null=True, unique=True)
    # upload_to 相对路径，  相对于的是MEDIA_ROOT  媒体根目录
    u_icon = models.ImageField(upload_to='%Y/%m/%d/icons')
    u_password = models.CharField(max_length=16)
    u_email = models.CharField(max_length=25)

class Collections(models.Model):
    c_id = models.IntegerField(max_length=64)
    c_positid = models.CharField(max_length=7, unique=True)
    c_title = models.CharField(max_length=50)
    c_image = models.CharField(max_length=200)
    c_duration = models.CharField(max_length=100)



class Movie(models.Model):
    m_positid = models.CharField(max_length=7, unique=True)
    m_title = models.CharField(max_length=50)
    m_image = models.CharField(max_length=200)
    m_duration = models.CharField(max_length=100)
    m_appfutitle = models.CharField(max_length=200, null=True)
