from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Django commands to wait for the database to be available."

    def handle(self, *args, **options):
        pass

    #     self.stdout.write('Waiting for the database...')
    #     retries = 20
    #     while retries:FF
    #         try:
    #             self.check_database_connection()
    #             self.stdout.write(self.style.SUCCESS('Database available!'))
    #             break
    #         except Exception as e:
    #             self.stdout.write(self.style.WARNING(str(e)))
    #             retries -= 1
    #             sleep(1)
    #
    #     if retries == 0:
    #         self.stdout.write(self.style.ERROR('Unable to connect to the database.'))
    #
    # def check_database_connection(self):
    #     # Place your database connection code here
    #     # Replace this with your actual database connection code
    #     # For example, you can use Django's database connection wrapper:
    #     from django.db import connections
    #     connections['default'].cursor()
