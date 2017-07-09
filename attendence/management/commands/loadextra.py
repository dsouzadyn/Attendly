from django.core.management.base import BaseCommand, CommandError
import csv
from attendence.models import *
import os

class Command(BaseCommand):
    help = 'Imports attendance data'

    def add_arguments(self, parser):
        parser.add_argument('subject_abbr', type=str)
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        subject_abbr = options['subject_abbr']
        cwd = os.getcwd()
        cwd += '/csvs'
        file_path = cwd + '/' + options['file_name']

        with open(file_path, newline='') as csvfile:
            attreader = list(csv.reader(csvfile))
            max_data = attreader.pop(1)
            max_data = [int(x) for x in max_data[1:]]
            max_data = sum(max_data)
            print(max_data)
            attreader.pop(0)

            subject = Subject.objects.filter(abbr=subject_abbr)[0]
            if subject_abbr == 'EXT':
                for row in attreader:
                    try:
                        attendance = Attendance.objects.filter(student__roll_no=row[0])[0]
                    except:
                        print(row[0])

                    ss = SubjectStudent.objects.filter(attendance=attendance, subject=subject)
                    if len(ss) == 0:
                        ss = SubjectStudent(attendance=attendance, subject=subject)
                        ss.save()
                    else:
                        ss = ss[0]
                    if subject.sub_type == 5:
                        act = [int(e) for e in row[1:]]
                        act = sum(act)
                        th = Theory.objects.filter(subject_student=ss)
                        if len(th) == 0:
                            th = Theory(subject_student=ss, actual=act, total=max_data)
                            th.save()
                        pr = Practical.objects.filter(subject_student=ss)
                        if len(pr) == 0:
                            pr = Practical(subject_student=ss, actual=0, total=0)
                            pr.save()
                    else:
                        pass
                    self.stdout.write(self.style.SUCCESS(
                        'SUCCESS!'
                    ))
            else:
                self.stdout.write(self.style.ERROR(
                    'This is only used for adding extra attendance!'
                ))