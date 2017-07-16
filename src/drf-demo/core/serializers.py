from rest_framework import serializers
from .models import University, Student


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


class StudentSerializer(serializers.ModelSerializer):

    # # This DOESN'T WORK!
    # university_name = serializers.RelatedField(source='university',
    #                                            queryset=University.objects.all())

    # # This one works.
    # university_name = serializers.ReadOnlyField()

    # # Works, too. This one.
    # university_name = serializers.CharField(source='university.name')

    class Meta:
        model = Student
        fields = ('university', 'first_name', 'last_name')
        # fields = ('university_name', 'first_name', 'last_name')

