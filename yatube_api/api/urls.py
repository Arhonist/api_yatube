from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register(r'posts', views.PostViewSet)
v1_router.register(r'groups', views.GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
