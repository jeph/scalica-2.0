from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.forms import ModelForm, TextInput
import uuid

class Post(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  text = models.CharField(max_length=256, default="")
  pub_date = models.DateTimeField('date_posted')
  def __str__(self):
    if len(self.text) < 16:
      desc = self.text
    else:
      desc = self.text[0:16]
    return self.user.username + ':' + desc

class Following(models.Model):
  follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="user_follows")
  followee = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="user_followed")
  follow_date = models.DateTimeField('follow data')
  def __str__(self):
    return self.follower.username + "->" + self.followee.username

class Photo(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
  img_id = models.CharField(max_length=100, null=True)
  num_faces = models.IntegerField(default=0)

class Tag(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.CharField(max_length=100)
  photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
# Model Forms
class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ('text',)
    widgets = {
      'text': TextInput(attrs={'id' : 'input_post'}),
    }

class FollowingForm(ModelForm):
  class Meta:
    model = Following
    fields = ('followee',)

class PhotoForm(ModelForm):
  class Meta:
    model = Photo
    fields = ()

class TagForm(ModelForm):
  class Meta:
    model = Tag
    fields = ('text',)

class MyUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    help_texts = {
      'username' : '',
    }
