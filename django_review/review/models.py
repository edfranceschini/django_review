from django.db import models
from django.utils.text import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .fields import IntegerRangeField




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(_('Bio '),max_length = 500, blank = True)
    location = models.CharField(_('Location'),max_length = 30, blank = True)
    
    
    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')



class Company(models.Model):
    name = models.CharField(_('Name'), max_length=64, db_index = True)
    address = models.TextField(_('Full address'), blank = True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _('Company')
        verbose_name = _('Companies')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    title = models.CharField(_('Title'), max_length = 64, blank = False)
    rating = IntegerRangeField(_('Rating'), blank = False, min = 1, max = 5)
    summary = models.CharField(_('Summary'), max_length = 10240, blank = False)
    ip_address = models.IPAddressField(_('Sender IP'), blank = True)
    sub_date = models.DateTimeField(_('Submission Date'), auto_created = True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
    



@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
