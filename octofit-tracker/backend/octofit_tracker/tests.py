from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        activity = Activity.objects.create(name='Run', user=user, duration=30)
        self.assertEqual(activity.name, 'Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')
        team = Team.objects.create(name='Test Team 2')
        leaderboard = Leaderboard.objects.create(user=user, team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username='testuser4', email='test4@example.com', password='testpass')
        workout = Workout.objects.create(name='Chest Day', description='Bench press', user=user)
        self.assertEqual(workout.name, 'Chest Day')
