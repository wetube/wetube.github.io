from django.db import models
from datetime import datetime

# This will hold the data for the models for the main part of the blog.

# The blog post itself
class BlogPost(models.Model):
    # The poster who posted the message. Currently set at 50 length, but can be increased later
    blog_Poster = models.CharField(max_length=50)
    # The time and date at which the message was posted
    blog_TimeDate = models.DateTimeField('Date and Time Published', default=datetime.now())
    # THe project for which the post was made
    blog_Project = models.CharField(max_length=50)
    # A summary of the post
    blog_Summary = models.CharField(max_length=100)
    # The actual content of the post
    blog_Content = models.CharField(max_length=1000)
    # The id of the blog post, so that we can identify it
    # blog_ID = models.IntegerField()
    
    def __str__(self):
        return self.blog_Summary
