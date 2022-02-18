from django.db import models


# Create your models here.
def create_path(instance,filename):
    return f'{instance.name/{filename}}'

    
class Student(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    age = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to=create_path,default='harry_potter.jpg')
    Mobile_No = models.IntegerField()
    Enrollment_No = models.IntegerField()

    def __str__(self):
        return self.name