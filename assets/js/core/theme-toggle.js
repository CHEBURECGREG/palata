// Theme management — Dark/Light mode with localStorage persistence
export function initTheme() {
  const html = document.documentElement;
  const themeBtn = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('theme');
  const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

  function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    if (themeBtn) {
      themeBtn.setAttribute('aria-label', theme === 'dark' ? 'Включить светлую тему' : 'Включить тёмную тему');
      themeBtn.setAttribute('aria-pressed', theme === 'dark');
    }
  }

  applyTheme(initialTheme);

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const current = html.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      localStorage.setItem('theme', next);
      applyTheme(next);
    });
  }

  // Listen for system preference changes (only if user hasn't set explicit preference)
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });

  return { applyTheme };
}