from django.db import models

# Create your models here.
'''
title
author
content
image
tags
puplish date

'''
class post (models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=50000)
    publish_date=models.DateTimeField()

