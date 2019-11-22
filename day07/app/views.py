from rest_framework import mixins,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.filters import ArticleFilter
from app.models import Article, ArticleType
from app.serializer import ArticleSerializer, ArticleTypeSerializer


class ArticleView(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,    # POST请求/app/article/
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,    #Delete /app/article/[id]
                  mixins.UpdateModelMixin,    #PUT/PATCH/app/article/
                  mixins.RetrieveModelMixin):      # GET/app/article/
    # queryset参数默认为路由注册资源所对应的表的所有数据
    # queryset = Article.objects.all().filter(is_delete=False)
    queryset = Article.objects.all()

    # def list(self, request, *args, **kwargs):
    #
    #     # 1.获取接口中的传递参数
    #     title = request.query_params.get('title')
    #     if title:
    #         queryset = self.get_queryset().filter(title__contains=title)
    #         # 2.序列化
    #     else:
    #         queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset,many=True)
    #
    #     return Response(serializer.data)

    filter_class = ArticleFilter

    # def get_queryset(self):
    #     return self.queryset.filter(is_delete=False)


    # 序列化/字段校验
    serializer_class = ArticleSerializer


    def retrieve(self,request,*args,**kwargs):
        # 1.获取对象
        instance = Article.objects.filter(pk=kwargs['pk']).first()
        instance = self.get_object()
        # 2.序列化
        serializer = ArticleSerializer(instance)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 假删除
        instance.is_delete = True
        # 真删除
        # instance.delete()
        instance.save()
        return Response({'msg':'删除成功'})

    def update(self, request, *args, **kwargs):

        # 1.获取对象
        instance = self.get_object()
        # 2.获取修改的参数
        data = request.data
        # 3.参数校验
        serializer = self.get_serializer(instance,data=data)
        # raise_exception=True,如果is-valid校验失败，直接抛异常
        serializer.is_valid(raise_exception=True)
        #
        serializer.save()
        return Response({'message':'更新成功'})


class TypeView(viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               mixins.CreateModelMixin):

    queryset = ArticleType.objects.all()


    serializer_class = ArticleTypeSerializer

    # 装饰器action装饰方法，装饰器中的detail的参数为False时，表示的是xxx/action函数名将作为接口的一部分
    #                                         True时，表示的是xxx/pk/action是否为单一
    # @action(detail=False) 等于@list_route()
    # @action(detail=True)  等于@detail_route()

    @action(detail=False,methods=['POST','GET'])
    def article(self,request):
        # 请求方式
        # 请求地址/app/type/article/
        """
            返回json结构[
            {
                id:'',
                t_name:'',
                articles:[
                    {},{}
                ]
            }
            ]
        """
        queryset = self.get_queryset()

        seriazlizer = self.get_serializer(queryset,many=True)
        return Response(seriazlizer.data)


    @action(detail=True)     #查看指定的
    def articles(self,request,pk):

        # 请求地址 /app/type/[id]/article
        # 请求方式 GET
        instance = self.get_object()
        seriazlizer = self.get_serializer(instance)
        return Response(seriazlizer.data)