document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-links a');
    const currentPath = window.location.pathname;
    
    // Default to index if root
    const normalizedPath = currentPath.endsWith('/') ? currentPath + 'index.html' : currentPath;

    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (normalizedPath.includes(linkPath) && linkPath !== '/') {
            link.classList.add('active');
        } else if (normalizedPath === '/' || normalizedPath === '/index.html') {
             if (link.getAttribute('href') === 'index.html') {
                 link.classList.add('active');
             }
        }
    });

    // Sticky Navigation Shadow Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                navbar.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.1)';
            } else {
                navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
            }
        });
    }
});

function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    if (navLinks) {
        navLinks.classList.toggle('active');
    }
}
