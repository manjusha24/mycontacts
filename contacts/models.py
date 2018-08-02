from django.db import models

class Contact(models.Model):
    name = models.TextField()
    phone = models.IntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name
