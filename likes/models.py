from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class likedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenttype = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    # what if the id doesn't integer? we should use code below
    # check it again
    # content_object = GenericForeignKey()
