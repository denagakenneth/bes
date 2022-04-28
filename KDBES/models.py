from django.db import models

class Resident(models.Model):
	brgyid = models.TextField(default='')
	FresName = models.TextField(default='')
	MresName = models.TextField(default='')
	LresName = models.TextField(default='')
	resAddress = models.TextField(default='')
	resAge= models.TextField(default='')
	resBday = models.TextField(default='')
	resContact = models.TextField(default='')
	registration = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE)

'''class Registration(models.Model):
	brgyID = models.TextField(default='')
	brgy = models.TextField(default='')
	brgyadd = models.TextField(default='')'''