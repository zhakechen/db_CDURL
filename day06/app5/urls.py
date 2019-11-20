
from rest_framework.routers import SimpleRouter



# 获取路由对象
from app5.views import ArticleView

router = SimpleRouter()
# 注册资源，自动生成了一些接口地址
# 、/app5/article/  /app5/article/[id]/
router.register('article',ArticleView)

urlpatterns =[

]

# 将自动生成的接口地址添加到django能解析到urlpatternes变量上
urlpatterns += router.urls