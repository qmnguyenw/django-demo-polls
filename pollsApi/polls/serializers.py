from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from .models import Poll, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # don’t want to get back the password in response which we ensure using extra_kwargs = {'password': {'write_only': True}}
        extra_kwargs = {'password': {'write_only': True}}

    # overriden the ModelSerializer method’s create() to save the User instances
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        # set the password correctly using user.set_password, rather than setting the raw password as the hash
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user) # ensure that tokens are created when user is created in UserCreate view
        return user