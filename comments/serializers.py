from rest_framework import serializers

from comments.models import Comment


class CustomForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Comment.objects.filter(ticket_id=self.context['request'].parser_context['kwargs']['pk'])


class CommentSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(source='ticket.title', read_only=True)
    text = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(source='author.username',
                                                read_only=True,
                                                default=serializers.CurrentUserDefault())
    parent = CustomForeignKey(allow_null=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def save(self, **kwargs):
        kwargs['author'] = self.fields['author'].get_default()
        kwargs['ticket_id'] = self.context['view'].kwargs['pk']
        return super().save(**kwargs)
