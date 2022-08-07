from django.db import models



class IllnessAcc(models.Model):
    Insurance_choice=(
        ("اتیه سازان", "atiye sazan" ),
        ("تامین اجتماعی", "tamin ejtemayi" ),
        ("سامان", "saman" ),
        ("دانا", "dana" ),
        ("ایران", "iran" ),
    )

    full_name=models.CharField(max_length=80)
    phone_number=models.PositiveBigIntegerField()
    national_code=models.PositiveBigIntegerField(max_length=10)
    profile_image=models.ImageField()
    Insurance=models.CharField(max_length=35,choices=Insurance_choice)




class Wallet(models.Model):
    user=models.OneToOneField("illness.IllnessAcc",on_delete=models.CASCADE)
    wallet_balance=models.DecimalField(max_digits=9, decimal_places=3,default=0)




class Appointment(models.Model):
    doctor=models.ForeignKey("doctor.Doctor",on_delete=models.CASCADE)
    user=models.ForeignKey("illness.IllnessAcc",null=True,blank=True,on_delete=models.DO_NOTHING)
    start_visit_time=models.TimeField()
    end_visit_time=models.TimeField()
    day=models.ForeignKey("doctor.WeekDays",on_delete=models.CASCADE)
    payment=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    reservetion_code=models.PositiveIntegerField(null=True,blank=True)


