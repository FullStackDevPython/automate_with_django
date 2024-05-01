from django.core.management.base import BaseCommand, CommandParser
#proposed command = python manage.py greeting Shashank
#proposed output = Good Morning {name}
class Command(BaseCommand):
    help = "It greets the user"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Specifies user name")

    def handle(self, *args, **kwargs):
        #it greets the user
        name = kwargs["name"]
        greeting = f"Good Morning {name}"
        self.stdout.write(greeting)
        self.stderr.write(greeting)
        self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(self.style.WARNING(greeting))