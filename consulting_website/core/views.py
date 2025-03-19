# core/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Service, TeamMember, Testimonial, CaseStudy, BlogPost
from django.core.paginator import Paginator
from .forms import ContactForm
from django.contrib import messages

# Home page view
def home(request):
    # Get featured services
    featured_services = Service.objects.filter(featured=True).order_by('order')
    
    # Get testimonials for homepage
    testimonials = Testimonial.objects.filter(display_on_homepage=True)
    
    context = {
        'featured_services': featured_services,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

# Services list view
def service_list(request):
    services = Service.objects.all().order_by('order')
    context = {
        'services': services,
    }
    return render(request, 'services/list.html', context)

# Service detail view
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    # Get case studies related to this service (you would need to add a relationship in models)
    # case_studies = service.case_studies.all()
    
    context = {
        'service': service,
        # 'case_studies': case_studies,
    }
    return render(request, 'services/detail.html', context)

# About page view
def about(request):
    team_members = TeamMember.objects.all().order_by('order')
    context = {
        'team_members': team_members,
    }
    return render(request, 'about/about.html', context)

# Testimonials page view
def testimonials(request):
    all_testimonials = Testimonial.objects.all()
    case_studies = CaseStudy.objects.all()
    
    context = {
        'testimonials': all_testimonials,
        'case_studies': case_studies,
    }
    return render(request, 'testimonials.html', context)

# Blog list view
def blog(request):
    posts = BlogPost.objects.all().order_by('-pub_date')
    
    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/list.html', context)

# Blog detail view
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)

# Contact page view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form but don't commit yet
            contact_submission = form.save(commit=False)
            # Add IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            contact_submission.ip_address = ip
            # Save to database
            contact_submission.save()
            # Add success message
            messages.success(request, 'Your message has been sent successfully. We will contact you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)