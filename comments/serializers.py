from rest_framework import serializers


# class Comment(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
#     text = models.TextField()
#     published = models.DateTimeField(auto_now_add=True)
#     parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(source='ticket.title', read_only=True)
    text = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(source='author.username',
                                                read_only=True,
                                                default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def save(self, **kwargs):
        kwargs['author'] = self.fields['author'].get_default()
        kwargs['ticket_id'] = self.context['view'].kwargs['pk']
        return super().save(**kwargs)
