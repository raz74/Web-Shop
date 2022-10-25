from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType


class tag(models.Model):
    label = models.CharField(max_length=225)


class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    # type ( product , video, article ... )
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # what if the id doesn't integer? we should use code below
    content_object = GenericForeignKey()
