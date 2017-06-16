from rest_framework import serializers
from attendence.models import *


class StudentSerializer(serializers.ModelSerializer):
    """
    Serialize the Student data
    """
    class Meta:
        model = Student
        fields = ('id', 'created', 'roll_no', 'first_name', 'last_name', 'branch', 'semester')


class TheorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Theory
        fields = ('id', 'actual', 'total')


class PracticalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Practical
        fields = ('id', 'actual', 'total')


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serialize the Subject data
    """
    class Meta:
        model = Subject
        fields = ('id', 'subject_name', 'abbr', 'sub_type')


class SubjectStudentSerializer(serializers.ModelSerializer):


    theory = TheorySerializer(many=True, read_only=True)
    practical = PracticalSerializer(many=True, read_only=True)

    class Meta:
        model = SubjectStudent
        fields = ('id', 'theory', 'practical')


class SubjectHolderSerializer(serializers.ModelSerializer):
    """
    Serialize the SubjectHolder Data
    """
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = SubjectHolder
        fields = ('id', 'branch', 'semester', 'subject')


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serialize the Attendance data
    """
    student = StudentSerializer(read_only=True)
    subs = SubjectStudentSerializer(many=True, read_only=True)

    class Meta:
        model = Attendance
        fields = ('id', 'created', 'student', 'subs')

    # def create(self, validated_data):
    #     subjects_data = validated_data.pop('subjects')
    #     attendance = Attendance.objects.create(**validated_data)
    #     for subject_data in subjects_data:
    #         print(subject_data)
    #         Subject.objects.create(attendance_id=attendance, **subject_data)
    #     return attendance
