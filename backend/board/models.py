from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    '''
    게시글
    '''
    title = models.CharField(max_length=200, default='')
    content = models.TextField()
    author = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    '''
    게시글 댓글, 대댓글(use parent)
    '''
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField('생성시간', auto_now_add=True)


class AttachmentFile(models.Model):
    '''
    게시글 파일
    '''
    post = models.ForeignKey(Post, related_name='attachments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='attachments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)