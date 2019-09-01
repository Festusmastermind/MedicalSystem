import hashlib
from django.db import models

# Create your models here.

class patient(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    local_govt = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=20,null=True, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    upload = models.FileField(null=True, blank=True)

    def __str__(self):
        return "%s - %s " % (self.firstname, self.phone)

    # overwriting the save method.
    # so before we save our post data we want to hash the password..
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = createHash(self.password)
        super(patient, self).save(*args, **kwargs)


# hashing of password using SHA256 , but then y hash the password again when the its already automatically hash?
def createHash(value):
    hash = hashlib.sha256()
    hash.update(str(value).encode(encoding='UTF-8'))
    return hash.hexdigest()


class doctor(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    ch_types = {
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    }
    status = models.CharField(choices=ch_types, max_length=20, blank=True, null=True)
    local_govt = models.CharField(max_length=200, null=True, blank=True)
    speciality = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    image1 = models.FileField(null=True, blank=True)

    def __str__(self):
        return "%s - %s " % (self.firstname, self.phone)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = createHash(self.password)
        super(doctor, self).save(*args, **kwargs)


class appointment(models.Model):
    status = models.CharField(max_length=200, null=True, blank=True)
    # apptime = models.TimeField(auto_now=False, auto_now_add=False)
    appdate = models.DateField(auto_now=False, auto_now_add=False)
    appmessage = models.TextField(null=True, blank=True)
    docname = models.CharField(max_length=200, null=True, blank=True)
    docfirst = models.CharField(max_length=200, null=True, blank=True)
    doclast = models.CharField(max_length=200, null=True, blank=True)
    patname = models.CharField(max_length=200, null=True, blank=True)
    patlast = models.CharField(max_length=200, null=True, blank=True)
    patfirst = models.CharField(max_length=200, null=True, blank=True)
    types = {
        ('9:00 - 9:30', '9:00 - 9:30'),
        ('9:30 - 10:00', '9:30 - 10:00'),
        ('10:00 - 10:30', '10:00 - 10:30'),
        ('10:30 - 11:00', '10:30 - 11:00'),
        ('11:00 - 11:30', '11:00 - 11:30'),
        ('11:30 - 12:00', '11:30 - 12:00'),
        ('12:00 - 12:30', '12:00 - 12:30'),
        ('12:30 - 1:00', '12:30 - 1:00'),
        ('1:00 - 1:30', '1:00 - 1:30'),
        ('1:30 - 2:00', '1:30 - 2:00'),
    }
    apptime = models.CharField(choices=types, max_length=40, blank=True, null=True)
    def __str__(self):
        return "%s - %s " % (self.appdate, self.apptime)

