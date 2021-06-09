from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Main Goals App
class Goal(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Step(models.Model):
    title = models.CharField(max_length=255)
    progress = models.TextField(default='In Progress')
    done = models.BooleanField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now())
    deadline = models.DateTimeField(null=True)

  
# Blog
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')