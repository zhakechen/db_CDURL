from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=10,null=False)
    desc = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_artcile'
