from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    chairman = models.ForeignKey('core.Employee', on_delete=models.RESTRICT, blank=True, null=True, related_name='chairman_of')
    posting_rights = models.ManyToManyField('core.Employee', related_name='has_posting_rights_of', blank=True, null=True)

class User(AbstractUser):
    email_notifications = models.BooleanField(default=True)

class Employee(models.Model):
    class DesignationChoice(models.TextChoices):
        ASSISTANT_PROFESSOR = 'P1', 'Assistant Professor'
        ASSOCIATE_PROFESSOR = 'P2', 'Associate Professor'
        PROFESSOR = 'PR', 'Professor'
        LAB_STAFF = 'LS', 'Lab Staff' 
        OFFICE_STAFF = 'OS', 'Office Staff' 

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    employee_id = models.CharField(max_length=10)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=13)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    designation = models.CharField(max_length=5, choices=DesignationChoice.choices)
    user = models.OneToOneField(User, on_delete=models.RESTRICT, related_name="employee", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)


