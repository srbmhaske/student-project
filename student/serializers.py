from rest_framework import serializers
import student.models as student_models

class StudentSerializer(serializers.ModelSerializer):
    def validate_student_no(self, value):
        if value>999:
            raise serializers.ValidationError("student_no can be of only 3 digits")

        if value is None:
            raise serializers.ValidationError("student_no can not be blank")
        return value


    class Meta:
        model = student_models.Student
        fields = '__all__'
