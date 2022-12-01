from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', views.APIComment.as_view()),
    path(
        'posts/<int:post_id>/comments/<int:comment_id>/',
        views.APICommentDetail.as_view()
    ),
    path('api-token-auth/', obtain_auth_token),
]
