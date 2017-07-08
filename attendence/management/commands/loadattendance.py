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
            attreader.pop(0)
            self.stdout.write(self.style.SUCCESS(' '.join(max_data)))
            subject = Subject.objects.filter(abbr=subject_abbr)[0]
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
                if subject.sub_type == 4:
                    th = Theory.objects.filter(subject_student=ss)
                    if len(th) == 0 and int(row[1]) != 0 and int(row[2]) != 0:
                        th = Theory(subject_student=ss, actual=row[1], total=max_data[1])
                        th.save()
                    pr = Practical.objects.filter(subject_student=ss)
                    if len(pr) == 0 and int(row[1]) != 0 and int(row[2]) != 0:
                        pr = Practical(subject_student=ss, actual=row[2], total=max_data[2])
                        pr.save()
                    else:
                        th = Theory(subject_student=ss, actual=0, total=0)
                        th.save()
                        pr = Practical(subject_student=ss, actual=0, total=0)
                        pr.save()
                if subject.sub_type == 1:
                    th = Theory.objects.filter(subject_student=ss)
                    if len(th) == 0:
                        th = Theory(subject_student=ss, actual=row[1], total=max_data[1])
                        th.save()
                    pr = Practical.objects.filter(subject_student=ss)
                    if len(pr) == 0:
                        pr = Practical(subject_student=ss, actual=row[2], total=max_data[2])
                        pr.save()
                elif subject.sub_type == 2:
                    th = Theory.objects.filter(subject_student=ss)
                    if len(th) == 0:
                        th = Theory(subject_student=ss, actual=row[1], total=max_data[1])
                        th.save()
                    pr = Practical.objects.filter(subject_student=ss)
                    if len(pr) == 0:
                        pr = Practical(subject_student=ss, actual=0, total=0)
                        pr.save()
                elif subject.sub_type == 3:
                    th = Theory.objects.filter(subject_student=ss)
                    if len(th) == 0:
                        th = Theory(subject_student=ss, actual=0, total=0)
                        th.save()
                    pr = Practical.objects.filter(subject_student=ss)
                    if len(pr) == 0:
                        pr = Practical(subject_student=ss, actual=row[2], total=row[2])
                        pr.save()
                else:
                    pass
                self.stdout.write(self.style.SUCCESS(
                    'SUCCESS!'
                ))