"""accountability_partner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from goals import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    # AUTH
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # GOAL
    path('goals/create', views.CreateGoal.as_view(), name='create_goal'),
    path('goals/<int:pk>', views.DetailGoal.as_view(), name='detail_goal'),
    path('goals/<int:pk>/update', views.UpdateGoal.as_view(), name='update_goal'),
    path('goals/<int:pk>/delete', views.DeleteGoal.as_view(), name='delete_goal'),
    # STEP
    path('goals/<int:pk>/addstep', views.add_step, name='add_step'),
    # TODO: ADD SEARCH STEPS
    path('steps/<int:pk>/deletestep', views.DeleteStep.as_view(), name='delete_step'),
    path('steps/<int:pk>/updatestep', views.UpdateStep.as_view(), name='update_step'),
    
    # API
    path('api/', include('api.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
