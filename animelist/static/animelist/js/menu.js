document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.getElementById('menuToggle');
    const nav = document.getElementById('mainNav');

    if (!toggle || !nav) {
        return;
    }

    function closeMenu() {
        nav.classList.remove('is-open');
        toggle.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
    }

    function openMenu() {
        nav.classList.add('is-open');
        toggle.classList.add('is-open');
        toggle.setAttribute('aria-expanded', 'true');
    }

    toggle.addEventListener('click', function () {
        const isOpen = nav.classList.contains('is-open');
        isOpen ? closeMenu() : openMenu();
    });

    nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', closeMenu);
    });

    document.addEventListener('click', function (event) {
        const clickedInsideNav = nav.contains(event.target);
        const clickedToggle = toggle.contains(event.target);
        if (!clickedInsideNav && !clickedToggle) {
            closeMenu();
        }
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            closeMenu();
        }
    });
});