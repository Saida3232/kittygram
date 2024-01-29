from django.urls import path,include
#from cats.views import CatDetail,CatList
#from cats.views import APICAT
from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.authtoken import views
# urlpatterns = [
#    path('cats/', cat_list),
#    path('cats/<int:id>/',detail_cat),
# ]
# urlpatterns = [
#     path('cats/',APICAT.as_view()),
# ]

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
