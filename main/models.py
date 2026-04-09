from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class Publication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    journal = models.CharField(max_length=200)
    year = models.IntegerField()
    abstract = models.TextField(blank=True)
    doi_url = models.URLField(blank=True)
    arxiv_url = models.URLField(blank=True)
    pub_type = models.CharField(max_length=50, choices=[
        ('journal', 'Journal Article'),
        ('conference', 'Conference Paper'),
        ('preprint', 'Preprint'),
        ('thesis', 'Thesis'),
    ], default='journal')

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('tools', 'Tools & Software'),
        ('physics', 'Physics & Theory'),
        ('data', 'Data & Analysis'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['category', '-proficiency']

    def __str__(self):
        return f"{self.name} ({self.category})"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]
