from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post = models.TextField()
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=False)
    image_post = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.post

    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment',on_delete=models.CASCADE)
    comment = models.TextField()
    image_comment = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    comment_date = models.DateTimeField(auto_now=False)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.comment


class Vote(models.Model):
    comment = models.ForeignKey(Comment, related_name='votes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("post", "vote_by")


