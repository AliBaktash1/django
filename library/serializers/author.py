from django.utils import timezone

from rest_framework import serializers

from library.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    life = serializers.SerializerMethodField()

    class Meta:
        model = Author
        read_only_fields = ('id', 'created', 'updated')
        fields = [
            "id", "created", "full_name", "updated", "life", "short_name"
        ]

    @staticmethod
    def get_life(author: Author):
        return timezone.now() - author.created

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['now'] = timezone.now()
        return data
