document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const navToggle = document.querySelector('.nav-toggle');
  const navPanel = document.querySelector('.nav-panel');
  const links = document.querySelectorAll('.nav-links a, .nav-cta');
  const galleryGrid = document.getElementById('gallery-grid');
  const lightbox = document.getElementById('lightbox');
  const lightboxImage = lightbox ? lightbox.querySelector('img') : null;
  const lightboxClose = document.querySelector('.lightbox-close');
  const prevButton = document.querySelector('.lightbox-prev');
  const nextButton = document.querySelector('.lightbox-next');
  const contactList = document.getElementById('contact-list');
  const reservationContactList = document.getElementById('reservation-contact-list');
  const reservationForm = document.getElementById('reservation-form');
  const contactForm = document.getElementById('contact-form');

  const hero = document.querySelector('.hero');
  const reservationHero = document.querySelector('.reservation-hero');
  const contactHero = document.querySelector('.contact-hero');
  const experienceImage = document.querySelector('.experience-visual img');

  if (hero && siteConfig && siteConfig.heroImage) {
    hero.style.backgroundImage = `url('${siteConfig.heroImage}')`;
  }

  if (reservationHero && siteConfig && siteConfig.heroImage) {
    reservationHero.style.backgroundImage = `url('${siteConfig.heroImage}')`;
  }

  if (contactHero && siteConfig && siteConfig.heroImage) {
    contactHero.style.backgroundImage = `url('${siteConfig.heroImage}')`;
  }

  if (experienceImage && siteConfig && siteConfig.experienceImage) {
    experienceImage.src = siteConfig.experienceImage;
  }

  function renderContactList() {
    const items = [
      siteConfig.address,
      siteConfig.phones.join(' • '),
      siteConfig.email
    ];

    const targetList = contactList || reservationContactList;
    if (!targetList) return;

    targetList.innerHTML = items.map((item) => `<li>${item}</li>`).join('');
  }

  function updateHeaderState() {
    if (!header) return;
    const isScrolled = window.scrollY > 20;
    header.classList.toggle('scrolled', isScrolled);
  }

  function toggleMenu(forceOpen) {
    if (!navToggle || !navPanel) return;
    const willOpen = typeof forceOpen === 'boolean' ? forceOpen : !navPanel.classList.contains('is-open');
    navPanel.classList.toggle('is-open', willOpen);
    navToggle.setAttribute('aria-expanded', String(willOpen));
  }

  function buildGallery() {
    if (!galleryGrid || !siteConfig || !siteConfig.gallery) return;

    const items = siteConfig.gallery.map((item, index) => {
      const sizeClass = index % 5 === 0 ? 'wide' : index % 3 === 0 ? 'tall' : '';

      return `
        <figure class="gallery-item ${sizeClass}" data-category="${item.category}" tabindex="0" data-index="${index}">
          <img src="${item.src}" alt="${item.title}" loading="lazy" />
          <figcaption>
            <span>${item.category}</span>
            <strong>${item.title}</strong>
          </figcaption>
        </figure>
      `;
    });

    galleryGrid.innerHTML = items.join('');
    attachGalleryEvents();
  }

  function attachGalleryEvents() {
    const galleryItems = document.querySelectorAll('.gallery-item');

    galleryItems.forEach((item) => {
      item.addEventListener('click', () => openLightbox(Number(item.dataset.index)));
      item.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          openLightbox(Number(item.dataset.index));
        }
      });
    });
  }

  let currentGalleryIndex = 0;

  function openLightbox(index) {
    if (!lightbox || !lightboxImage || !siteConfig || !siteConfig.gallery) return;
    const galleryItems = siteConfig.gallery;
    currentGalleryIndex = index;
    lightboxImage.src = galleryItems[index].src;
    lightboxImage.alt = galleryItems[index].title;
    lightbox.classList.add('show');
    lightbox.setAttribute('aria-hidden', 'false');
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('show');
    lightbox.setAttribute('aria-hidden', 'true');
  }

  function changeGalleryImage(direction) {
    if (!siteConfig || !siteConfig.gallery || !lightboxImage) return;
    const total = siteConfig.gallery.length;
    currentGalleryIndex = (currentGalleryIndex + direction + total) % total;
    lightboxImage.src = siteConfig.gallery[currentGalleryIndex].src;
    lightboxImage.alt = siteConfig.gallery[currentGalleryIndex].title;
  }

  function filterGallery(category) {
    const items = document.querySelectorAll('.gallery-item');

    items.forEach((item) => {
      const match = category === 'all' || item.dataset.category === category;
      item.style.display = match ? 'block' : 'none';
    });
  }

  function sendWhatsAppMessage(fields) {
    const message = encodeURIComponent(fields.join('\n'));
    window.open(`https://wa.me/22890246655?text=${message}`, '_blank', 'noopener,noreferrer');
  }

  const filterButtons = document.querySelectorAll('.filter');
  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      filterButtons.forEach((btn) => btn.classList.toggle('active', btn === button));
      filterGallery(button.dataset.filter);
    });
  });

  if (navToggle) {
    navToggle.addEventListener('click', () => toggleMenu());
  }

  links.forEach((link) => {
    link.addEventListener('click', () => toggleMenu(false));
  });

  if (lightboxClose) {
    lightboxClose.addEventListener('click', closeLightbox);
  }

  if (prevButton) {
    prevButton.addEventListener('click', () => changeGalleryImage(-1));
  }

  if (nextButton) {
    nextButton.addEventListener('click', () => changeGalleryImage(1));
  }

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && lightbox && lightbox.classList.contains('show')) {
      closeLightbox();
    }

    if (event.key === 'ArrowLeft' && lightbox && lightbox.classList.contains('show')) {
      changeGalleryImage(-1);
    }

    if (event.key === 'ArrowRight' && lightbox && lightbox.classList.contains('show')) {
      changeGalleryImage(1);
    }
  });

  if (lightbox) {
    lightbox.addEventListener('click', (event) => {
      if (event.target === lightbox) {
        closeLightbox();
      }
    });
  }

  if (reservationForm) {
    reservationForm.addEventListener('submit', (event) => {
      event.preventDefault();

      const formData = new FormData(reservationForm);
      const name = formData.get('name') || 'Client';
      const phone = formData.get('phone') || 'Non renseigné';
      const guests = formData.get('guests') || '1';
      const date = formData.get('date') || 'Date à confirmer';
      const time = formData.get('time') || 'Heure à confirmer';
      const occasion = formData.get('occasion') || 'Non précisée';
      const message = formData.get('message') || 'Aucune demande complémentaire';

      sendWhatsAppMessage([
        'Bonjour ALIS Lounge BAR, je souhaite réserver une table.',
        `Nom : ${name}`,
        `Téléphone : ${phone}`,
        `Nombre de personnes : ${guests}`,
        `Date : ${date}`,
        `Heure : ${time}`,
        `Occasion : ${occasion}`,
        `Message : ${message}`
      ]);
      reservationForm.reset();
    });
  }

  if (contactForm) {
    contactForm.addEventListener('submit', (event) => {
      event.preventDefault();

      const formData = new FormData(contactForm);
      const name = formData.get('name') || 'Client';
      const phone = formData.get('phone') || 'Non renseigné';
      const subject = formData.get('subject') || 'Demande';
      const email = formData.get('email') || 'Non renseigné';
      const message = formData.get('message') || 'Aucune demande complémentaire';

      sendWhatsAppMessage([
        'Bonjour ALIS Lounge BAR, je souhaite vous contacter.',
        `Nom : ${name}`,
        `Téléphone : ${phone}`,
        `Email : ${email}`,
        `Objet : ${subject}`,
        `Message : ${message}`
      ]);
      contactForm.reset();
    });
  }

  window.addEventListener('scroll', updateHeaderState);
  updateHeaderState();
  renderContactList();
  buildGallery();
  if (galleryGrid) {
    filterGallery('all');
  }
});
