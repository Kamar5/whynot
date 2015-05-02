from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #Not sure whether to store the actual picture or a link to the picture that is stored on the filesystem
    #For now we're going to use filepath
    profile_pic = models.CharField(max_length=40)

class Pic_Actions(models.Model):
    username = models.CharField(max_length=30) #Uploader
    date = models.CharField(max_length=40) 
    pic_before = models.CharField(max_length=30) #Before Pic Filepath
    pic_after = models.CharField(max_length=30)  #After Pic filepath
    score = models.PositiveSmallIntegerField(default=1) #Picture Score
    
   


    

