from rest_framework import serializers

from app.models import Article, ArticleType


class ArticleSerializer(serializers.ModelSerializer):
    """
    实现序列化，序列化的字段由fields来定义
    实现字段校验，默认按照model中指定的Article模型中的定义

    """

    title = serializers.CharField(required=True,
                                  max_length=10,
                                  min_length=3,error_messages={
            'required':'title必填',
            'max_length':'不超过10字符',
            'min_length':'不短于3字符'
        })
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)
        data['type'] = ArticleTypeSerializer(instance.type).data

        return data


class ArticleType2Serializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleType
        fields = '__all__'


class ArticleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleType
        fields = '__all__'

    def to_representation(self, instance):
        # 该方就是进项序列化的方法
        # 实现功能： 对象 ====》dict

        data = super().to_representation(instance)

        # 返回给前段的数据一定是序列化的结果，不能返回对象给前段
        articles = instance.article_set.all()
        data['article'] = ArticleSerializer(articles,many=True).data
        return data
