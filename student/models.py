from django.db import models
import uuid


# Create your models here.
class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_no = models.IntegerField(null=True, blank=True, unique=True)
    student_name = models.CharField(max_length=30)
    student_dob = models.DateField()
    student_doj = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
