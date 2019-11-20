from django.db import models

class ArticleType(models.Model):
    t_name = models.CharField(max_length=10,null=False,unique=True)

    class Meta:
        db_table = 'tb_article_type'


class Article(models.Model):
    title = models.CharField(max_length=50,null=False)
    desc = models.TextField(null=True)
    type = models.ForeignKey(ArticleType,on_delete=models.PROTECT,
                             null=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'tb_article'

