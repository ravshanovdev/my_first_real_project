from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class ClassRoom(models.Model):
    name = models.CharField(max_length=150)
    student_size = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=200)
    about = models.TextField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    about = models.TextField()

    def __str__(self):
        return self.first_name


class Payments(models.Model):
    VALUE_TYPE = (
        ('1', 'UZS'),
        ('2', 'USA'),
        ('3', 'EURO')
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=9)
    amount_type = models.CharField(max_length=15, choices=VALUE_TYPE)

    def __repr__(self):
        return self.student


class Group(models.Model):
    VALUE_TYPE = (
        ('Active', 'Faol'),
        ('Waiting', 'Kutilyapti'),
        ('Finished', 'Tugalangan')
    )

    VALUE_TYPE2 = (
        ('1', 'Dushanba'),
        ('2', 'Seshanba'),
        ('3', 'Chorshanba'),
        ('4', 'Payshanba'),
        ('5', 'Juma'),
        ('6', 'Shanba'),
        ('7', 'Yakshanba')
    )
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_size = models.IntegerField(default=0)
    students = models.ManyToManyField('Student', blank=True)
    start_time = models.CharField(max_length=150)
    days = models.CharField(max_length=150, choices=VALUE_TYPE2)
    status = models.CharField(max_length=150, choices=VALUE_TYPE)
    text = models.TextField()

    def __str__(self):
        return self.name


class Attendance(models.Model):
    VALUE_TYPE = (
        ('ha', "+"),
        ("yo'q", "-")
    )
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    student_id = models.ManyToManyField('Student')
    data = models.DateTimeField(auto_now_add=True)
    attendance = models.CharField(max_length=1500, choices=VALUE_TYPE)
