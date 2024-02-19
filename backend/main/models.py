from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import pytz


class Operators(models.Model):
    name = models.CharField(max_length=20)
    code = models.PositiveIntegerField(default=0)
    def __str__(self) -> str:
         return self.name
             
		 	
    
class Tags(models.Model):
    tag_name = models.CharField(max_length=40)
    def __str__(self) -> str:
         return self.tag_name
    
class Send_Status(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self) -> str:
         return self.name
         
    

class Sender(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1200)
    mobile_operator = models.ForeignKey(Operators,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)
    created_until = models.DateTimeField(auto_now_add=False)
    def __str__(self) -> str:
         return self.text + " | " + self.mobile_operator

class Client(models.Model):
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, region='RU')
    mobile_operator = models.ForeignKey(Operators,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, default='UTC', choices=TIMEZONES)
    def __str__(self) -> str:
         return self.phone_number + " | " + self.tag

class Message(models.Model):
    send_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Send_Status,on_delete=models.CASCADE)
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self) -> str:
         return self.client.phone_number + " | " + self.status
