from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'A django command for saying hello to users!'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-n', '--name', default='Akbar', help='Enter your name please')

    def handle(self, *args, **options):
        name = options['name']
        if name == 'Arman':
            raise CommandError("Ma be arman salam nemikonim!")

        print(self.style.WARNING(f"Hello {name}"))