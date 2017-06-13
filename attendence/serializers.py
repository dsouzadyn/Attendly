from rest_framework import serializers
from attendence.models import *


class StudentSerializer(serializers.ModelSerializer):
    """
    Serialize the Student data
    """
    class Meta:
        model = Student
        fields = ('id', 'created', 'roll_no', 'first_name', 'last_name', 'branch_id', 'semester')


class SubjectHolderSerializer(serializers.ModelSerializer):
    """
    Serialize the SubjectHolder Data
    """
    subject_name = serializers.StringRelatedField()

    class Meta:
        model = SubjectHolder
        fields = ('id', 'branch', 'semester', 'subject_name')


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serialize the Subject data
    """
    class Meta:
        model = Subject
        fields = ('id', 'created', 'subject_name', 'value', 'lecture_type')


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serialize the Attendance data
    """
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Attendance
        fields = ('id', 'created', 'student_id', 'subjects')

    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects')
        attendance = Attendance.objects.create(**validated_data)
        for subject_data in subjects_data:
            print(subject_data)
            Subject.objects.create(attendance_id=attendance, **subject_data)
        return attendance
