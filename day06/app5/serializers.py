from rest_framework import serializers

from app5.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['title','desc']
