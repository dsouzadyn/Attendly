from attendence.serializers import *
from rest_framework import generics


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def perform_create(self, serializer):
        serializer.save()


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class FacultyList(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def perform_create(self, serializer):
        serializer.save()


class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


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
        branch_id = self.kwargs['branch_id']
        return SubjectHolder.objects.filter(branch_id=branch_id, semester=semester)

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
    queryset = Subject.objects.all()
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
        queryset = Attendance.objects.all()
        branch = self.request.query_params.get('branch', None)
        semester = self.request.query_params.get('semester', None)
        if semester is not None and branch is not None:
            queryset = queryset.filter(student_id__semester=semester, student_id__branch_id=branch)
        return queryset


class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
