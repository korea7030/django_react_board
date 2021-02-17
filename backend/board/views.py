from rest_framework import viewsets, permissions
from rest_framework.response import Response

from accounts.models import CustomUser
from .serializers import (
    PostSerializer, 
    CommentSerializer, 
    PostCommentSerializer, 
    AttachmentSerializer, 
    PostAttachmentSerializer
)
from .models import Post, Comment, AttachmentFile
from .permissions import IsPostOwnerOrReadOnly, IsCommentOwnerOrReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostOwnerOrReadOnly]

    def perform_create(self, serializer):
        # frontend 구현시 고쳐야 할 부분
        data = self.request.data
        author = data.get('author', None)
        
        if author is not None:
            user = CustomUser.objects.get(pk=author)
            serializer.save(author=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit = instance.hit + 1
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]

    def perform_create(self, serializer):
        # frontend 구현시 고쳐야 할 부분
        data = self.request.data
        user = data.get('user', None)
        
        if user is not None:
            user_pk = CustomUser.objects.get(pk=user)
            serializer.save(user=user_pk)


class PostCommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.AllowAny]


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = AttachmentFile.objects.all()
    serializer_class = AttachmentSerializer

    def perform_create(self, serializer):
        # frontend 구현시 고쳐야 할 부분
        data = self.request.data
        user = data.get('user', None)
        
        if user is not None:
            user_pk = CustomUser.objects.get(pk=user)
            serializer.save(user=user_pk)


class PostAttachmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostAttachmentSerializer