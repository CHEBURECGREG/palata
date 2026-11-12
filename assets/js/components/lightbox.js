// Lightbox component for gallery images
export class Lightbox {
  constructor() {
    this.currentIndex = 0;
    this.images = [];
    this.isOpen = false;
    this.elements = {};
    this.init();
  }

  init() {
    this.elements = {
      container: document.getElementById('lightbox'),
      img: document.getElementById('lightbox-img'),
      caption: document.getElementById('lightbox-caption'),
      close: document.getElementById('lightbox-close'),
      prev: document.getElementById('lightbox-prev'),
      next: document.getElementById('lightbox-next'),
      overlay: document.getElementById('lightbox-overlay'),
    };

    // Bind events
    this.elements.close?.addEventListener('click', () => this.close());
    this.elements.prev?.addEventListener('click', () => this.prev());
    this.elements.next?.addEventListener('click', () => this.next());
    this.elements.overlay?.addEventListener('click', () => this.close());

    document.addEventListener('keydown', (e) => this.handleKeydown(e));
  }

  open(index, images) {
    this.images = images;
    this.currentIndex = index;
    this.isOpen = true;
    this.render();
    this.elements.container.classList.add('open');
    document.body.style.overflow = 'hidden';
    // Focus management
    setTimeout(() => this.elements.close?.focus(), 100);
  }

  close() {
    this.isOpen = false;
    this.elements.container.classList.remove('open');
    document.body.style.overflow = '';
  }

  prev() {
    this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    this.render();
  }

  next() {
    this.currentIndex = (this.currentIndex + 1) % this.images.length;
    this.render();
  }

  render() {
    const current = this.images[this.currentIndex];
    if (!current) return;

    this.elements.img.src = current.src;
    this.elements.img.alt = current.alt;
    this.elements.caption.textContent = current.caption;
  }

  handleKeydown(e) {
    if (!this.isOpen) return;
    switch (e.key) {
      case 'Escape': this.close(); break;
      case 'ArrowLeft': this.prev(); break;
      case 'ArrowRight': this.next(); break;
    }
  }
}

// Global lightbox instance
let lightboxInstance = null;

export function initLightbox() {
  lightboxInstance = new Lightbox();

  // Delegate click on gallery images
  document.addEventListener('click', (e) => {
    const card = e.target.closest('.gallery-card');
    if (!card) return;

    const grid = card.closest('.gallery-grid');
    if (!grid) return;

    const cards = Array.from(grid.querySelectorAll('.gallery-card'));
    const index = cards.indexOf(card);
    if (index === -1) return;

    const images = cards.map(c => ({
      src: c.dataset.fullImage || c.querySelector('img')?.src,
      alt: c.querySelector('img')?.alt || '',
      caption: c.dataset.caption || c.querySelector('.gallery-caption-text')?.textContent || '',
    }));

    lightboxInstance.open(index, images);
  });

  return lightboxInstance;
}