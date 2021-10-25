from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Add a table in database named as product

DeptChoice = [
    ('', 'Depertment'),
    ('Not Applicable', 'Not Applicable'),
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil '),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
]
YearChoice = [
    ('', 'Year'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstYear', 'First Year'),
    ('SecondYear', 'Second Year '),
    ('ThirdYear', 'Third Year'),
    ('FourthYear', 'Fourth Year'),
]
SemChoice = [
    ('', 'Semester'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstSemester', 'First Semester'),
    ('SecondSemester', 'Second Semester '),
    ('ThirdSemester', 'Third Semester'),
    ('FourthSemester', 'Fourth Semester'),
    ('FifthSemester', 'Fifth Semester'),
    ('SixthSemester', 'Sixth Semester'),
    ('SeventhSemester', 'Seventh Semester'),
    ('EightthSemester', 'Eightth Semester'),
]
NewsDeptChoice = [
    ('Mechanical', 'Mechanical'),
    ('Civil ', 'Civil '),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
    ('placement', 'Placement'),
    ('admission', 'Admission'),
    ('event', 'Event'),
    ('CDC', 'CDC')
]


class User(AbstractUser):
    # Need For All Project
    dept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    year = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    semester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    profilepic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png')
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)
    status = models.BooleanField(default=True)


class News(models.Model):
    Heading = models.CharField(max_length=50)
    category = models.CharField(
        max_length=40, choices=NewsDeptChoice, default='Computer Science')
    subcategory = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="outlet/images", default="")

    def __str__(self):
        return self.Heading


class Contact(models.Model):
    person_name = models.CharField(max_length=30)
    person_email = models.EmailField()
    person_phone = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.person_name+'-'+self.person_email
