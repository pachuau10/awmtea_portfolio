# 🔬 MSc Physics Portfolio — Django

A dark, techy portfolio website built with Django for an MSc Physics student.
Features neon-cyan-on-dark aesthetic, fully responsive (desktop + mobile).

---

## 📁 Project Structure

```
portfolio/              ← Django project root
├── manage.py
├── db.sqlite3
├── portfolio/          ← Project settings & URLs
│   ├── settings.py
│   └── urls.py
├── main/               ← Main app
│   ├── models.py       ← Project, Publication, Skill, BlogPost
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templatetags/
│       └── portfolio_tags.py
├── templates/
│   ├── base.html       ← Navbar, footer, shared layout
│   └── main/
│       ├── home.html           ← Hero, About, Education, Skills, Projects, Publications, Blog
│       ├── projects.html
│       ├── publications.html
│       ├── blog.html
│       ├── blog_detail.html
│       └── contact.html
└── static/
    ├── css/style.css   ← All styles (dark techy, neon accents, responsive)
    └── js/main.js      ← Nav toggle, scroll animations, skill bars, typewriter
```

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install django
```

### 2. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a superuser (to manage content via Admin)
```bash
python manage.py createsuperuser
```

### 4. Run the development server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

---

## ✏️ Personalising Your Portfolio

### Replace placeholder text
Search for these placeholders throughout the templates and replace them:

| Placeholder | Replace with |
|-------------|--------------|
| `Your Name` | Your actual name |
| `YN` | Your initials |
| `[Your University]` | Your university name |
| `[your research area]` | e.g. Condensed Matter, Astrophysics |
| `[Your Thesis Title]` | Your actual thesis title |
| `[Supervisor Name]` | Your supervisor's name |
| `your@email.com` | Your email address |
| `yourusername` | Your GitHub/LinkedIn username |

### Add your photo
Replace the initials placeholder in `base.html` avatar section with:
```html
<img src="{% static 'img/profile.jpg' %}" alt="Your Name" style="width:100%;height:100%;object-fit:cover;" />
```
Then place your photo at `static/img/profile.jpg`.

### Add your CV
Place your CV PDF at `static/cv.pdf`.

---

## 📋 Managing Content (Django Admin)

Go to `/admin` and log in with your superuser account.

### Adding Projects
- **Title**: Project name
- **Description**: What it does
- **Tech Stack**: Comma-separated (e.g. `Python, NumPy, Matplotlib`)
- **Featured**: Check to show on homepage
- **Order**: Controls display order

### Adding Publications
- Fill in title, authors, journal, year
- Choose type: Journal / Conference / Preprint / Thesis
- Add DOI or arXiv URL for links

### Adding Skills
- Choose category: Programming / Physics & Theory / Data & Analysis / Tools / Other
- Set proficiency 0–100 (renders as animated bar)

### Adding Blog Posts
- Write content in plain text or HTML
- Set `published = True` to make it visible
- Slug is the URL: e.g. slug `my-post` → `/blog/my-post/`
- Add comma-separated tags: `Quantum Physics, Tutorial`

---

## 🌐 Pages

| URL | Description |
|-----|-------------|
| `/` | Home (Hero + About + Education + Skills + Projects + Publications + Blog) |
| `/projects/` | All projects |
| `/publications/` | All publications |
| `/blog/` | Blog post list |
| `/blog/<slug>/` | Individual blog post |
| `/contact/` | Contact form + social links |
| `/admin/` | Django admin panel |

---

## 📱 Responsive Design

- **Desktop (>768px)**: Full navbar, multi-column grid layouts
- **Tablet (768px–1024px)**: Single-column about/contact sections
- **Mobile (<768px)**: Hamburger menu, single-column everything
- **Small mobile (<480px)**: Full-width buttons, tighter spacing

---

## 🎨 Design System

| Variable | Value | Use |
|----------|-------|-----|
| `--neon-cyan` | `#00f5ff` | Primary accent, glows, links |
| `--neon-purple` | `#7b2fff` | Secondary accent |
| `--neon-green` | `#00ff88` | Tertiary accent |
| `--bg-primary` | `#050a0e` | Page background |
| `--bg-card` | `#0d1b2a` | Card backgrounds |
| `--font-display` | Orbitron | Headings |
| `--font-body` | Rajdhani | Body text |
| `--font-mono` | Space Mono | Labels, tags, code |

---

## 🔧 Production Deployment

Before deploying:

1. In `settings.py`:
   - Set `DEBUG = False`
   - Set `ALLOWED_HOSTS = ['yourdomain.com']`
   - Set a strong `SECRET_KEY`
   - Configure `DATABASES` (PostgreSQL recommended)

2. Collect static files:
```bash
python manage.py collectstatic
```

3. Use gunicorn + nginx, or deploy to Railway / Render / Heroku.

---

## 📧 Email Contact Form

The current contact form just sets `sent = True` on POST.
To actually send emails, add to `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```
Then update the `contact` view in `views.py` to call `send_mail()`.
