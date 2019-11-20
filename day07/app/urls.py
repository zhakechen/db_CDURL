from rest_framework.routers import SimpleRouter

from app.views import ArticleView,TypeView
# 配置路由，先定义模型
# 1.生成路由对象，路由对象可以用于管理路由地址
router = SimpleRouter()
# 2.注册资源
router.register('article',ArticleView)
router.register('type',TypeView)
urlpatterns = [

]

# 3.通过router.urls获取自动生成的地址
urlpatterns += router.urls