from django.db import models

class Alias(models.Model):
    shortcut = models.CharField(max_length=250, primary_key=True)
    dst = models.URLField()

    def __unicode__(self):
        return '%s -> %s' % (self.shortcut, self.dst)


