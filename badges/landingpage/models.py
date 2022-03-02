from django.db import models

# Create your models here.
class Badge(models.Model):
    badge_name=models.CharField(max_length=30)
    badge_description = models.TextField(default='')
    badge_image = models.ImageField(upload_to='badge_images',default ='badge_images/badge_default.jpg' )
    
    def __str__(self):
         return self.badge_name

class Student(models.Model):
    student_email=models.CharField(max_length=100)
    student_badge=models.ForeignKey('Badge',on_delete=models.CASCADE)
    
    def __str__(self):
         return self.student_email