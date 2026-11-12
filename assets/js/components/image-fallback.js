// Image fallback handler — replaces broken images with styled placeholders
export function initImageFallbacks() {
  const images = document.querySelectorAll('img[data-placeholder]');

  images.forEach(img => {
    // If already has natural dimensions, it loaded fine
    if (img.complete && img.naturalWidth > 0) return;

    const placeholderText = img.dataset.placeholder || 'Изображение';

    img.addEventListener('error', () => {
      // Prevent infinite loop
      if (img.dataset.fallbackApplied === 'true') return;
      img.dataset.fallbackApplied = 'true';

      // Create placeholder
      const wrapper = document.createElement('div');
      wrapper.className = 'img-placeholder';
      wrapper.setAttribute('role', 'img');
      wrapper.setAttribute('aria-label', img.alt || placeholderText);
      wrapper.textContent = placeholderText;

      // Preserve aspect ratio if specified
      if (img.dataset.aspectRatio) {
        const [w, h] = img.dataset.aspectRatio.split('/').map(Number);
        if (w && h) {
          wrapper.style.aspectRatio = `${w}/${h}`;
        }
      }

      // Replace image with placeholder
      img.parentNode?.replaceChild(wrapper, img);
    });

    // Also handle load event to remove loading state
    img.addEventListener('load', () => {
      img.classList.add('loaded');
    });
  });
}