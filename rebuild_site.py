from pathlib import Path

root = Path(r'F:\PROJETS\ALIS_LOUNGE_BAR')

index_html = '''<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta
      name="description"
      content="ALIS Lounge BAR — un espace haut de gamme à Lomé, dédié à une expérience lounge élégante et conviviale."
    />
    <title>ALIS Lounge BAR | Lomé</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <header class="site-header">
      <nav class="nav container" aria-label="Navigation principale">
        <a href="#home" class="brand" aria-label="ALIS Lounge BAR Accueil">
          <span class="brand-mark">ALIS</span>
        </a>

        <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>

        <div class="nav-panel">
          <ul class="nav-links">
            <li><a href="#home">Accueil</a></li>
            <li><a href="#experience">L'expérience</a></li>
            <li><a href="#gallery">Galerie</a></li>
            <li><a href="#menu">Menu</a></li>
            <li><a href="#events">Événements</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>

          <a href="reservation.html" class="btn btn-primary nav-cta">Réserver une table</a>
        </div>
      </nav>
    </header>

    <main>
      <section id="home" class="hero">
        <div class="hero-overlay"></div>
        <div class="container hero-inner">
          <div class="eyebrow">Lomé • Nyékonakpoè</div>
          <h1>ALIS LOUNGE BAR</h1>
          <p class="hero-tagline">L'élégance de vos instants.</p>
          <p class="hero-copy">
            Un lieu, une atmosphère, une expérience. Découvrez un espace dédié à vos
            moments de détente et de convivialité à Lomé.
          </p>

          <div class="hero-actions">
            <a href="#experience" class="btn btn-primary">Découvrir l'expérience</a>
            <a href="reservation.html" class="btn btn-secondary">Réserver une table</a>
          </div>

          <div class="hero-meta">
            <span>Ambiance premium</span>
            <span>Soirées élégantes</span>
            <span>Accueil sur mesure</span>
          </div>
        </div>

        <div class="container hero-summary">
          <article>
            <span>Lieu</span>
            <strong>Nyékonakpoè</strong>
          </article>
          <article>
            <span>Ambiance</span>
            <strong>Premium lounge</strong>
          </article>
          <article>
            <span>Expérience</span>
            <strong>Convivialité</strong>
          </article>
        </div>

        <a href="#experience" class="scroll-indicator" aria-label="Voir la suite">
          <span class="scroll-line"></span>
          <span class="scroll-label">Scroll</span>
        </a>
      </section>

      <section id="experience" class="section experience">
        <div class="container experience-grid">
          <div class="experience-visual">
            <img
              src="https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=1200&q=80"
              alt="Ambiance lounge premium"
            />
          </div>

          <div class="experience-content">
            <p class="section-kicker">L'EXPÉRIENCE ALIS</p>
            <h2>Bienvenue dans l'univers ALIS</h2>
            <p>
              ALIS Lounge BAR est conçu comme un refuge urbain où l'élégance se mêle
              au plaisir de partager un moment de détente et d'échange. L'ambiance,
              la lumière douce et le cadre accueillant créent une expérience dédiée à la
              convivialité, au ressourcement et à l'exceptionnel.
            </p>
            <p>
              Bien plus qu'un simple lieu de rencontre, l'établissement cherche à offrir
              des instants mémorables, inspirés par le luxe discret et le confort d'un
              espace pensé pour accueillir les soirées, les pauses faciles et les grands
              moments entre amis.
            </p>

            <div class="experience-pills">
              <span>Atmosphère raffinée</span>
              <span>Moment de détente</span>
              <span>Convivialité</span>
            </div>
          </div>
        </div>
      </section>

      <section class="section signature-section">
        <div class="container">
          <div class="section-heading">
            <p class="section-kicker">L'ART DE VIVRE</p>
            <h2>Des soirées pensées pour les instants précieux</h2>
          </div>

          <div class="signature-grid">
            <article class="signature-card">
              <div class="signature-icon">01</div>
              <h3>Ambiance lounge</h3>
              <p>Un cadre élégant et immersif pensé pour recharger les sens et partager des moments réellement hors du temps.</p>
            </article>
            <article class="signature-card">
              <div class="signature-icon">02</div>
              <h3>Convivialité</h3>
              <p>Une expérience ouverte à la rencontre, à la discussion et à la détente dans un esprit contemporain.</p>
            </article>
            <article class="signature-card accent-card">
              <div class="signature-icon">03</div>
              <h3>Réservations</h3>
              <p>Un accueil pensé pour accueillir les soirées, les dîners et les instants privés selon les disponibilités.</p>
            </article>
          </div>
        </div>
      </section>

      <section id="gallery" class="section gallery-section">
        <div class="container">
          <div class="section-heading">
            <p class="section-kicker">GALLERIE</p>
            <h2>Une atmosphère qui se raconte en images</h2>
          </div>

          <div class="gallery-filters" aria-label="Filtres galerie">
            <button class="filter active" data-filter="all">Tout</button>
            <button class="filter" data-filter="Ambiance">Ambiance</button>
            <button class="filter" data-filter="Cocktails">Cocktails</button>
            <button class="filter" data-filter="Intérieur">Intérieur</button>
            <button class="filter" data-filter="Événements">Événements</button>
          </div>

          <div id="gallery-grid" class="gallery-grid" aria-live="polite"></div>
        </div>
      </section>

      <section id="menu" class="section menu-section">
        <div class="container">
          <div class="section-heading align-left">
            <p class="section-kicker">MENU</p>
            <h2>Une expérience pensée pour les instants précieux</h2>
          </div>

          <div class="menu-grid">
            <article class="menu-card">
              <div class="menu-card__label">À venir</div>
              <h3>Cocktails & signatures</h3>
              <p>
                Une sélection de boissons et de créations à personnaliser selon les
                préférences et les offres confirmées pour l'établissement.
              </p>
            </article>

            <article class="menu-card">
              <div class="menu-card__label">À confirmer</div>
              <h3>Ambiance & services</h3>
              <p>
                Les prestations et formules exactes seront mises à jour dès que les
                informations officielles du lounge seront validées.
              </p>
            </article>

            <article class="menu-card accent-card">
              <div class="menu-card__label">Important</div>
              <h3>Contenus temporaires</h3>
              <p>
                Les éléments de menu, tarifs et offres sont volontairement laissés flexibles
                pour permettre une mise à jour rapide et fidèle à la réalité de l'établissement.
              </p>
            </article>
          </div>
        </div>
      </section>

      <section id="events" class="section events-section">
        <div class="container">
          <div class="section-heading">
            <p class="section-kicker">ÉVÉNEMENTS</p>
            <h2>Des soirées à créer ensemble</h2>
          </div>

          <div class="events-grid">
            <article class="event-card event-card--large">
              <div class="event-badge">À venir</div>
              <h3>Soirées lounge</h3>
              <p>
                Des moments de musique, de convivialité et d'élégance, pensés pour offrir
                un cadre convivial et premium à chaque visite.
              </p>
            </article>

            <article class="event-card">
              <div class="event-badge">À confirmer</div>
              <h3>Programmes spéciaux</h3>
              <p>Des animations et offres qui seront ajoutées selon les actualités de l'établissement.</p>
            </article>

            <article class="event-card">
              <div class="event-badge">À personnaliser</div>
              <h3>Réservations privées</h3>
              <p>Pour des rencontres, célébrations et moments sur mesure, le contact direct reste privilégié.</p>
            </article>
          </div>
        </div>
      </section>
    </main>

    <footer id="contact" class="site-footer">
      <div class="container footer-grid">
        <div class="footer-branding">
          <div class="brand brand-footer">
            <span class="brand-mark">ALIS</span>
          </div>
          <p>
            Un espace de détente et de convivialité pensé pour des instants hors du temps à Lomé.
          </p>
        </div>

        <div class="footer-contact">
          <h3>Contact</h3>
          <ul id="contact-list" class="contact-list"></ul>
        </div>

        <div class="footer-cta">
          <h3>Réservation</h3>
          <p>Pour réserver une table ou demander un renseignement, contactez-nous directement.</p>
          <div class="footer-actions">
            <a href="reservation.html" class="btn btn-primary">Réserver</a>
            <a href="contact.html" class="btn btn-secondary">Contact</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="container footer-bottom-inner">
          <span>© 2025 ALIS Lounge BAR</span>
          <span>Nyékonakpoè • Lomé • Togo</span>
        </div>
      </div>
    </footer>

    <a
      href="https://wa.me/22890246655?text=Bonjour%20ALIS%20Lounge%20BAR%2C%20je%20souhaite%20r%C3%A9server%20une%20table."
      class="whatsapp-float"
      target="_blank"
      rel="noreferrer"
      aria-label="Contact WhatsApp"
    >
      WhatsApp
    </a>

    <div id="lightbox" class="lightbox" aria-hidden="true">
      <button class="lightbox-close" aria-label="Fermer la galerie">×</button>
      <button class="lightbox-nav lightbox-prev" aria-label="Image précédente">‹</button>
      <img src="" alt="" />
      <button class="lightbox-nav lightbox-next" aria-label="Image suivante">›</button>
    </div>

    <script src="config.js"></script>
    <script src="script.js"></script>
  </body>
</html>
'''

contact_html = '''<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta
      name="description"
      content="Contactez ALIS Lounge BAR à Lomé. Réservez une table ou demandez un renseignement directement."
    />
    <title>Contact | ALIS Lounge BAR</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body class="contact-page">
    <header class="site-header">
      <nav class="nav container" aria-label="Navigation principale">
        <a href="index.html" class="brand" aria-label="ALIS Lounge BAR Accueil">
          <span class="brand-mark">ALIS</span>
        </a>

        <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>

        <div class="nav-panel">
          <ul class="nav-links">
            <li><a href="index.html#home">Accueil</a></li>
            <li><a href="index.html#experience">L'expérience</a></li>
            <li><a href="index.html#gallery">Galerie</a></li>
            <li><a href="index.html#menu">Menu</a></li>
            <li><a href="index.html#events">Événements</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>

          <a href="reservation.html" class="btn btn-primary nav-cta">Réserver une table</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="contact-hero">
        <div class="contact-overlay"></div>
        <div class="container contact-hero-content">
          <p class="section-kicker">Contact</p>
          <h1>Échangez avec ALIS</h1>
          <p>Nous sommes à votre écoute pour préparer un moment unique, intime ou festif à Lomé.</p>
        </div>
      </section>

      <section class="container contact-shell">
        <div class="contact-card contact-infos">
          <div class="reservation-card__head">
            <p class="section-kicker">Coordonnées</p>
            <h2>Nous joindre</h2>
          </div>

          <ul id="reservation-contact-list" class="contact-list"></ul>

          <div class="contact-badges">
            <span>Réservation</span>
            <span>Événements</span>
            <span>Prestations</span>
          </div>
        </div>

        <div class="contact-card contact-form-card">
          <div class="reservation-card__head">
            <p class="section-kicker">Demande rapide</p>
            <h2>Une question ?</h2>
          </div>

          <form id="contact-form" class="reservation-form">
            <div class="form-grid">
              <label class="field">
                <span>Nom</span>
                <input type="text" name="name" placeholder="Votre nom" required />
              </label>

              <label class="field">
                <span>Téléphone</span>
                <input type="tel" name="phone" placeholder="+228 ..." required />
              </label>

              <label class="field">
                <span>Objet</span>
                <select name="subject">
                  <option value="Réservation">Réservation</option>
                  <option value="Question">Question</option>
                  <option value="Événement">Événement</option>
                  <option value="Autre">Autre</option>
                </select>
              </label>

              <label class="field">
                <span>Email</span>
                <input type="email" name="email" placeholder="Votre email" />
              </label>
            </div>

            <label class="field field-full">
              <span>Message</span>
              <textarea name="message" rows="5" placeholder="Décrivez votre demande..." required></textarea>
            </label>

            <div class="reservation-actions">
              <button type="submit" class="btn btn-primary">Envoyer</button>
              <a href="https://wa.me/22890246655?text=Bonjour%20ALIS%20Lounge%20BAR%2C%20je%20souhaite%20vous%20contacter." class="btn btn-secondary" target="_blank" rel="noreferrer">WhatsApp</a>
            </div>
          </form>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="footer-bottom">
        <div class="container footer-bottom-inner">
          <span>© 2025 ALIS Lounge BAR</span>
          <span>Nyékonakpoè • Lomé • Togo</span>
        </div>
      </div>
    </footer>

    <script src="config.js"></script>
    <script src="script.js"></script>
  </body>
</html>
'''

styles = ''' :root {
  --bg: #101010;
  --bg-soft: #191919;
  --surface: rgba(25, 25, 25, 0.82);
  --surface-light: #1f1f1f;
  --text: #f5f0e7;
  --text-soft: rgba(245, 240, 231, 0.72);
  --gold: #c6a46a;
  --gold-soft: rgba(198, 164, 106, 0.18);
  --line: rgba(255, 255, 255, 0.08);
  --shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
  --container: min(1180px, calc(100vw - 48px));
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  overflow-x: hidden;
}

img {
  width: 100%;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
}

button,
input,
select,
textarea {
  font: inherit;
}

.container {
  width: var(--container);
  margin: 0 auto;
}

.section {
  padding: 120px 0;
}

.section-kicker {
  font-size: 0.75rem;
  letter-spacing: 0.22rem;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 18px;
}

h1, h2, h3 {
  font-family: 'Cormorant Garamond', serif;
  line-height: 0.96;
  font-weight: 600;
}

h2 {
  font-size: clamp(2.5rem, 4vw, 4.3rem);
  margin-bottom: 20px;
}

p {
  color: var(--text-soft);
  font-size: 1.05rem;
}

.site-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  transition: background 0.35s ease, box-shadow 0.35s ease;
}

.site-header.scrolled {
  background: rgba(16, 16, 16, 0.9);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
  backdrop-filter: blur(12px);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 86px;
  gap: 20px;
}

.brand {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.brand-mark {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2rem, 2vw, 2.4rem);
  letter-spacing: 0.24rem;
  color: var(--text);
}

.nav-panel {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-links {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-links a {
  color: var(--text-soft);
  font-size: 0.82rem;
  letter-spacing: 0.12rem;
  text-transform: uppercase;
  transition: color 0.2s ease;
}

.nav-links a:hover,
.nav-links a:focus-visible {
  color: var(--text);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 50px;
  padding: 0 1.6rem;
  border-radius: 999px;
  font-size: 0.78rem;
  letter-spacing: 0.08rem;
  text-transform: uppercase;
  transition: transform 0.25s ease, background 0.25s ease, border-color 0.25s ease;
}

.btn:hover,
.btn:focus-visible {
  transform: translateY(-1px);
}

.btn-primary {
  background: linear-gradient(135deg, var(--gold), #d8b990);
  color: var(--bg);
  box-shadow: 0 12px 30px rgba(198, 164, 106, 0.25);
}

.btn-secondary {
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: var(--text);
  background: rgba(255, 255, 255, 0.02);
}

.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url('https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1800&q=80');
  background-position: center;
  background-size: cover;
  isolation: isolate;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(16, 16, 16, 0.82), rgba(16,16,16,0.48), rgba(16,16,16,0.2));
  z-index: 0;
}

.hero-inner {
  position: relative;
  z-index: 1;
  max-width: 760px;
  padding-top: 120px;
  padding-bottom: 80px;
}

.eyebrow {
  display: inline-flex;
  padding: 0.55rem 0.9rem;
  border: 1px solid rgba(255,255,255,0.2);
  background: rgba(255,255,255,0.04);
  border-radius: 999px;
  text-transform: uppercase;
  letter-spacing: 0.16rem;
  font-size: 0.7rem;
  margin-bottom: 1.4rem;
}

.hero h1 {
  font-size: clamp(4rem, 7vw, 8rem);
  letter-spacing: -0.04em;
  margin-bottom: 1rem;
}

.hero-tagline {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2.2rem, 3.3vw, 3.9rem);
  color: var(--text);
  line-height: 1;
  margin-bottom: 1rem;
}

.hero-copy {
  max-width: 680px;
  font-size: 1.08rem;
  color: rgba(245, 240, 231, 0.8);
  margin-bottom: 2rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-bottom: 2.3rem;
}

.hero-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  color: rgba(245, 240, 231, 0.75);
  font-size: 0.82rem;
  letter-spacing: 0.07rem;
  text-transform: uppercase;
}

.hero-meta span {
  position: relative;
  padding-right: 18px;
}

.hero-meta span:not(:last-child)::after {
  content: '•';
  position: absolute;
  right: 0;
  top: 0;
  color: var(--gold);
}

.hero-summary {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  margin-top: -30px;
  padding-bottom: 40px;
}

.hero-summary article {
  padding: 22px 24px;
  background: rgba(17, 17, 17, 0.68);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  backdrop-filter: blur(8px);
}

.hero-summary span {
  display: block;
  color: var(--gold);
  font-size: 0.7rem;
  letter-spacing: 0.12rem;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.hero-summary strong {
  font-size: 1.1rem;
  font-weight: 600;
}

.scroll-indicator {
  position: absolute;
  bottom: 34px;
  left: 50%;
  transform: translateX(-50%);
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: rgba(255,255,255,0.7);
  text-transform: uppercase;
  letter-spacing: 0.16rem;
  font-size: 0.65rem;
}

.scroll-line {
  width: 1px;
  height: 70px;
  background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,1), rgba(255,255,255,0));
  animation: pulse 1.8s ease-in-out infinite;
}

@keyframes pulse {
  0% { opacity: 0.3; transform: scaleY(0.7); }
  50% { opacity: 1; transform: scaleY(1); }
  100% { opacity: 0.3; transform: scaleY(0.7); }
}

.experience {
  background: linear-gradient(180deg, rgba(17,17,17,1), rgba(19,19,19,1));
}

.experience-grid {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 58px;
  align-items: center;
}

.experience-visual img {
  height: 680px;
  object-fit: cover;
  border-radius: 22px;
  box-shadow: var(--shadow);
}

.experience-content {
  padding-right: 20px;
}

.experience-content p + p {
  margin-top: 1.3rem;
}

.experience-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 2rem;
}

.experience-pills span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.68rem 1rem;
  border-radius: 999px;
  background: rgba(198, 164, 106, 0.08);
  border: 1px solid rgba(198, 164, 106, 0.24);
  color: var(--text);
  font-size: 0.75rem;
  letter-spacing: 0.08rem;
  text-transform: uppercase;
}

.signature-section {
  background: rgba(255,255,255,0.02);
}

.section-heading {
  text-align: center;
  margin-bottom: 48px;
}

.align-left {
  text-align: left;
}

.signature-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.signature-card {
  padding: 32px 26px;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  background: rgba(255,255,255,0.015);
  box-shadow: var(--shadow);
}

.signature-card h3 {
  font-size: clamp(2.2rem, 3vw, 3rem);
  margin-bottom: 12px;
}

.signature-icon {
  display: inline-flex;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  align-items: center;
  justify-content: center;
  background: rgba(198,164,106,0.12);
  border: 1px solid rgba(198,164,106,0.3);
  color: var(--gold);
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 14px;
}

.gallery-section {
  background: rgba(255,255,255,0.01);
}

.gallery-filters {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 32px;
}

.filter {
  border: 1px solid rgba(255,255,255,0.08);
  background: transparent;
  color: var(--text-soft);
  padding: 0.75rem 1.1rem;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.72rem;
  letter-spacing: 0.08rem;
  text-transform: uppercase;
}

.filter.active,
.filter:hover {
  background: rgba(198, 164, 106, 0.12);
  color: var(--text);
  border-color: rgba(198, 164, 106, 0.35);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 16px;
}

.gallery-item {
  grid-column: span 4;
  position: relative;
  overflow: hidden;
  border-radius: 18px;
  cursor: pointer;
  min-height: 300px;
  background: #111;
}

.gallery-item.tall {
  grid-column: span 3;
  min-height: 420px;
}

.gallery-item.wide {
  grid-column: span 6;
  min-height: 360px;
}

.gallery-item img {
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease, filter 0.5s ease;
}

.gallery-item::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.68), rgba(0,0,0,0));
}

.gallery-item:hover img,
.gallery-item:focus-visible img {
  transform: scale(1.05);
}

.gallery-item figcaption {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 18px;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 20px;
}

.gallery-item figcaption span {
  font-size: 0.72rem;
  letter-spacing: 0.1rem;
  text-transform: uppercase;
  color: rgba(255,255,255,0.72);
}

.gallery-item figcaption strong {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(1.5rem, 2vw, 2.15rem);
  line-height: 1;
}

.menu-section {
  background: linear-gradient(180deg, rgba(17, 17, 17, 0.95), rgba(16,16,16,1));
}

.menu-grid,
.events-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.menu-card,
.event-card {
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 30px 26px;
  box-shadow: var(--shadow);
}

.accent-card {
  background: linear-gradient(135deg, rgba(198,164,106,0.12), rgba(255,255,255,0.02));
  border-color: rgba(198,164,106,0.35);
}

.menu-card__label,
.event-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 0.85rem;
  border-radius: 999px;
  border: 1px solid rgba(198,164,106,0.3);
  background: rgba(198,164,106,0.08);
  color: var(--gold);
  font-size: 0.65rem;
  letter-spacing: 0.1rem;
  text-transform: uppercase;
  margin-bottom: 1.1rem;
}

.menu-card h3,
.event-card h3 {
  font-size: clamp(2.1rem, 3vw, 2.8rem);
  margin-bottom: 0.75rem;
}

.event-card--large {
  min-height: 240px;
}

.site-footer {
  background: #0d0d0d;
  border-top: 1px solid var(--line);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1.1fr 1.1fr;
  gap: 30px;
  padding: 80px 0 40px;
}

.footer-branding p,
.footer-cta p,
.contact-list li {
  color: var(--text-soft);
}

.brand-footer {
  margin-bottom: 18px;
}

.footer-contact h3,
.footer-cta h3 {
  font-size: 2.2rem;
  margin-bottom: 16px;
}

.contact-list {
  list-style: none;
  display: grid;
  gap: 14px;
}

.contact-list li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.contact-list li::before {
  content: '•';
  color: var(--gold);
  font-size: 1.5rem;
  line-height: 1;
}

.footer-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 1.2rem;
}

.footer-bottom {
  border-top: 1px solid var(--line);
  padding: 20px 0 30px;
}

.footer-bottom-inner {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  color: rgba(255,255,255,0.6);
  font-size: 0.8rem;
  letter-spacing: 0.05rem;
  text-transform: uppercase;
}

.whatsapp-float {
  position: fixed;
  right: 20px;
  bottom: 22px;
  z-index: 50;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 54px;
  padding: 0 1.2rem;
  border-radius: 999px;
  background: #25d366;
  color: #0f2a17;
  box-shadow: 0 12px 30px rgba(37, 211, 102, 0.35);
  font-weight: 700;
  letter-spacing: 0.04rem;
}

.nav-toggle {
  display: none;
  width: 46px;
  height: 46px;
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 10px 9px;
  cursor: pointer;
}

.nav-toggle span {
  display: block;
  width: 100%;
  height: 2px;
  background: var(--text);
  border-radius: 999px;
}

.nav-toggle span + span {
  margin-top: 5px;
}

.lightbox {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.86);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.28s ease;
  z-index: 1000;
}

.lightbox.show {
  opacity: 1;
  pointer-events: auto;
}

.lightbox img {
  max-width: min(88vw, 1100px);
  max-height: 82vh;
  object-fit: cover;
  border-radius: 20px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.35);
}

.lightbox-close,
.lightbox-nav {
  position: absolute;
  border: none;
  background: rgba(255,255,255,0.08);
  color: var(--text);
  width: 54px;
  height: 54px;
  border-radius: 50%;
  font-size: 2.2rem;
  cursor: pointer;
}

.lightbox-close {
  top: 22px;
  right: 22px;
}

.lightbox-prev {
  left: 28px;
}

.lightbox-next {
  right: 28px;
}

.reservation-page,
.contact-page {
  background: #101010;
}

.reservation-hero,
.contact-hero {
  position: relative;
  min-height: 460px;
  display: flex;
  align-items: center;
  background-size: cover;
  background-position: center;
  isolation: isolate;
}

.reservation-overlay,
.contact-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(16, 16, 16, 0.86), rgba(16, 16, 16, 0.54));
  z-index: 0;
}

.reservation-hero-content,
.contact-hero-content {
  position: relative;
  z-index: 1;
  padding-top: 140px;
  padding-bottom: 80px;
  max-width: 640px;
}

.reservation-hero h1,
.contact-hero h1 {
  font-size: clamp(3.2rem, 6vw, 5.5rem);
  margin-bottom: 1rem;
}

.reservation-hero p,
.contact-hero p {
  font-size: 1.05rem;
  color: rgba(245, 240, 231, 0.82);
}

.reservation-shell,
.contact-shell {
  display: grid;
  grid-template-columns: 1.1fr 1.3fr;
  gap: 28px;
  padding-top: 60px;
  padding-bottom: 90px;
}

.reservation-card,
.contact-card {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  padding: 32px;
  box-shadow: var(--shadow);
}

.reservation-card__head {
  margin-bottom: 24px;
}

.reservation-card__head h2 {
  font-size: clamp(2.5rem, 4vw, 3.4rem);
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.field span {
  color: var(--text);
  font-size: 0.78rem;
  letter-spacing: 0.08rem;
  text-transform: uppercase;
}

.field input,
.field select,
.field textarea {
  width: 100%;
  border: 1px solid rgba(255,255,255,0.12);
  background: rgba(255,255,255,0.02);
  border-radius: 14px;
  color: var(--text);
  padding: 0.95rem 1rem;
}

.field input::placeholder,
.field textarea::placeholder {
  color: rgba(255,255,255,0.36);
}

.field textarea {
  resize: vertical;
  min-height: 150px;
}

.field-full {
  margin-top: 20px;
}

.reservation-actions,
.quick-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 26px;
}

.contact-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 28px;
}

.contact-badges span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.7rem 1rem;
  border-radius: 999px;
  background: rgba(198,164,106,0.08);
  border: 1px solid rgba(198,164,106,0.28);
  color: var(--text);
  font-size: 0.7rem;
  letter-spacing: 0.08rem;
  text-transform: uppercase;
}

@media (max-width: 980px) {
  .nav-toggle {
    display: block;
  }

  .nav-panel {
    position: absolute;
    top: 86px;
    right: 24px;
    left: 24px;
    display: none;
    flex-direction: column;
    align-items: stretch;
    background: rgba(17,17,17,0.98);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 22px;
    box-shadow: var(--shadow);
  }

  .nav-panel.is-open {
    display: flex;
  }

  .nav-links {
    flex-direction: column;
    align-items: flex-start;
    gap: 18px;
  }

  .nav-cta {
    width: 100%;
  }

  .experience-grid,
  .menu-grid,
  .events-grid,
  .footer-grid,
  .reservation-shell,
  .contact-shell,
  .signature-grid {
    grid-template-columns: 1fr;
  }

  .experience-visual img {
    height: 520px;
  }

  .gallery-item,
  .gallery-item.tall,
  .gallery-item.wide {
    grid-column: span 6;
  }
}

@media (max-width: 640px) {
  .section {
    padding: 90px 0;
  }

  .hero h1 {
    font-size: 3.2rem;
  }

  .hero-inner {
    padding-top: 100px;
  }

  .hero-summary {
    grid-template-columns: 1fr;
    margin-top: 0;
  }

  .hero-actions,
  .reservation-actions,
  .quick-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .gallery-item,
  .gallery-item.tall,
  .gallery-item.wide {
    grid-column: span 12;
    min-height: 330px;
  }

  .footer-bottom-inner {
    flex-direction: column;
    align-items: flex-start;
  }

  .whatsapp-float {
    right: 16px;
    bottom: 16px;
  }
}
'''

script = '''document.addEventListener('DOMContentLoaded', () => {
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
'''

(root / 'index.html').write_text(index_html, encoding='utf-8')
(root / 'contact.html').write_text(contact_html, encoding='utf-8')
(root / 'styles.css').write_text(styles, encoding='utf-8')
(root / 'script.js').write_text(script, encoding='utf-8')

print('done')
