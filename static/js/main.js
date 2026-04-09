// ===== NAV TOGGLE =====
const toggle = document.querySelector('.nav-toggle');
const mobileNav = document.querySelector('.nav-mobile');

if (toggle && mobileNav) {
  toggle.addEventListener('click', () => {
    toggle.classList.toggle('open');
    mobileNav.classList.toggle('open');
  });

  // Close on link click
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      toggle.classList.remove('open');
      mobileNav.classList.remove('open');
    });
  });
}

// ===== ACTIVE NAV LINK =====
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a, .nav-mobile a').forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});

// ===== SCROLL ANIMATIONS =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      entry.target.style.animationDelay = `${i * 0.1}s`;
      entry.target.classList.add('fade-in');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.card, .timeline-item, .pub-card').forEach(el => {
  el.style.opacity = '0';
  observer.observe(el);
});

// ===== SKILL BAR ANIMATION =====
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const fill = entry.target;
      const target = fill.getAttribute('data-width');
      setTimeout(() => { fill.style.width = target; }, 200);
      skillObserver.unobserve(fill);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.skill-fill').forEach(bar => {
  const targetWidth = bar.style.width;
  bar.setAttribute('data-width', targetWidth);
  bar.style.width = '0';
  skillObserver.observe(bar);
});

// ===== TYPEWRITER =====
function typewriter(el, text, speed = 60) {
  let i = 0;
  el.textContent = '';
  const interval = setInterval(() => {
    el.textContent += text[i];
    i++;
    if (i >= text.length) clearInterval(interval);
  }, speed);
}

const twEl = document.querySelector('[data-typewriter]');
if (twEl) {
  setTimeout(() => typewriter(twEl, twEl.getAttribute('data-typewriter')), 800);
}

// ===== SMOOTH CLOSE MOBILE NAV ON OUTSIDE CLICK =====
document.addEventListener('click', (e) => {
  if (toggle && mobileNav && !toggle.contains(e.target) && !mobileNav.contains(e.target)) {
    toggle.classList.remove('open');
    mobileNav.classList.remove('open');
  }
});
