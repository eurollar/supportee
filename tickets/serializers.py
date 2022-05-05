from rest_framework import serializers

from tickets.models import Ticket


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]


# class CurrentUserDefault(serializers.CurrentUserDefault):
#
#     def __call__(self, serializer_field):
#         return serializer_field.context['request'].user.id


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        source='author.username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = ChoiceField(choices=Ticket.CHOICES, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def save(self, **kwargs):
        kwargs['author'] = self.fields['author'].get_default()
        return super().save(**kwargs)


class UserTaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = ChoiceField(choices=Ticket.CHOICES, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


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
