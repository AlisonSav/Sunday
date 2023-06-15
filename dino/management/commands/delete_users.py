from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    User = get_user_model()

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        User = get_user_model()
        for id in options['user_ids']:
            if User.objects.filter(pk=id).filter(is_superuser=1):
                raise CommandError("You can't delete superuser")
            else:
                try:
                    user = User.objects.get(pk=id)
                    user.delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'User {id} deleted with success!'))
                except User.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'User with id {id} does not exist.'))
