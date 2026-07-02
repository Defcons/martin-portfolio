/* ============================================
   Martin Davidsen — Portfolio Logic
   ============================================ */

(function () {
    'use strict';

    // ---- Language Toggle ----
    let currentLang = localStorage.getItem('cc-lang') || 'en';

    function setLanguage(lang) {
        currentLang = lang;
        localStorage.setItem('cc-lang', lang);

        document.documentElement.lang = lang === 'no' ? 'no' : 'en';

        document.querySelectorAll('[data-en][data-no]').forEach(el => {
            const text = el.getAttribute(`data-${lang}`);
            if (text) el.textContent = text;
        });

        // Update active flag in toggle
        const flags = document.querySelectorAll('.lang-flag');
        flags.forEach(flag => {
            flag.classList.toggle('active',
                (flag.textContent === 'EN' && lang === 'en') ||
                (flag.textContent === 'NO' && lang === 'no')
            );
        });
    }

    // ---- Navbar Scroll Effect ----
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;

    function handleScroll() {
        const scrollY = window.scrollY;
        navbar.classList.toggle('scrolled', scrollY > 50);
        lastScroll = scrollY;
    }

    // ---- Mobile Menu ----
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    function toggleMenu() {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('open');
        document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
    }

    function closeMenu() {
        hamburger.classList.remove('active');
        navLinks.classList.remove('open');
        document.body.style.overflow = '';
    }

    // ---- Scroll Animations ----
    function initScrollAnimations() {
        const elements = document.querySelectorAll(
            '.service-card, .ai-card, .timeline-item, .skill-group, .beyond-card, .client-item, .about-text, .contact-info, .contact-form-wrap'
        );

        elements.forEach(el => el.classList.add('fade-in'));

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        elements.forEach(el => observer.observe(el));
    }

    // ---- Smooth Scroll for Nav Links ----
    function handleNavClick(e) {
        const href = e.target.getAttribute('href');
        if (href && href.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
                closeMenu();
            }
        }
    }

    // ---- Contact Form (placeholder) ----
    function handleFormSubmit(e) {
        e.preventDefault();
        const btn = e.target.querySelector('button[type="submit"]');
        const originalText = btn.textContent;
        btn.textContent = currentLang === 'no' ? 'Sendt!' : 'Sent!';
        btn.style.background = '#10b981';
        btn.disabled = true;

        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.background = '';
            btn.disabled = false;
            e.target.reset();
        }, 3000);
    }

    // ---- Initialize ----
    function init() {
        // Set language
        setLanguage(currentLang);

        // Scroll listener
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();

        // Language toggle
        document.getElementById('langToggle').addEventListener('click', () => {
            setLanguage(currentLang === 'en' ? 'no' : 'en');
        });

        // Mobile menu
        hamburger.addEventListener('click', toggleMenu);

        // Nav link clicks
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', handleNavClick);
        });

        // Close menu on outside click
        document.addEventListener('click', (e) => {
            if (navLinks.classList.contains('open') &&
                !navLinks.contains(e.target) &&
                !hamburger.contains(e.target)) {
                closeMenu();
            }
        });

        // Contact form
        const form = document.getElementById('contactForm');
        if (form) form.addEventListener('submit', handleFormSubmit);

        // Contact email — assembled at runtime so the plaintext address never
        // appears in the committed source (defeats repo email-harvesting bots).
        const emailLink = document.getElementById('cc-email');
        if (emailLink) {
            const addr = atob('ZGF2aWRzZW45MDhAZ21haWwuY29t');
            emailLink.href = 'mailto:' + addr;
            emailLink.textContent = addr;
        }

        // Scroll animations
        initScrollAnimations();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
