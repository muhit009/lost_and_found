from django.db import models

# Create your models here.
#location of the item optional?
#something which says it is picked up?
class LostItem(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date_lost = models.DateField()
    category = models.CharField(max_length= 20)
    contact_name = models.CharField(max_length= 20)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length= 15)
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Lost on {self.date_lost})"
    
class FoundItem(models.Model):
    title = models.CharField (max_length= 100)
    description =  models.TextField()
    date_found = models.DateField()
    category = models.CharField(max_length= 20)
    contact_name = models.CharField(max_length= 20)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length= 15)
    
    claimed = models.BooleanField(default=False)  # ✅ new field

    def __str__(self):
        return f"{self.title}(Found on {self.date_found})"
    