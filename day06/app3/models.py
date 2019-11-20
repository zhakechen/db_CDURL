from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=10,unique=True,null=False)
    password = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_user'


class UserToken(models.Model):

    token = models.CharField(max_length=50,unique=True,null=False)
    # 级联删除CASCADE
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    timeout = models.DateTimeField(null=False)


    class Meta:
        db_table = 'tb_user_token'


class UserImage(models.Model):
    # upload_to 将图片存下来
    images = models.ImageField(upload_to='images')

    class Meta:
        db_table = 'tb_user_images'
