# core/admin.py

from django.contrib import admin
from .models import Service, TeamMember, Testimonial, CaseStudy, Metric, BlogPost, ContactSubmission

class MetricInline(admin.TabularInline):
    model = Metric
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'featured', 'order')
    list_filter = ('featured',)
    search_fields = ('title', 'short_description', 'full_description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'order')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position', 'bio')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'display_on_homepage')
    list_filter = ('display_on_homepage',)
    list_editable = ('display_on_homepage',)
    search_fields = ('client_name', 'company', 'quote')

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'industry')
    search_fields = ('title', 'client_name', 'industry', 'challenge', 'approach', 'solution')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MetricInline]

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at', 'ip_address')

# Customize admin site header and title
admin.site.site_header = 'Consulting Firm Admin'
admin.site.site_title = 'Consulting Firm Admin Portal'
admin.site.index_title = 'Welcome to Consulting Firm Admin Portal'