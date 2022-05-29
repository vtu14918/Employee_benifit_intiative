from django.db import models
    
class upload(models.Model):
    file=models.FileField(upload_to='pictures')
