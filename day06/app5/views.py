from rest_framework import  mixins,viewsets


# 继承六个父类
from rest_framework.response import Response

from app5.models import Article
from app5.serializers import ArticleSerializer


class ArticleView(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,    # 展示
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,  # 删除
                  mixins.UpdateModelMixin):  # 更新

    queryset = Article.objects.all()   # 获取所有文章内容

    serializer_class = ArticleSerializer   # 序列化

    def list(self, request, *args, **kwargs):

        # get_queryset()拿的是上面的方法默认返回Article.object.all()
        # queryset = self.get_queryset()
        queryset = self.queryset    # 同上句意思一样


        # get_serializer()默认返回ArtileSerializer
        # 实现将queryset中的每一个对象转化为dict
        # serializer = self.get_serializer(queryset,many=True)
        serializer = ArticleSerializer(queryset,many=True)   # 同上句意思一样

        return Response(serializer.data)



    def reate(self,request,*args,**kwargs):
        # 接收post请求传递参数 request.data
        data = request.data
        # 将获取到的参数丢给ArticleSerializer进行字段校验
        serializer = self.get_serializer(data=data)
        # is_valid()校验成功还是失败
        result = serializer.is_valid()
        if result:
            # 保存成功
            serializer.save()
            return Response(serializer.data)
        else:
            errors = serializer.errors
            return Response({'msg':'保存失败'})

