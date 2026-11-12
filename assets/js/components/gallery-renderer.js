// Gallery data renderer — builds gallery grid from JSON
export function initGallery() {
  const grid = document.getElementById('gallery-grid');
  if (!grid) return;

  fetch('data/gallery.json')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load gallery data');
      return res.json();
    })
    .then(data => {
      const items = data.gallery;
      const baseUrl = data.baseImageUrl;

      grid.innerHTML = items.map((item, index) => {
        const src = baseUrl + item.file;
        const aspectRatio = `${item.width}/${item.height}`;
        return `
          <article class="gallery-card fade-in stagger-${(index % 5) + 1}"
                   data-caption="${escapeHtml(item.caption)}"
                   data-full-image="${escapeHtml(src)}"
                   data-category="${escapeHtml(item.category)}">
            <div class="gallery-card-inner">
              <img class="gallery-img"
                   src="${escapeHtml(src)}"
                   alt="${escapeHtml(item.alt)}"
                   loading="lazy"
                   data-placeholder="${escapeHtml(item.caption)}"
                   data-aspect-ratio="${aspectRatio}"
                   width="${item.width}"
                   height="${item.height}">
              <span class="gallery-category-badge">${escapeHtml(item.category)}</span>
              <div class="gallery-overlay">
                <p class="gallery-caption-overlay">${escapeHtml(item.caption)}</p>
              </div>
            </div>
            <figcaption class="gallery-caption-text">${escapeHtml(item.caption)}</figcaption>
          </article>
        `;
      }).join('');

      // Re-initialize image fallbacks for new images
      if (typeof initImageFallbacks === 'function') {
        initImageFallbacks();
      }
    })
    .catch(err => {
      console.error('Gallery load error:', err);
      grid.innerHTML = '<p class="error-message">Не удалось загрузить галерею. Пожалуйста, попробуйте позже.</p>';
    });
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}