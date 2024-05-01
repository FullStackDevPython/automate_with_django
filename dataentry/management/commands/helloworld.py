from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "It Prints Hello World"

    def handle(self, *args, **kwargs):
        #this is to print hello world

        self.stdout.write("Hello World")