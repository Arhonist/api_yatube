from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views # , GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
