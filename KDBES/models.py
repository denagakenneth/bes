from django.db import models

#BARANGAY EVENT SCHEDULE


'''COURT_CHOICES =(
    ("M" , "Main Phase 2"),
    ("A" , "Annex Phase 3"),
    )

DAY_CHOICES =(
    ("AM" , "Day Reserve"),
    ("PM" , "Night Reserve"),
    )

# Model 1
class Resident_info(models.Model):
	Brgy_id = models.CharField(max_length=4)
    FresName = models.CharField(max_length=30)
    MresName = models.CharField(max_length=30)
    LresName = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Age = models.CharField(max_length=3)
    Contact_No = models.CharField(max_length=20)
    Emailaddress = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.Name

# Model 2
class Schedule(models.Model):
    resident_info = models.ForeignKey(Resident_info, default=None, on_delete=models.CASCADE)
    Day = models.TextField(default='')
    Time start= models.TextField(default='')
    Time end= models.TextField(default='')
    Hours = models.TextField(default='')
    Date = models.DateTimeField(default='')
    Participants number = models.TextField(default='')
    

    def __str__(self):
        return self.Date_time

# Model 3
class Reservation(models.Model):
	Event = models.ForeignKey(Resident_info, default=None, on_delete=models.CASCADE)
	Court = models.CharField(max_length=1, choices = COURT_CHOICES, default ="")
	Day = models.CharField(max_length = 2, choices = DAY_CHOICES, default ="")
	
	

	def __str__(self):
        return self.Schedule



# Model 4

class Rent(models.Model):
    resident_resrep = models.ForeignKey(Resident_info, default=None, on_delete=models.CASCADE)
    chairs = models.CharField(max_length=30)
    tables = models.CharField(max_length=30)


    def __str__(self):
        return str(self.equipment)


#Model 5
class Barangay_report(models.Model):
    Resident_brgyrep = models.ForeignKey(Resident_info, default=None, on_delete=models.CASCADE)
    Brgyreport = models.TextField(default='')
    Brgy_comment = models.TextField(default='')
    Brgyreport_date = models.DateTimeField(default='')

    def __str__(self):
        return str(self.Brgyreport_date)


#reserved Model 
class Resident_report(models.Model):
    resident_resrep = models.ForeignKey(Resident_info, default=None, on_delete=models.CASCADE)
    Residentreport = models.TextField(default='')
    Resident_comment = models.TextField(default='')
    Barangay_rating = models.TextField(default='')
    Resreport_date = models.DateTimeField(default='')

    def __str__(self):
        return str(self.Resreport_date)'''
