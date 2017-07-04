from attendence.serializers import *
from rest_framework import generics
from datetime import datetime


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save()


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectHolderList(generics.ListCreateAPIView):
    serializer_class = SubjectHolderSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):

        semester = self.kwargs['semester']
        branch = self.kwargs['branch']
        return SubjectHolder.objects.filter(branch=branch, semester=semester)

#
# class SubjectCountList(generics.ListAPIView):
#     serializer_class = SubjectHolderSerializer
#
#     def get_queryset(self):
#         semester = self.kwargs['semester']
#         return SubjectHolder.objects.filter(semester=semester)


# class SubjectHolderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SubjectHolder.objects.all()
#     serializer_class = SubjectHolderSerializer
#
#     def get_queryset(self):
#         semester = self.kwargs['semester']
#         pid = self.kwargs['pk']
#         print(semester)
#         print(pid)
#         return SubjectHolder.objects.filter(id=pid)


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.order_by('+subject_name').all()
    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        serializer.save()



class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class AttendanceList(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer


    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        today = datetime.today()
        datem = datetime(today.year, today.month, 1)
        semester = None
        branch = None
        queryset = Attendance.objects.all()
        if len(self.kwargs) > 0:
            branch = self.kwargs['branch']
            semester = self.kwargs['semester']
        if semester is not None and branch is not None:
            #queryset = queryset.filter(student__semester=semester, student__branch=branch, created__lt=datem)
            queryset = queryset.filter(student__semester=semester, student__branch=branch)
        return queryset


class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
