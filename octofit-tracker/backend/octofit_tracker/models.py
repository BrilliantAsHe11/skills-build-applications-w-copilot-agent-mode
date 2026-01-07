from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} - {self.team.name}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.user.username}"