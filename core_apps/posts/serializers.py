from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from rest_framework import serializers
from taggit.models import Tag
from taggit.serializers import TagListSerializerField, TaggitSerializer
from core_apps.commons.models import ContentView
from core_apps.posts.models import Post, Reply


User = get_user_model()


class PopularTagSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ["name", "slug", "post_count"]


class TopPostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    replies_count = serializers.IntegerField(read_only=True)
    view_count = serializers.IntegerField(read_only=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "author_username",
            "upvotes",
            "view_count",
            "replies_count",
            "avatar",
            "created_at",
        ]

    def get_avatar(self, obj) -> str | None:
        if obj.author.profile.avatar:
            return obj.author.profile.avatar.url
        return None


class ReplySerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = [
            "id",
            "post",
            "author_username",
            "body",
            "avatar",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "author_username",
            "created_at",
            "updated_at",
        ]

    def get_avatar(self, obj) -> str | None:
        if obj.author.profile.avatar:
            return obj.author.profile.avatar.url
        return None


class UpvotePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = []

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user not in instance.upvoted_by.all():
            instance.upvoted_by.add(user)
            instance.upvotes += 1
            instance.save()
        return instance


class DownvotePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = []

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user in instance.upvoted_by.all():
            instance.upvoted_by.remove(user)
            instance.upvotes = F("upvotes") - 1
        if user not in instance.downvoted_by.all():
            instance.downvoted_by.add(user)
            instance.downvotes = F("upvotes") + 1
        else:
            instance.downvoted_by.remove(user)
            instance.downvotes = F("downvotes") - 1

        instance.save()
        instance.refresh_from_db()

        return instance
