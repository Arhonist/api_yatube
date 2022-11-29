from django.urls import include, path

from rest_framework.routers import DefaultRouter

from views import PostView, GroupView, CommentView

app_name = 'api'

router = DefaultRouter()
router.register('')