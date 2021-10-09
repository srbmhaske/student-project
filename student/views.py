###package imports
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json

###student app imports
import student.serializers as student_serializer
from student.models import *
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = student_serializer.StudentSerializer

    ###display all students
    def get_queryset(self):
        return Student.objects.all()


    ###save a new studen profilet
    @action(methods=['post'], detail=False)
    def create_student(self, request, pk=None):
        data = request.data
        add_student = student_serializer.StudentSerializer(data=data)
        if add_student.is_valid(raise_exception=True):
            add_student.save()
            return HttpResponse(json.dumps({
                    'status': status.HTTP_201_CREATED,
                    'message': 'student added successfully',
                    'data': add_student.data,
                    'error': None
                }),content_type='application/json', status=status.HTTP_201_CREATED)


    ###update student profile
    @action(methods=['patch'], detail=False)
    def update_student(self, request, pk=None):
        data = request.data
        if 'student_no' not in data or data['student_no'] =='':
            return HttpResponse(json.dumps({
                    'student_no': ['Please enter student no (mandatory)']
                }),content_type='application/json', status=status.HTTP_400_BAD_REQUEST)
        student_no = data['student_no']
        student = Student.objects.get(student_no=student_no)
        add_student = student_serializer.StudentSerializer(student, data=data, partial=True)
        if add_student.is_valid(raise_exception=True):
            add_student.save()
            return HttpResponse(json.dumps({
                    'status': status.HTTP_200_OK,
                    'message': 'student updated successfully',
                    'data': add_student.data,
                    'error': None
                }),content_type='application/json', status=status.HTTP_200_OK)


    ###delete student profile
    @action(methods=['delete'], detail=False)
    def delete_student(self, request, pk=None):
        student_no = self.request.query_params.get('student_no')
        if student_no =='':
            return HttpResponse(json.dumps({
                    'student_no': ['Please enter student no (mandatory)']
                }),content_type='application/json', status=status.HTTP_400_BAD_REQUEST)
        student = Student.objects.get(student_no=student_no)
        student.delete()
        return HttpResponse(json.dumps({
                'status': status.HTTP_200_OK,
                'message': 'student with no ' + student_no +' deleted successfully',
                'error': None
            }),content_type='application/json', status=status.HTTP_200_OK)
