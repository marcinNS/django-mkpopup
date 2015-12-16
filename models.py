from cms.models.pluginmodel import CMSPlugin

from django.db import models

class MkPopup(models.Model):
    popup_name = models.CharField(max_length=200,default='Popup...')
    popup_contain = models.TextField(null=True, blank=True)
    popup_image = models.ImageField(upload_to='popup',null=True, blank=True)
    popup_url = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.popup_name

class Popup(CMSPlugin):
    mkpopup = models.ForeignKey(MkPopup)

