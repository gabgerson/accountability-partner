from rest_framework import serializers
from goals.models import Goal, Step
from django.contrib.auth.models import User

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        read_only_fields = ['goal', 'date_created']
        fields = ['id', 'title', 'progress', 'done', 'goal', 'date_created', 'deadline']



class GoalSerializer(serializers.ModelSerializer):

    # step_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Step.objects.all())
    step_set = StepSerializer(many=True, read_only=True)
    # steps = serializers.StringRelatedField(many=True)

    class Meta:
        model = Goal
        fields = ['id', 'title','step_set']



class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

 