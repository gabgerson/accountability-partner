from rest_framework import generics, permissions
from .serializers import GoalSerializer, StepSerializer
from goals.models import Goal, Step



class GoalList(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permissions = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StepCreate(generics.CreateAPIView):

    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]