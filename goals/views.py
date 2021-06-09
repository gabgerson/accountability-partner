from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Goal, Step
from django.contrib.auth import authenticate, login
from .forms import StepForm, SearchForm
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
# import requests

def home(request):
    return render(request, 'goals/home.html')

@login_required
def dashboard(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/dashboard.html',{'goals':goals})

@login_required
def add_step(request, pk):
    form = StepForm
#     search_form = SearchForm()
    goal = Goal.objects.get(pk=pk)
    if not goal.user == request.user:
        raise Http404
    
    if request.method == 'POST':
        #CREATE
        form = StepForm(request.POST)
        if form.is_valid():
            step = Step()
            step.goal = goal
            step.title = form.cleaned_data['title']
            step.deadline = form.cleaned_data['deadline']
            step.user = request.user
            step.progress = form.cleaned_data['progress']
            step.done = form.cleaned_data['done']
            step.save()
            return redirect('detail_goal', pk)

    return render(request, 'goals/add_step.html', {'form': form, 'goal': goal})


class UpdateStep(LoginRequiredMixin, generic.UpdateView):
    model = Step
    template_name = 'goals/update_step.html'
    fields = ['title', 'progress', 'done', 'deadline']
    success_url = reverse_lazy('dashboard')


    def get_object(self):
        step = super(UpdateStep, self).get_object()
        print(step.goal.user.id)
        if not step.goal.user == self.request.user:
            raise Http404
        return step

class DeleteStep(LoginRequiredMixin, generic.DeleteView):
    model = Step
    template_name = 'goals/delete_step.html'
    success_url = reverse_lazy('dashboard')
    
    def get_object(self):
        step = super(DeleteStep, self).get_object()
        if step.done == True:
            step.done = 'Yes'
        else:
            step.done = 'No'
        if not step.goal.user == self.request.user:
            raise Http404
        return step

class SignUp(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

class CreateGoal(LoginRequiredMixin, generic.CreateView):
    model = Goal
    fields = ['title']
    template_name = 'goals/create_goal.html'
    success_url = reverse_lazy('dashboard')


    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateGoal, self).form_valid(form)
        return redirect('dashboard')


class DetailGoal(generic.DetailView):
    model = Goal
    template_name = 'goals/detail_goal.html'

class UpdateGoal(LoginRequiredMixin, generic.UpdateView):
    model = Goal
    template_name = 'goals/update_goal.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')


    def get_object(self):
        goal = super(UpdateGoal, self).get_object()
        if not goal.user == self.request.user:
            raise Http404
        return goal

class DeleteGoal(LoginRequiredMixin, generic.DeleteView):
    model = Goal
    template_name = 'goals/delete_goal.html'
    success_url = reverse_lazy('dashboard')
    
    def get_object(self):
        goal = super(DeleteGoal, self).get_object()
        if not goal.user == self.request.user:
            raise Http404
        return goal