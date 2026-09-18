// Kronotípus-kérdőív — az rMEQ (Adan & Almirall 1991) szerkezete és pontozása, magyarra fogalmazva.
// Tájékoztató eszköz; az eredményt a böngésző tárolja (ht.kronotipus), a kalkulátor onnan olvassa.
(function () {
  var LS = window.HT && window.HT.ls;
  var Q = [
    { q: 'Ha teljesen szabadon tervezhetnéd a napodat, és csak arra figyelnél, mikor érzed magad a legjobban, mikor kelnél fel?',
      o: [['05:00–06:30', 5], ['06:30–07:45', 4], ['07:45–09:45', 3], ['09:45–11:00', 2], ['11:00–12:00', 1]] },
    { q: 'Ébredés után az első fél órában mennyire érzed magad fáradtnak?',
      o: [['Nagyon fáradt', 1], ['Eléggé fáradt', 2], ['Eléggé friss', 3], ['Nagyon friss', 4]] },
    { q: 'Este mikor érzed úgy, hogy elfáradtál, és alvásra van szükséged?',
      o: [['20:00–21:00', 5], ['21:00–22:15', 4], ['22:15–00:45', 3], ['00:45–02:00', 2], ['02:00–03:00', 1]] },
    { q: 'A nap melyik szakaszában érzed, hogy a csúcson vagy — a legjobb formádban?',
      o: [['05:00–08:00', 5], ['08:00–10:00', 4], ['10:00–17:00', 3], ['17:00–22:00', 2], ['22:00–05:00', 1]] },
    { q: 'Beszélnek „reggeli” és „esti” típusú emberekről. Te melyiknek tartod magad?',
      o: [['Határozottan reggeli', 6], ['Inkább reggeli, mint esti', 4], ['Inkább esti, mint reggeli', 2], ['Határozottan esti', 0]] }
  ];
  var root = document.getElementById('meq'); if (!root) return;
  Q.forEach(function (q, i) {
    var d = document.createElement('div'); d.className = 'card';
    d.innerHTML = '<h2><span class="mono muted">' + (i + 1) + '/5</span> ' + q.q + '</h2><div class="radio">' +
      q.o.map(function (o) { return '<label><input type="radio" name="m' + i + '" value="' + o[1] + '"><span>' + o[0] + '</span></label>'; }).join('') + '</div>';
    root.appendChild(d);
  });
  var out = document.getElementById('meq-out');
  var band = function (s) {
    if (s <= 7) return ['határozottan esti', 'kesoi']; if (s <= 11) return ['mérsékelten esti', 'kesoi'];
    if (s <= 17) return ['köztes', 'koztes']; if (s <= 21) return ['mérsékelten reggeli', 'korai']; return ['határozottan reggeli', 'korai'];
  };
  var CAT = { korai: 'korai', koztes: 'köztes', kesoi: 'késői' };
  var TIP = {
    korai: 'A csúcsod dél körül, kb. 5,6–6,5 órával az ébredés után; a hajnali szakasz kevésbé vesz el belőled, a késő esti szunyókálás viszont kockázatosabb — az éjszakai blokkot kezdd korábban (a 00:00–04:00 sávot eltolva a korábbi irányba).',
    koztes: 'A csúcsod délután 4 körül, kb. 5,6–6,5 órával az ébredés után; a 00:00–04:00 sáv nagyjából változtatás nélkül érvényes rád.',
    kesoi: 'A csúcsod este 8 körül, kb. 11 órával az ébredés után; a hajnali szakasz és a hajnali ébresztés utáni kábaság többet vesz el belőled (26 % ingadozás) — inkább később fekszel és később kelsz, a blokkot told későbbre.'
  };
  root.addEventListener('change', function () {
    var vals = Q.map(function (_, i) { var el = document.querySelector('input[name="m' + i + '"]:checked'); return el ? +el.value : null; });
    if (vals.some(function (v) { return v === null; })) { out.innerHTML = '<span class="muted">' + vals.filter(function (v) { return v !== null; }).length + ' / 5 kérdés megválaszolva.</span>'; return; }
    var s = vals.reduce(function (a, b) { return a + b; }, 0); var b = band(s);
    out.innerHTML = '<div class="result"><div class="small muted">rMEQ-pontszám (4–25)</div><div class="big"><span class="mono">' + s + '</span> · ' + b[0] + '</div>' +
      '<p style="margin:8px 0 4px">A modul besorolásában: <b>' + CAT[b[1]] + ' típus</b>. ' + TIP[b[1]] + '</p>' +
      '<p class="small muted" style="margin:0">Mentve ebben a böngészőben; az alvásterv-kalkulátor innen veszi át. Tájékoztató eszköz, nem klinikai besorolás — a versenytervhez elég.</p></div>';
    if (LS) LS('ht.kronotipus', { score: s, band: b[0], cat: b[1], when: new Date().toISOString().slice(0, 10) });
  });
  var prev = LS && LS('ht.kronotipus');
  if (prev) out.innerHTML = '<div class="note">Korábbi eredményed (' + prev.when + '): <b class="mono">' + prev.score + '</b> · ' + prev.band + ' → <b>' + CAT[prev.cat] + ' típus</b>. Töltsd ki újra, ha frissíteni akarod.</div>';
})();
