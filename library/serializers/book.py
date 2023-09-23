from rest_framework import serializers

from library.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1, read_only=True)
    title = serializers.CharField(max_length=255)
    likes = serializers.IntegerField(min_value=0)
    author_id = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)
