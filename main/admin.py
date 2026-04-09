from django.contrib import admin
from .models import Project, Publication, Skill, BlogPost

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order']
    list_editable = ['featured', 'order']

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'journal', 'year', 'pub_type']
    list_filter = ['pub_type', 'year']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created_at']
    list_editable = ['published']
    prepopulated_fields = {'slug': ('title',)}
