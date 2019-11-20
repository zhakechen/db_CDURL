# 定义一个过滤文件
import django_filters

from app.models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    # 实现过滤
    # 左边的title是地址上的(参数)，右边的title是数据库中需要过滤的title
    # 如果借口中参数的字段和过滤的字段一样，CharFilter中可以不用写过滤字段
    title = django_filters.CharFilter(lookup_expr='icontains')
    # contains,gt,gte,lt,lte

    # 老版本djangorestframework中叫action,行版本中叫method
    is_delete = django_filters.CharFilter(method='filter_is_delete')

    class Meta:
        model = Article
        fields = []


    def filter_is_delete(self,queryset,name,value):

        if value == 'yes':
            return queryset.filter(is_delete=True)
        else:
            return queryset.filter(is_delete=False)

