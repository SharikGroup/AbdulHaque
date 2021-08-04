from django.db import models
from core.models import User, Department

# Create your models here.
class Post(models.Model):
    class PrivacyChoice(models.TextChoices):
        PUBLIC = 'PBLC', 'Public'
        ALL_EMPLOYEES = 'EMAL', "All Employees"
        ALL_EMPLOYEES_OF_DEPT = 'EMDP', 'All Employees of Selected Departments'
        ALL_CHAIRMEN = 'CMAL', 'All Chairmen'
        CHAIRMAN_OF_DEPT = 'CMDP', 'CHariman of Selected Departments'

    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    privacy = models.CharField(max_length=5, choices=PrivacyChoice.choices)
    departments = models.ManyToManyField(Department, related_name="posts")

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image_original = models.ImageField(upload_to='images', max_length=255)
    image_sm = models.ImageField(upload_to='images', max_length=255)
    image_md = models.ImageField(upload_to='images', max_length=255)