from rest_framework import serializers
from goals.models import Goal, Step

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['title', 'progress', 'done', 'goal']



class GoalSerializer(serializers.ModelSerializer):

    # step_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Step.objects.all())
    step_set = StepSerializer(many=True, read_only=True)
    # steps = serializers.StringRelatedField(many=True)
    print(step_set)
    class Meta:
        model = Goal
        fields = ['id', 'title','step_set']

