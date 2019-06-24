from django.db import models
import datetime

# Create your models here.
class Adie(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    orientation = models.CharField(max_length=100)
    transplant = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'cohort: %s,\nAge: %s,\nGender: %s,\nRace: %s,\nSexual Orientation: %s,\nTransplant?: %s,\nLocation: %s, %s' % (self.cohort, self.age, self.gender, self.race, self.orientation, self.transplant, self.city, self.state)

class Company(models.Model):
    startup = models.BooleanField(default=False)
    org_size = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    adies_present = models.BooleanField(default=False)

    def __str__(self):
        return '\nStartup?: %s,\nOrg Size: %s,\nLocation: %s,  %s\nIndustry: %s,\nAdies Present?: %s' % (self.startup, self.org_size, self.city, self.state, self.industry, self.adies_present)

class Offer(models.Model):
    adie = models.ForeignKey(Adie, on_delete=models.CASCADE)
    base_amount = models.IntegerField()
    signing_bonus = models.IntegerField()
    negotiations = models.BooleanField(default=False)
    relocation_package = models.BooleanField(default=False)
    health_insurance = models.BooleanField(default=False)
    retirement_matching = models.IntegerField()
    vacation_days = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '\nAdie: %s,\nCompany: %s,\nBase Pay: %s,\nAny Negotiations?: %s,\nSigning Bonus: %s,\nHealth Insurance?: %s,\n # of Vacation Days: %s,\nRetirement?: %s,\nRelocation Compensation?: %s' % (self.adie_id, self.company_id, self.base_amount, self.negotiations, self.signing_bonus, self.health_insurance, self.vacation_days, self.retirement, self.relocation_package)
