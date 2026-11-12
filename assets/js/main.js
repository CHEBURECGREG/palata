// Main entry point — initializes all modules
import { initTheme } from './core/theme-toggle.js';
import { initAccessibility } from './core/accessibility.js';
import { initNavigation } from './core/navigation.js';
import { initLightbox } from './components/lightbox.js';
import { initAccordions } from './components/accordion.js';
import { initImageFallbacks } from './components/image-fallback.js';
import { initGallery } from './components/gallery-renderer.js';

document.addEventListener('DOMContentLoaded', () => {
  // Core systems
  initTheme();
  initAccessibility();
  initNavigation();

  // Components
  initLightbox();
  initAccordions();
  initImageFallbacks();
  initGallery();

  // Announce page ready
  console.log('«Международная палата личности» — initialized');
});