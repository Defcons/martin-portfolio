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

    // ---- Project Detail Modal ----
    function initModal() {
        const overlay = document.getElementById('projectModal');
        if (!overlay) return;

        const media = document.getElementById('modalMedia');
        const img = document.getElementById('modalImg');
        const thumbs = document.getElementById('modalThumbs');
        const badge = document.getElementById('modalBadge');
        const titleEl = document.getElementById('modalTitle');
        const descEl = document.getElementById('modalDesc');
        const privateEl = document.getElementById('modalPrivate');
        const actions = document.getElementById('modalActions');
        const closeBtn = document.getElementById('modalClose');

        const EXT_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6M10 14L21 3"/></svg>';

        let lastFocused = null;

        function buildThumbs(shots) {
            thumbs.innerHTML = '';
            if (shots.length < 2) return;
            shots.forEach((src, i) => {
                const t = document.createElement('img');
                t.src = src;
                t.alt = '';
                if (i === 0) t.classList.add('active');
                t.addEventListener('click', () => {
                    img.src = src;
                    thumbs.querySelectorAll('img').forEach(x => x.classList.remove('active'));
                    t.classList.add('active');
                });
                thumbs.appendChild(t);
            });
        }

        function buildActions(card) {
            actions.innerHTML = '';
            [['link', 'linkLabel'], ['link2', 'link2Label']].forEach(([hrefKey, labelKey]) => {
                const href = card.dataset[hrefKey];
                if (!href) return;
                const a = document.createElement('a');
                a.className = 'modal-link';
                a.href = href;
                a.target = '_blank';
                a.rel = 'noopener';
                a.innerHTML = (card.dataset[labelKey] || 'Visit') + ' ' + EXT_ICON;
                actions.appendChild(a);
            });
        }

        function openModal(card) {
            const shots = [card.dataset.shot, card.dataset.shot2].filter(Boolean);
            if (shots.length) {
                img.src = shots[0];
                img.alt = (card.querySelector('h3') || {}).textContent || '';
                img.classList.toggle('modal-img--contain', card.dataset.fit === 'contain');
                media.hidden = false;
                buildThumbs(shots);
            } else {
                media.hidden = true;
                thumbs.innerHTML = '';
            }

            const cardBadge = card.querySelector('.ai-badge');
            if (cardBadge) {
                let variant = 'modal-badge--muted';
                if (cardBadge.classList.contains('ai-badge--live')) variant = 'modal-badge--live';
                else if (cardBadge.classList.contains('ai-badge--dev')) variant = 'modal-badge--dev';
                badge.textContent = cardBadge.textContent;
                badge.className = 'modal-badge ' + variant;
                badge.hidden = false;
            } else {
                badge.hidden = true;
            }

            const h3 = card.querySelector('h3');
            const p = card.querySelector('p');
            titleEl.textContent = h3 ? h3.textContent : '';
            descEl.textContent = p ? p.textContent : '';

            privateEl.hidden = card.dataset.private !== '1';
            buildActions(card);

            lastFocused = document.activeElement;
            overlay.hidden = false;
            document.body.classList.add('modal-open');
            requestAnimationFrame(() => overlay.classList.add('open'));
            closeBtn.focus();
        }

        function closeModal() {
            overlay.classList.remove('open');
            document.body.classList.remove('modal-open');
            setTimeout(() => { overlay.hidden = true; img.src = ''; }, 250);
            if (lastFocused && lastFocused.focus) lastFocused.focus();
        }

        document.querySelectorAll('.ai-card--modal, .service-card--modal').forEach(card => {
            card.addEventListener('click', () => openModal(card));
            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    openModal(card);
                }
            });
        });

        closeBtn.addEventListener('click', closeModal);
        overlay.addEventListener('click', (e) => { if (e.target === overlay) closeModal(); });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !overlay.hidden) closeModal();
        });
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

        // Project detail modal
        initModal();

        // Scroll animations
        initScrollAnimations();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
