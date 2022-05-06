from rest_framework import serializers

from tickets.models import Ticket


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]


class UserTaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = ChoiceField(choices=Ticket.CHOICES, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def save(self, **kwargs):
        kwargs['author'] = self.fields['author'].get_default()
        return super().save(**kwargs)


class SupportTaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    text = serializers.CharField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        source='author.username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    status = ChoiceField(choices=Ticket.CHOICES)

    class Meta:
        model = Ticket
        fields = '__all__'
