from django.core.management.base import BaseCommand, CommandError
import csv
from attendence.models import *
import os


class Command(BaseCommand):
    help = 'Update batch data'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        cwd = os.getcwd()
        cwd += '/csvs'
        file_path = cwd + '/' + options['file_name']

        with open(file_path, newline='') as csvfile:
            attreader = list(csv.reader(csvfile))
            attreader.pop(0)
            for row in attreader:
                try:
                    attendance = Attendance.objects.get(student__roll_no=row[0])
                    attendance.batch_no = row[1]
                    attendance.save()
                except:
                    print(row[0])
                self.stdout.write(self.style.SUCCESS(
                    'SUCCESS!'
                ))