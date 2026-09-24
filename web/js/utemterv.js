// Felkészülési ütemterv-generátor — paraméterek: data/tools/utemterv.yaml → window.HT_TOOL.
(function () {
  var P = window.HT_TOOL; if (!P) return;
  var LS = window.HT && window.HT.ls;
  var $ = function (id) { return document.getElementById(id); };
  var kv = function (rows) { return rows.map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v ' + (r[2] || '') + '">' + r[1] + '</div>'; }).join(''); };
  var DAY = 86400000;
  var hu = function (d) { return d.toLocaleDateString('hu-HU', { month: 'short', day: 'numeric' }); };
  var hu2 = function (d) { return d.toLocaleDateString('hu-HU', { year: 'numeric', month: 'short', day: 'numeric' }); };

  var IDS = ['race', 'fmt', 'hours', 'hot', 'brevet', 'start'];
  var saved = LS && LS('ht.utemterv');
  if (saved) IDS.forEach(function (k) { if ($(k) && saved[k]) $(k).value = saved[k]; });
  if (!$('start').value) { var t0 = new Date(); $('start').value = t0.toISOString().slice(0, 10); }
  if (!$('race').value) { var r0 = new Date(Date.now() + 140 * DAY); $('race').value = r0.toISOString().slice(0, 10); }
  IDS.forEach(function (id) { $(id).addEventListener('input', calc); });

  function calc() {
    var race = new Date($('race').value), start = new Date($('start').value);
    if (isNaN(race) || isNaN(start)) return;
    var weeks = Math.floor((race - start) / (7 * DAY));
    var fmt = $('fmt').value, hours = +$('hours').value || 10, hot = $('hot').value === '1', brevet = $('brevet').value === '1';
    var taperD = fmt === 'tobb' ? 18 : 12;
    var specW = 4, buildW = Math.min(8, Math.max(4, weeks - specW - Math.ceil(taperD / 7) - 4));
    var baseW = Math.max(0, weeks - specW - buildW - Math.ceil(taperD / 7));
    var wAt = function (wBefore) { return new Date(race - wBefore * 7 * DAY); };
    var taperStart = new Date(race - taperD * DAY);
    var peak = wAt(5), reh = wAt(P.rehearsal.weeks_before);
    var b600 = wAt(5), b400 = wAt(8), b300 = wAt(11), b200 = wAt(14);
    var heatStart = new Date(race - 13 * DAY);
    var head = [
      ['A rajtig', weeks + ' hét', 'big'],
      ['Fázisok', baseW + ' hét alap → ' + buildW + ' hét építés → ' + specW + ' hét specifikus → taper ' + taperD + ' nap'],
      ['Heti órád', hours + ' h — Z1-arány cél: ' + (hours < 8 ? '75–80' : hours < 12 ? '80–85' : '85–90') + ' % (3. oldal)']
    ];
    $('head-out').innerHTML = kv(head);
    var w = [];
    if (weeks < 16) w.push('<b>' + weeks + ' hét van a rajtig</b> — a 16–24 hetes keret rövidül: az alapfázis esik ki, a specifikus rész és a taper nem. Az edződdel priorizáljatok.');
    if (weeks > 26) w.push('Bőven van idő: a többlet az alapfázisba megy (Z1-volumen, erősítés) — a csúcsot ne hozd előre.');
    if (hours < 8 && fmt === 'tobb') w.push('Heti ' + hours + ' óra többnapos versenyre a modul 8–12 órás reális minimuma alatt van: a hétvégi hosszú és a főpróba még fontosabb (13. oldal).');
    $('warn').innerHTML = w.map(function (s) { return '<p class="note" style="border-left:4px solid var(--warning);padding-left:10px">' + s + '</p>'; }).join('');

    // gantt
    var W = 760, H = 130, L = 20, RW = W - L - 20;
    var x = function (d) { return L + Math.max(0, Math.min(1, (d - start) / (race - start))) * RW; };
    var seg = [[start, wAt(specW + buildW + Math.ceil(taperD / 7)), 'alap', '#c9dcf3'], [wAt(specW + buildW + Math.ceil(taperD / 7)), wAt(specW + Math.ceil(taperD / 7) - 0), 'építés', '#9cc1ea'], [wAt(specW + Math.ceil(taperD / 7)), taperStart, 'specifikus', '#f3b89c'], [taperStart, race, 'taper', '#a9dfc8']];
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" font-family="Inter, system-ui, sans-serif" font-size="11">';
    seg.forEach(function (g) {
      if (g[1] <= g[0]) return;
      s += '<rect x="' + x(g[0]) + '" y="30" width="' + Math.max(2, x(g[1]) - x(g[0])) + '" height="30" rx="4" fill="' + g[3] + '"/>';
      if (x(g[1]) - x(g[0]) > 50) s += '<text x="' + ((x(g[0]) + x(g[1])) / 2) + '" y="49" text-anchor="middle" fill="#0b0b0b" font-weight="600">' + g[2] + '</text>';
    });
    s += '<text x="' + L + '" y="20" fill="#52514e">' + hu2(start) + '</text><text x="' + (L + RW) + '" y="20" text-anchor="end" fill="#52514e">rajt: ' + hu2(race) + '</text>';
    var marks = [[peak, 'csúcs', '#eb6834'], [reh, 'főpróba', '#0d366b']];
    if (hot) marks.push([heatStart, 'hőblokk', '#ec835a']);
    marks.forEach(function (m, i) {
      s += '<line x1="' + x(m[0]) + '" y1="60" x2="' + x(m[0]) + '" y2="' + (78 + i * 16) + '" stroke="' + m[2] + '" stroke-dasharray="3 2"/>';
      s += '<text x="' + x(m[0]) + '" y="' + (90 + i * 16) + '" text-anchor="middle" fill="' + m[2] + '" font-weight="600">' + m[1] + ' · ' + hu(m[0]) + '</text>';
    });
    $('gantt').innerHTML = s + '</svg>';

    // plan list
    var items = [];
    items.push(['Taper kezdete', hu2(taperStart) + ' — volumen −40–60 %, intenzitás és ritmus marad; utolsó hosszú: ' + hu2(new Date(race - 12 * DAY)) + ' körül', 'fix']);
    items.push(['Terhelés-csúcs', hu2(wAt(6)) + ' – ' + hu2(wAt(4)) + ' (a rajt előtti 4–6. hét)', 'ex']);
    items.push(['2–4 napos főpróba', hu2(reh) + ' hétvégéjén — felszerelés, alvás, etetés versenyéles tesztje', 'ex']);
    if (brevet) {
      items.push(['Brevet-lépcső', '200: ' + hu(b200) + ' · 300: ' + hu(b300) + ' · 400: ' + hu(b400) + ' · 600: ' + hu(b600) + ' (a 600-as az alvás-főpróba; hagyj tartalék-dátumot)', 'fix']);
    }
    if (hot) items.push(['Hőblokk', hu2(heatStart) + '-től 10–14 nap, a taperrel átfedésben; utána 2 naponta fenntartó hőexpozíció (levezetett szabály)', 'ex']);
    items.push(['Erősítés', 'alapozástól heti 2 nehéz; szezonban heti 1 fenntartó; utolsó nehéz: ' + hu2(new Date(race - 8 * DAY)) + ' körül', 'fix']);
    items.push(['Blokk-ritmus', '3 terhelő + 1 könnyű hét; heti legalább 1 teljes pihenőnap — a pihenőhét kihagyása a leggyakoribb hiba', 'fix']);
    items.push(['Monitorozás', 'napi 2 kérdés (fáradtság, edzéskészség) + heti összóra; HRV 7 napos trendben, ha mérsz (11–12. oldal)', 'ex']);
    items.push(['Munkacsúcs-vészterv', 'minimál-dózis: heti 2 rövid, élénk edzés + heti 1 erő — a bázis ~15 hétig kitart', 'ex']);
    $('plan-out').innerHTML = '<div class="kv">' + kv(items.map(function (i) { return [i[0], i[1]]; })) + '</div>';
    if (LS) { var sv = {}; IDS.forEach(function (k) { sv[k] = $(k).value; }); LS('ht.utemterv', sv); }
  }
  $('print').addEventListener('click', function () { window.print(); });
  calc();
})();
