

from django.core.management.base import BaseCommand
from octofit_tracker.models import UserProfile, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name="Marvel", description="Team Marvel")
        dc = Team.objects.create(name="DC", description="Team DC")

        # Create users (superheroes)
        spiderman = UserProfile.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=marvel.name)
        ironman = UserProfile.objects.create(name="Iron Man", email="ironman@marvel.com", team=marvel.name)
        batman = UserProfile.objects.create(name="Batman", email="batman@dc.com", team=dc.name)
        wonderwoman = UserProfile.objects.create(name="Wonder Woman", email="wonderwoman@dc.com", team=dc.name)

        # Create activities
        Activity.objects.create(user=spiderman.name, activity="Running", duration=30)
        Activity.objects.create(user=ironman.name, activity="Cycling", duration=45)
        Activity.objects.create(user=batman.name, activity="Swimming", duration=25)
        Activity.objects.create(user=wonderwoman.name, activity="Yoga", duration=60)

        # Create leaderboard
        Leaderboard.objects.create(user=spiderman.name, points=100)
        Leaderboard.objects.create(user=ironman.name, points=90)
        Leaderboard.objects.create(user=batman.name, points=95)
        Leaderboard.objects.create(user=wonderwoman.name, points=110)

        # Create workouts
        Workout.objects.create(user=spiderman.name, workout="Pushups", reps=50)
        Workout.objects.create(user=ironman.name, workout="Situps", reps=40)
        Workout.objects.create(user=batman.name, workout="Pullups", reps=30)
        Workout.objects.create(user=wonderwoman.name, workout="Squats", reps=60)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data (Django ORM).'))
