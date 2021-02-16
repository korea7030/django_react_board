from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'view/comment', views.PostCommentViewSet)


urlpatterns = [
    path('', include(router.urls))
]