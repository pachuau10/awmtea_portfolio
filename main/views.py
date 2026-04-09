from django.shortcuts import render, get_object_or_404
from .models import Project, Publication, Skill, BlogPost
from itertools import groupby


def home(request):
    projects = Project.objects.filter(featured=True)[:3]
    publications = Publication.objects.all()[:3]
    skills = Skill.objects.all()
    skills_by_category = {}
    for skill in skills:
        skills_by_category.setdefault(skill.get_category_display(), []).append(skill)
    recent_posts = BlogPost.objects.filter(published=True)[:3]
    return render(request, 'main/home.html', {
        'projects': projects,
        'publications': publications,
        'skills_by_category': skills_by_category,
        'recent_posts': recent_posts,
    })


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': all_projects})


def publications(request):
    pubs = Publication.objects.all()
    return render(request, 'main/publications.html', {'publications': pubs})


def blog(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'main/blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'main/blog_detail.html', {'post': post})


def contact(request):
    sent = False
    if request.method == 'POST':
        sent = True
    return render(request, 'main/contact.html', {'sent': sent})
