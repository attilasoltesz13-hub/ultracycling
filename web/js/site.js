// Hosszú távon — közös oldal-viselkedés: tartalomjegyzék kiemelése, szintszűrő. Vanilla JS, file:// alól is fut.
(function () {
  var LS = function (k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k)); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } };
  window.HT = window.HT || {}; window.HT.ls = LS;

  // --- tartalomjegyzék: az éppen látható szakasz kiemelése
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a[href^="#"]'));
  if (links.length && 'IntersectionObserver' in window) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { links.forEach(function (a) { a.classList.remove('on'); }); var a = map[e.target.id]; if (a) a.classList.add('on'); }
      });
    }, { rootMargin: '-64px 0px -70% 0px', threshold: 0 });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  // --- szintszűrő: alap / haladó / elit (halmozódó: a haladó az alapot is mutatja)
  var chips = document.querySelectorAll('.filters .chip[data-level]');
  if (chips.length) {
    var order = ['alap', 'halado', 'elit'];
    var apply = function (lvl) {
      var max = order.indexOf(lvl);
      chips.forEach(function (c) { c.classList.toggle('on', c.getAttribute('data-level') === lvl); });
      document.querySelectorAll('section.pg[data-level]').forEach(function (s) {
        var i = order.indexOf(s.getAttribute('data-level'));
        s.classList.toggle('hidden', i > max);
      });
      document.querySelectorAll('.toc li[data-level]').forEach(function (li) {
        li.style.display = order.indexOf(li.getAttribute('data-level')) > max ? 'none' : '';
      });
      LS('ht.level', lvl);
    };
    chips.forEach(function (c) { c.addEventListener('click', function () { apply(c.getAttribute('data-level')); }); });
    apply(LS('ht.level') || 'elit');
  }
})();
