from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from random import randint

from django.utils.crypto import get_random_string


class Command(BaseCommand):
    User = get_user_model()

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        User = get_user_model()
        if 1 < int(options.get('count')) < 10:
            for i in range(options.get('count')):
                a = randint(99, 98989898)
                username = get_random_string(10)
                user = User(username=username, email='email'+str(a)+'@ex.com', password='Pas1231'+str(a))
                user.save()
        else:
            raise CommandError("Invalid count!")

