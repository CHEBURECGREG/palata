// Accessibility / high-contrast mode with localStorage persistence
export function initAccessibility() {
  const html = document.documentElement;
  const accessBtn = document.getElementById('access-toggle');
  const savedAccess = localStorage.getItem('accessibility');
  const initialAccess = savedAccess === 'true';

  function applyAccessibility(enabled) {
    html.setAttribute('data-accessibility', enabled);
    if (accessBtn) {
      accessBtn.setAttribute('aria-label', enabled ? 'Отключить версию для слабовидящих' : 'Включить версию для слабовидящих');
      accessBtn.setAttribute('aria-pressed', enabled);
      accessBtn.classList.toggle('active', enabled);
    }
    // Force reflow for CSS transitions
    document.body.style.display = 'none';
    document.body.offsetHeight;
    document.body.style.display = '';
  }

  applyAccessibility(initialAccess);

  if (accessBtn) {
    accessBtn.addEventListener('click', () => {
      const current = html.getAttribute('data-accessibility') === 'true';
      const next = !current;
      localStorage.setItem('accessibility', next);
      applyAccessibility(next);
    });
  }

  return { applyAccessibility };
}