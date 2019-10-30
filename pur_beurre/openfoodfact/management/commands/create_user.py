from django.core.management.base import BaseCommand, CommandError
from ...init_db import OpenFoodFacts


op = OpenFoodFacts()

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **kwargs):
        op.create_user()