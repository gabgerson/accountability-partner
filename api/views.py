from rest_framework import generics, permissions, mixins, status
from .serializers import GoalSerializer, StepSerializer
from rest_framework.exceptions import ValidationError
from .permissions import IsOwnerOrReadOnly
from goals.models import Goal, Step



class GoalListCreate(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes =[permissions.IsAuthenticated, IsOwnerOrReadOnly]

    # def delete(self, request, *args, **kwargs):
    #     goal = Goal.objects.filter(pk=kwargs['pk'], user=self.request.user)
    #     if goal.exists():
    #         return self.destroy(request, *args, **kwargs)
    #     else:

    #         raise ValidationError('You isn\'t your goal to delete.')

class StepListCreate(generics.ListCreateAPIView):

    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        goal = Goal.objects.get(pk=self.kwargs['pk'])
        return Step.objects.filter(goal=goal)

    def perform_create(self, serializer):
        # serializer.instance.date_created = timezone.now()
        serializer.save(goal=Goal.objects.get(pk=self.kwargs['pk']), user = self.request.user)
    

class StepRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):


    serializer_class = StepSerializer
    permission_classes =[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        user = self.request.user

        return Step.objects.filter(id=self.kwargs['pk'])

    # def delete(self, request, *args, **kwargs):
    #     step = Step.objects.filter(pk=kwargs['pk'])
    #     print(step[0].goal.id)
    #     goal_pk = step[0].goal.id
    #     # print(goal_pk)
    #     goal = Goal.objects.filter(pk=goal_pk, user = self.request.user)


    #     if goal.exists():
    #         if step.exists():
    #             return self.destroy(request, *args, **kwargs)
    #     else:

    #         raise ValidationError('You isn\'t your goal to delete.')

