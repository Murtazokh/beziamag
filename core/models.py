from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
    
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    content = models.TextField()
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author} - {self.role}"