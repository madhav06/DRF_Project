from django.db import models

# Create your models here.

class Manager(models.Model):
    full_name = models.CharField(max_length=200, null=False )
    date_of_birth = models.DateField(max_length=100, null=False )
    blood_group = models.CharField(max_length=200, null=True )
    # job_role = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=200, null=True )
    email = models.CharField(max_length=200, null=True )
    aadhar_number = models.IntegerField( null=False )

    def __str__(self):
        return self.full_name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    CATEGORY = (
        ('IT DEPT.', 'HR DEPT.',),
        ('HR DEPT.','IT DEPT.',),
        ('FINANCE', 'AUDIT',),
        ('MARKETING', 'SALES',),
    )


    staff_name = models.CharField(max_length=200, null=True )
    category = models.CharField(max_length=100, null=True , choices=CATEGORY)
    date_joined = models.DateField(max_length=200, null=True )
    contact = models.CharField(max_length=200, null=True )
    email = models.CharField(max_length=200, null=True )
    status = models.CharField(max_length=100 ,null=True)
    aadhar_number = models.IntegerField( null=False )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.staff_name

class utility(models.Model):
    STATUS = (
        ('IsActive', 'IsNotActive', ),
        ('IsNotActive', 'IsActive'),
    )

    # One- Many relationship
    manager = models.ForeignKey(Manager, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)

    status = models.CharField(max_length=100,  null=True, choices=STATUS )
    

class BankDetails(models.Model):
    ifsc_code = models.CharField(max_length=100, null=False)
    bank_acc = models.IntegerField(max_length=100, null=True)
    bank_name = models.CharField(max_length=100, null=True)

# class Tag(models.Model):





