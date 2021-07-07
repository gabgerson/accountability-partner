from django.urls import path
from . import views

urlpatterns = [
    # Goals
    path('goals/<int:pk>', views.GoalRetrieveUpdateDestroy.as_view()),
    path('goals', views.GoalListCreate.as_view()),

    # Steps
    path('goals/<int:pk>/steps', views.StepListCreate.as_view()),
    path('steps/<int:pk>', views.StepRetreiveUpdateDestroy.as_view()),

    # Auth
    path('signup', views.UserCreate.as_view(), name='create_user'),
    path('logout/blacklist', views.BlacklistTokenView.as_view(), name='blacklist')

    
]