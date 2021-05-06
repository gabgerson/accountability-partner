from django.urls import path
from . import views

urlpatterns = [
    # Todos
    path('goals/<int:pk>/steps', views.StepCreate.as_view()),
        path('steps/<int:pk>', views.StepRetreiveUpdateDestroy.as_view(), name='delete_step'),
    path('goals/<int:pk>', views.GoalRetrieveUpdateDestroy.as_view()),
    # path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('goals', views.GoalList.as_view()),

    # Auth
    # path('signup', views.signup),
    # path('login', views.login),
    
]