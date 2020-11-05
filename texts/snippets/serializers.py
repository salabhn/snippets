from rest_framework import serializers

from .models import Tag, Snippet


class TagSerializerField(serializers.Field):

    def to_internal_value(self, data):
        tag, created = Tag.objects.get_or_create(title=data)
        return tag


class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializerField(write_only=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'message', 'tag', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']




class TagSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='snippet-detail'
    )

    class Meta:
        model = Tag
        fields = ['id', 'title', 'snippets']
