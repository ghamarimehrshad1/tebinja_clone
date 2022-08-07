from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
import datetime as dt




class Doctor(models.Model):
    time_choices=(
        ("15 mine", "15" ),
        ("20 mine", "20" ),
        ("30 mine", "30" ),
        ("45 mine", "45" ),
        ("60 mine", "60" ),
    )
    full_name=models.CharField(max_length=80)
    medical_system_code=models.PositiveSmallIntegerField(max_length=6)
    adress=models.TextField()
    phone_number = models.PositiveBigIntegerField(unique=True)
    registeration_date=models.DateTimeField(auto_now_add=True)
    bio=models.TextField()
    experince=models.PositiveSmallIntegerField()
    cost_visit=models.DecimalField(max_digits=9, decimal_places=3)
    week_days=models.ManyToManyField("doctor.WeekDays")
    visit_time=models.CharField(max_length=10,choices=time_choices)



class Telephone(models.Model):
    doctor=models.ForeignKey("doctor.Doctor",on_delete=models.CASCADE)
    telephone_number=models.PositiveBigIntegerField(unique=True)



class CommentForDoctor(models.Model):

    rate_choices=(
        ("1", "1" ),
        ("2", "2" ),
        ("3", "3" ),
        ("4", "4" ),
        ("5", "5" ),
    )
    desciption=models.TextField()
    doctor=models.ForeignKey("doctor.Doctor",on_delete=models.CASCADE)
    user=models.OneToOneField()
    create_time=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerChoices(rate_choices)



class WeekDays(models.Model):
    choice_days=(
        ("saturday", "saturday" ),
        ("sunday", "sunday" ),
        ("monday", "monday" ),
        ("tuesday", "tuesday" ),
        ("wednesday", "wednesday" ),
        ("thursday", "thursday" ),
        ("friday", "friday" ),
    )

    day=models.CharField(choices=choice_days,max_length=10)



class DoctorShift(models.Model):
    HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
    start_time=models.TimeField(choices=HOUR_CHOICES)
    end_time=models.TimeField(choices=HOUR_CHOICES)
    doctor=models.ForeignKey("doctor.Doctor",on_delete=models.CASCADE)



    