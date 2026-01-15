from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, LeaderboardEntry, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Create users
        user1, _ = User.objects.get_or_create(username='alice', email='alice@example.com')
        user2, _ = User.objects.get_or_create(username='bob', email='bob@example.com')

        # Create teams
        team1, _ = Team.objects.get_or_create(name='Team Alpha')
        team2, _ = Team.objects.get_or_create(name='Team Beta')

        # Assign users to teams (if applicable)
        if hasattr(team1, 'members'):
            team1.members.add(user1)
        if hasattr(team2, 'members'):
            team2.members.add(user2)

        # Create activities
        Activity.objects.get_or_create(user=user1, type='Running', duration=30, calories=250)
        Activity.objects.get_or_create(user=user2, type='Cycling', duration=45, calories=400)

        # Create leaderboard entries
        LeaderboardEntry.objects.get_or_create(user=user1, team=team1, points=100)
        LeaderboardEntry.objects.get_or_create(user=user2, team=team2, points=120)

        # Create workouts
        Workout.objects.get_or_create(name='Morning Cardio', description='A quick cardio session', duration=20)
        Workout.objects.get_or_create(name='Strength Training', description='Full body workout', duration=40)

        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
