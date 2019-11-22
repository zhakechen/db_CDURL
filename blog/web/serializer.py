"""实现序列化，需要在相关app下创建新的py文件"""

from rest_framework import serializers
from web.models import ArticleType ,BlogIndex

class ArticleSerializer(serializers.ModelSerializer):

    blog_index_stitle = serializers.CharField(required=True,
                                              max_length=10,
                                              min_length=3,
                                              error_messages={
                                                  'required':'stitle必填',
                                                  'max_length':'不超过10字符',
                                                  'min_length':'不短于3字符'
                                              })
    class Meta:
        model = BlogIndex
        fields = '__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)
        return data



