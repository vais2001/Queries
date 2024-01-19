from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    SUBJECT_CHOICES=(
        ('HOME_SCIENCE','home_science'),
        ('MATHS','maths'),
        ('ENGLISH','english'),
        ('PHYSICS','physics'),
        ('COMPUTER','computer')
    )
    subjects=models.CharField(max_length=50,choices=SUBJECT_CHOICES)
    
    
    def __str__(self):
       return self.name 

class Books(models.Model):
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=200)
  price = models.IntegerField(null=True)
  student = models.ForeignKey('Student', on_delete=models.CASCADE,null=True,blank=True)
 
  def __str__(self):
    return self.title