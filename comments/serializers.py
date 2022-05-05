from rest_framework import serializers


# class Comment(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
#     text = models.TextField()
#     published = models.DateTimeField(auto_now_add=True)
#     parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()

    class Meta:
        model = Comment
        fields = '__all__'
