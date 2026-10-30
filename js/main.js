// Mobile nav toggle + dropdown accordions
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  document.querySelectorAll('.has-drop > button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.parentElement;
      var wasOpen = item.classList.contains('open');
      document.querySelectorAll('.has-drop.open').forEach(function (o) {
        o.classList.remove('open');
        o.querySelector('button').setAttribute('aria-expanded', 'false');
      });
      if (!wasOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });
});

// ─────────────────────────────────────────────
// Scroll reveal — sections fade up as you scroll
// (same treatment as the Karen/Britney sites)
// ─────────────────────────────────────────────
(function () {
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced || !('IntersectionObserver' in window)) return;

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });

  var blocks = document.querySelectorAll('main section, section.section, .page-hero, .cta-band');
  var seen = [];
  blocks.forEach(function (block) {
    if (block.classList.contains('video-hero')) return; // hero has its own entrance
    if (seen.indexOf(block) !== -1) return;
    seen.push(block);

    var wrap = block.querySelector('.wrap');
    var items = wrap ? Array.prototype.slice.call(wrap.children) : [block];
    items.forEach(function (el, i) {
      el.classList.add('reveal-item');
      // Stagger: each child arrives ~90ms after the previous (capped)
      el.style.setProperty('--rd', Math.min(i * 90, 450) + 'ms');
      io.observe(el);
    });
  });
})();
