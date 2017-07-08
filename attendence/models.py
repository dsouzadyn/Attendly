from django.db import models


class Student(models.Model):
    """
    Student table to indicate the information of each student
    """
    branches = (
        (1, 'Computer Engineering'),
        (2, 'Mechanical Engineering'),
        (3, 'Electrical Engineering'),
        (4, 'Information Technology'),
        (5, 'EXTC'),
    )
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    branch = models.IntegerField(choices=branches)
    semester = models.IntegerField()
    roll_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.roll_no)


class Attendance(models.Model):
    """
    Attendance table to indicate the attendence of each student in each subject
    """
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, related_name='student')
    batch_no = models.IntegerField()

    def __str__(self):
        return str(self.student.roll_no)


class Subject(models.Model):
    subject_name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=30)
    sub_type = models.IntegerField()

    def __str__(self):
        return str(self.subject_name)


class SubjectStudent(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, related_name='subs', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.attendance.student.roll_no) + ' ' + self.subject.subject_name


class Theory(models.Model):
    subject_student = models.ForeignKey(SubjectStudent, related_name='theory', on_delete=models.CASCADE)
    actual = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.subject_student)


class Practical(models.Model):
    subject_student = models.ForeignKey(SubjectStudent, related_name='practical', on_delete=models.CASCADE)
    actual = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.subject_student)


class SubjectHolder(models.Model):
    """
    Table which contains each semester subject names
    """
    branches = (
        (1, 'Computer Engineering'),
        (2, 'Mechanical Engineering'),
        (3, 'Electrical Engineering'),
        (4, 'Information Technology'),
        (5, 'EXTC'),
    )

    created = models.DateTimeField(auto_now_add=True)
    branch = models.IntegerField(choices=branches)
    semester = models.IntegerField()
    subject = models.ForeignKey(Subject, related_name='subject')

    def __str__(self):
        return str(self.subject)
