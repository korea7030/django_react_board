from rest_framework import serializers
from .models import Post, Comment, AttachmentFile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'hit', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('post', 'id', 'user', 'parent', 'comment', 'created_at','reply')
        read_only_fields = ['user']

    def get_reply(self, obj):
        serializer = self.__class__(obj.reply, many=True)
        serializer.bind('', self)
        return serializer.data


class PostCommentSerializer(serializers.ModelSerializer):
    parent_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'parent_comments')

    def get_parent_comments(self, obj):
        parent_comments = obj.comments.filter(parent=None)
        serializer = CommentSerializer(parent_comments, many=True)
        return serializer.data


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentFile
        fields = ('id', 'post', 'user', 'created_at')
        read_only_fields = ['user']


class PostAttachmentSerializer(serializers.ModelSerializer):
    attachment = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'attachment')

    def get_attachment(self, obj):
        attachments = obj.attachments.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return serializer.data