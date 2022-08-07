from django.db import models

class cust(models.Model):
 custid=models.IntegerField(primary_key=True)
 passwd=models.EmailField(max_length=20,default="")
 name=models.EmailField(max_length=20,default="")
 balance=models.IntegerField(default=0)
 opendate=models.DateField(default="")
 status=models.IntegerField(default=0)

class trans(models.Model):
 transid=models.IntegerField(primary_key=True)
 sender=models.IntegerField(default=0)
 receiver=models.EmailField(default=0) 
 amt=models.IntegerField(default=0)
 status=models.TextField(default="")
 dot=models.DateField(default="")
 

