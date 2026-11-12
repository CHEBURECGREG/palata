// Navigation — mobile hamburger, sidebar, nav panel
export function initNavigation() {
  const navToggle = document.getElementById('nav-toggle');
  const navPanel = document.getElementById('nav-panel');
  const navOverlay = document.getElementById('nav-overlay');
  const navClose = document.getElementById('nav-close');
  const navLinks = navPanel?.querySelectorAll('a');

  function openNav() {
    navToggle?.setAttribute('aria-expanded', 'true');
    navPanel?.classList.add('open');
    navOverlay?.classList.add('open');
    document.body.style.overflow = 'hidden';
    // Focus management
    setTimeout(() => navClose?.focus(), 100);
  }

  function closeNav() {
    navToggle?.setAttribute('aria-expanded', 'false');
    navPanel?.classList.remove('open');
    navOverlay?.classList.remove('open');
    document.body.style.overflow = '';
  }

  navToggle?.addEventListener('click', () => {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    expanded ? closeNav() : openNav();
  });

  navClose?.addEventListener('click', closeNav);
  navOverlay?.addEventListener('click', closeNav);

  navLinks?.forEach(link => {
    link.addEventListener('click', () => {
      // Close on internal link click
      if (link.getAttribute('href')?.startsWith('#') || link.getAttribute('href')?.endsWith('.html')) {
        closeNav();
      }
    });
  });

  // Keyboard trap in nav panel
  navPanel?.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeNav();
  });

  // Close on resize to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) closeNav();
  });

  return { openNav, closeNav };
}