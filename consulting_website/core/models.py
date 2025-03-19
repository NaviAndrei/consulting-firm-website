from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    icon = models.ImageField(upload_to='services/icons/')
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    quote = models.TextField()
    display_on_homepage = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Testimonial from {self.client_name}, {self.company}"

class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    client_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    challenge = models.TextField()
    approach = models.TextField()
    solution = models.TextField()
    testimonial_text = models.TextField(blank=True, null=True)
    testimonial_author = models.CharField(max_length=100, blank=True, null=True)
    testimonial_position = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('case_study_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Metric(models.Model):
    case_study = models.ForeignKey(CaseStudy, related_name='metrics', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # e.g., "45%" or "$2.3M"
    label = models.CharField(max_length=100)  # e.g., "Increase in Revenue"
    
    def __str__(self):
        return f"{self.label}: {self.value}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    def __str__(self):
        return f"Contact from {self.name} ({self.created_at})"