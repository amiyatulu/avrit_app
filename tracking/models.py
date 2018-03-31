from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import utc
from django.forms.models import ModelForm


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    SUB_TYPE = (
              ('CG','Curriculum Guide'),
              ('TK','Assignment Task'), 
              ('WB','Workbook'),
                )
    type_of_submission = models.CharField(max_length = 3, choices= SUB_TYPE)
    grade = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    description = models.TextField()
    dat_link = models.CharField(max_length=500)
    backup_link = models.CharField(max_length=500,blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if self.create_time == None:
            self.create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.update_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['create_time','update_time','user']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    graphics = models.TextField(verbose_name="Pairing graphics with words")
    concrete = models.TextField(verbose_name="Linking abstract concepts with concrete representations")
    probing = models.TextField(verbose_name="Posing probing questions")
    elaboration = models.TextField(verbose_name="Elaboration Interrogation")
    solved_problems = models.TextField(verbose_name="Repeatedly alternating solved and unsolved problems")
    practice = models.TextField(verbose_name="Retrieval and Distributed Practice")
    originality = models.TextField()
    errors = models.TextField()
    deepness = models.TextField()
    comprehensible = models.TextField()
    cognitive_load = models.TextField()
    big_ideas = models.TextField()
    evidence = models.TextField()
    overall_comments = models.TextField()
    dat_link = models.CharField(max_length=500)
    backup_link = models.CharField(max_length=500,blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if self.create_time == None:
            self.create_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.update_time = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(Review, self).save(*args, **kwargs)
    def __str__(self):
        return self.post.title