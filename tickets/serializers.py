from rest_framework import serializers

from comments.models import Comment
from comments.serializers import CommentSerializer
from tickets.models import Ticket


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]

"""
class UserTaskSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = ChoiceField(choices=Ticket.CHOICES, read_only=True)
    # comments = CommentSerializer()

    class Meta:
        model = Ticket
        fields = ('id', 'status', 'title', 'create')

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def save(self, **kwargs):
        kwargs['author'] = self.fields['author'].get_default()
        return super().save(**kwargs)


class SupportTaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    # text = serializers.CharField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        source='author.username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    status = ChoiceField(choices=Ticket.CHOICES)

    class Meta:
        model = Ticket
        fields = ('id', 'status', 'title', 'author', 'create')
"""


# NEW serializers
class UserTicketList(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(write_only=True)
    status = ChoiceField(choices=Ticket.CHOICES, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def save(self, **kwargs):
        kwargs['author'] = self.fields['author'].get_default()
        return super().save(**kwargs)


class UserTicketDetail(serializers.ModelSerializer):
    status = ChoiceField(choices=Ticket.CHOICES, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        exclude = ('author',)


class SupportTicketList(serializers.ModelSerializer):
    status = ChoiceField(choices=Ticket.CHOICES)
    author = serializers.PrimaryKeyRelatedField(
        source='author.username',
        read_only=True
    )

    class Meta:
        model = Ticket
        fields = '__all__'


class SupportTicketDetail(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    text = serializers.CharField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        source='author.username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    status = ChoiceField(choices=Ticket.CHOICES)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'text', 'author', 'status', 'create', 'comments')
