// Alvásterv-kalkulátor — paraméterek: data/tools/alvasterv.yaml → window.HT_TOOL (a build írja be).
(function () {
  var P = window.HT_TOOL; if (!P) return;
  var LS = window.HT && window.HT.ls;
  var $ = function (id) { return document.getElementById(id); };
  var H = 3600000, D = 86400000;
  var pad = function (n) { return String(n).padStart(2, '0'); };
  var hm = function (d) { return pad(d.getHours()) + ':' + pad(d.getMinutes()); };
  var hrs = function (x) { return String(Math.round(x * 10) / 10).replace('.', ','); };
  var midnight = function (d) { var m = new Date(d); m.setHours(0, 0, 0, 0); return m; };
  var dayOf = function (d, m0) { return Math.floor((midnight(d) - m0) / D) + 1; };
  var dayLab = function (d, m0) { return dayOf(d, m0) + '. nap ' + hm(d); };
  var esc = function (s) { return String(s).replace(/</g, '&lt;'); };

  // --- alapértékek
  var now = new Date(); now.setDate(now.getDate() + 30); now.setHours(8, 0, 0, 0);
  $('rajt').value = now.getFullYear() + '-' + pad(now.getMonth() + 1) + '-' + pad(now.getDate()) + 'T08:00';
  var kr = LS && LS('ht.kronotipus');
  if (kr && kr.cat) { $('krono').value = kr.cat; $('krono-hint').innerHTML = 'a kérdőív eredménye (' + kr.when + '): ' + esc(kr.band); }
  var saved = LS && LS('ht.alvasterv');
  if (saved) Object.keys(saved).forEach(function (k) { if ($(k) && saved[k] !== undefined) $(k).value = saved[k]; });
  $('eltolas').value = P.chronotype_shift_h[$('krono').value];

  function band(days, tipus) {
    if (tipus === 'brevet') return P.sleep_bands.filter(function (b) { return b.id === 'brevet'; })[0];
    return P.sleep_bands.filter(function (b) { return b.id !== 'brevet' && days <= b.max_days; })[0] || P.sleep_bands[2];
  }
  var lastBand = null;
  function setBand(force) {
    var b = band(+$('napok').value, $('tipus').value);
    $('sav-hint').textContent = b.label + ': ' + hrs(b.hours_min) + '–' + hrs(b.hours_max) + ' óra/éj — ' + b.note;
    if (force || !lastBand || lastBand.id !== b.id) { $('alvas').value = (b.hours_min + b.hours_max) / 2; }
    lastBand = b; return b;
  }
  $('krono').addEventListener('change', function () { $('eltolas').value = P.chronotype_shift_h[$('krono').value]; calc(); });
  ['napok', 'tipus'].forEach(function (id) { $(id).addEventListener('change', function () { setBand(true); calc(); }); });
  ['verseny', 'tav', 'rajt', 'ebredes', 'eltolas', 'szunyi', 'alvas', 'sebesseg', 'arany', 'lefekves'].forEach(function (id) { $(id).addEventListener('input', calc); });

  var R = {};
  function calc() {
    var b = setBand(false);
    var rajt = new Date($('rajt').value); if (isNaN(rajt)) return;
    var eb = $('ebredes').value.split(':'); var wake = new Date(rajt); wake.setHours(+eb[0], +eb[1], 0, 0);
    if (wake > rajt) wake.setDate(wake.getDate() - 1);
    var m0 = midnight(rajt);
    var napok = +$('napok').value || 1, shift = +$('eltolas').value || 0, alvas = +$('alvas').value || 0;
    var h17 = new Date(wake.getTime() + P.thresholds.first_hours * H), h24 = new Date(wake.getTime() + P.thresholds.second_hours * H);
    var nights = Math.max(0, Math.ceil(napok) - 1);
    var blocks = [];
    for (var i = 1; i <= nights; i++) {
      var center = new Date(m0.getTime() + i * D + ((P.nadir.start + P.nadir.end) / 2 + shift) * H);
      if (alvas > 0) { var bs = Math.round((center.getTime() - alvas / 2 * H) / (15 * 60000)) * 15 * 60000; blocks.push({ s: new Date(bs), e: new Date(bs + alvas * H), n: i }); }
    }
    var awakeAtStart = (rajt - wake) / H;
    var firstAwake = blocks.length ? (blocks[0].s - wake) / H : null;
    var arany = +$('arany').value / 100; $('arany-v').textContent = Math.round(arany * 100) + ' %';
    var speed = +$('sebesseg').value || P.moving_ratio.default_speed_kmh;
    var awake = 24 - alvas, moving = awake * arany, km = moving * speed, tav = +$('tav').value || 0;
    R = { rajt: rajt, wake: wake, m0: m0, h17: h17, h24: h24, blocks: blocks, shift: shift, alvas: alvas, band: b, km: km, speed: speed, arany: arany, awake: awake, moving: moving, napok: napok };

    var rows = [
      ['Ébren a rajt pillanatában', hrs(awakeAtStart) + ' óra', ''],
      ['<b>' + P.thresholds.first_hours + '. ébrenléti óra</b> ≈ 0,5 ‰ — innen a jelekre figyelsz, szunyókálás jöhet', dayLab(h17, m0), 'big'],
      ['<b>' + P.thresholds.second_hours + '. ébrenléti óra</b> ≈ 1 ‰ — ide nem tervezel technikás szakaszt', dayLab(h24, m0), 'big warn'],
      ['Belső óra mélypontja (' + pad(P.nadir.start) + ':00–' + pad(P.nadir.end) + ':00, eltolva ' + (shift >= 0 ? '+' : '') + hrs(shift) + ' h)', hm(new Date(m0.getTime() + (P.nadir.start + shift) * H)) + '–' + hm(new Date(m0.getTime() + (P.nadir.end + shift) * H)), ''],
      ['Legveszélyesebb szakasz terepen (' + pad(P.nadir.danger_start) + ':00–' + pad(P.nadir.danger_end) + ':00, a leglassabb reakcióidő)', pad(P.nadir.danger_start) + ':00–' + pad(P.nadir.danger_end) + ':00', ''],
      ['Napi alvássáv a versenyhosszra', hrs(b.hours_min) + '–' + hrs(b.hours_max) + ' óra/éj', '']
    ];
    blocks.forEach(function (bl) { rows.push([bl.n + '. éjszaka — alvásblokk (' + hrs(alvas) + ' óra, minden éjjel ugyanannyi)', dayLab(bl.s, m0) + ' → ' + hm(bl.e), '']); });
    if (!blocks.length) rows.push(['Éjszakai blokk', nights ? 'nincs (0 óra) — csak szunyókálás' : 'nincs: a verseny 24 órán belüli', '']);
    rows.push(['Szunyókálás: ablak / alvás', (+$('szunyi').value + (P.nap.window_min - P.nap.sleep_min)) + ' perc / ' + $('szunyi').value + ' perc', '']);
    $('out').innerHTML = rows.map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v ' + r[2] + '">' + r[1] + '</div>'; }).join('');

    var w = [];
    if (firstAwake !== null && firstAwake > P.thresholds.second_hours) w.push('<b>Az első blokk a ' + P.thresholds.second_hours + '. ébrenléti óra után kezdődne (' + hrs(firstAwake) + '. óra).</b> Tegyél be egy ' + $('szunyi').value + ' perces szunyókálást a ' + P.thresholds.first_hours + '. óra körül (' + dayLab(h17, m0) + '), vagy kezdd korábban a blokkot.');
    else if (firstAwake !== null && firstAwake > P.thresholds.first_hours) w.push('Az első blokk a ' + P.thresholds.first_hours + '. ébrenléti óra után kezdődik (' + hrs(firstAwake) + '. óra): a ' + P.thresholds.first_hours + '. órától a jelekre figyelsz, és ' + dayLab(h17, m0) + ' körül egy ' + $('szunyi').value + ' perces szunyókálás jöhet.');
    if (b.id === 'hosszu' && alvas < 5.3) w.push('5,3 óra/nap alatt terepen az álmosság napról napra nőtt (7. oldal) — a ' + hrs(alvas) + ' óra a mezőny gyakorlata, nem cél; a jelekre a szunyókálás jön, nem a kihagyás.');
    if (nights >= 4 && alvas < 1.5) w.push('5+ napos versenyen a „ma kihagyom, holnap pótolom” nem működik: laborban egy hét rövid alvás után három pihenőéjszaka sem törlesztett (10. oldal).');
    $('warn').innerHTML = w.map(function (s) { return '<p class="note" style="border-left:4px solid var(--warning);padding-left:10px">' + s + '</p>'; }).join('');

    $('cost').innerHTML = [
      ['Ébren töltött idő naponta', hrs(awake) + ' óra'],
      ['Mozgásban ebből (' + Math.round(arany * 100) + ' %)', hrs(moving) + ' óra'],
      ['Napi távolság ' + speed + ' km/h átlaggal', Math.round(km) + ' km/nap'],
      ['Becsült versenyidő ' + tav + ' km-re', tav ? hrs(tav / km) + ' nap' : '—'],
      ['+1 óra alvás naponta', '≈ −' + Math.round(speed) + ' km/nap'],
      ['Egy órányi alvásmámoros eltévedés', '≈ −' + Math.round(speed) + ' km']
    ].map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v">' + r[1] + '</div>'; }).join('');

    var lf = $('lefekves').value.split(':'); var bed = new Date(m0); bed.setHours(+lf[0], +lf[1], 0, 0);
    var bedT = new Date(bed.getTime() - P.banking.extra_hours * H);
    var c100 = new Date(bed.getTime() - P.caffeine.before_bed_h_100mg * H), c200 = new Date(bed.getTime() - P.caffeine.before_bed_h_200mg * H);
    $('week').innerHTML = [
      ['Rajt előtti ' + P.banking.nights + '–7 éjszaka: lefekvés (+' + hrs(P.banking.extra_hours) + ' óra a szokásoshoz képest)', hm(bedT) + ' helyett ' + hm(bed)],
      ['Utolsó kávé (~100 mg), ' + P.caffeine.before_bed_h_100mg + ' órával lefekvés előtt', hm(c100)],
      ['Utolsó erős edzés előtti készítmény (~200 mg), ' + P.caffeine.before_bed_h_200mg + ' órával', hm(c200)],
      ['Nappali szunyókálás, ha az éjszakai nyújtás nem megy', '13:00–16:00, < 30 perc'],
      ['Utolsó hosszú edzés', 'ne ezen a héten']
    ].map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v">' + r[1] + '</div>'; }).join('');
    R.bed = bed; R.bedT = bedT; R.c100 = c100;

    drawTimeline();
    if (LS) { var o = {}; ['verseny', 'tav', 'napok', 'tipus', 'rajt', 'ebredes', 'krono', 'eltolas', 'szunyi', 'alvas', 'sebesseg', 'arany', 'lefekves'].forEach(function (k) { o[k] = $(k).value; }); LS('ht.alvasterv', o); }
  }

  function drawTimeline() {
    var W = 760, L = 58, RW = W - L - 12, RH = 36, top = 26;
    var days = Math.max(Math.ceil(R.napok), dayOf(R.h24, R.m0), R.blocks.length ? dayOf(R.blocks[R.blocks.length - 1].e, R.m0) : 1);
    var Hh = top + days * RH + 18;
    var x = function (t) { return L + t * RW / 24; };
    var s = '<svg viewBox="0 0 ' + W + ' ' + Hh + '" font-family="Inter, system-ui, sans-serif" font-size="11">';
    // órarács
    for (var h = 0; h <= 24; h += 3) { s += '<line x1="' + x(h) + '" y1="' + top + '" x2="' + x(h) + '" y2="' + (top + days * RH) + '" stroke="#e1e0d9"/><text x="' + x(h) + '" y="' + (top - 8) + '" text-anchor="middle" fill="#898781" font-size="10">' + pad(h) + '</text>'; }
    var interval = function (a, b, fill, op, ry) {
      for (var d = 1; d <= days; d++) {
        var ds = R.m0.getTime() + (d - 1) * D, de = ds + D;
        var s0 = Math.max(a.getTime(), ds), e0 = Math.min(b.getTime(), de); if (e0 <= s0) continue;
        s += '<rect x="' + x((s0 - ds) / H) + '" y="' + (top + (d - 1) * RH + (ry || 4)) + '" width="' + ((e0 - s0) / H * RW / 24) + '" height="' + (RH - 2 * (ry || 4)) + '" fill="' + fill + '" fill-opacity="' + op + '" rx="2"/>';
      }
    };
    for (var d = 1; d <= days; d++) {
      var ds = new Date(R.m0.getTime() + (d - 1) * D);
      s += '<text x="' + (L - 8) + '" y="' + (top + (d - 1) * RH + RH / 2 + 4) + '" text-anchor="end" fill="#52514e" font-weight="500">' + d + '. nap</text>';
      s += '<line x1="' + L + '" y1="' + (top + d * RH) + '" x2="' + (L + RW) + '" y2="' + (top + d * RH) + '" stroke="#e1e0d9"/>';
      interval(new Date(ds.getTime() + (P.nadir.start + R.shift) * H), new Date(ds.getTime() + (P.nadir.end + R.shift) * H), '#256abf', 0.13, 2);
      interval(new Date(ds.getTime() + P.nadir.danger_start * H), new Date(ds.getTime() + P.nadir.danger_end * H), '#eb6834', 0.10, 2);
    }
    // ébren a rajt előtt / verseny alatt: halvány sáv ébredéstől a 24. óráig (a küszöbök szakasza)
    interval(R.wake, R.h17, '#0ca30c', 0.10, 12); interval(R.h17, R.h24, '#fab219', 0.22, 12);
    R.blocks.forEach(function (b) { interval(b.s, b.e, '#0d366b', 0.9, 9); });
    var mark = function (t, lab, col, up) {
      var d = dayOf(t, R.m0); if (d < 1 || d > days) return;
      var xx = x((t - (R.m0.getTime() + (d - 1) * D)) / H), y0 = top + (d - 1) * RH;
      s += '<line x1="' + xx + '" y1="' + (y0 + 2) + '" x2="' + xx + '" y2="' + (y0 + RH - 2) + '" stroke="' + col + '" stroke-width="2"/>';
      s += '<text x="' + (xx + 4) + '" y="' + (y0 + (up ? 12 : RH - 5)) + '" fill="' + col + '" font-weight="600" font-size="10">' + lab + '</text>';
    };
    mark(R.wake, 'ébredés', '#52514e', true); mark(R.rajt, 'rajt', '#184f95', false);
    mark(R.h17, P.thresholds.first_hours + '. óra', '#b07a00', true); mark(R.h24, P.thresholds.second_hours + '. óra', '#d03b3b', false);
    var ly = top + days * RH + 13;
    s += '<g font-size="10" fill="#52514e"><rect x="' + L + '" y="' + (ly - 8) + '" width="12" height="8" fill="#256abf" fill-opacity=".2"/><text x="' + (L + 16) + '" y="' + ly + '">mélypont</text>' +
      '<rect x="' + (L + 80) + '" y="' + (ly - 8) + '" width="12" height="8" fill="#eb6834" fill-opacity=".15"/><text x="' + (L + 96) + '" y="' + ly + '">05–09: leglassabb reakció</text>' +
      '<rect x="' + (L + 250) + '" y="' + (ly - 8) + '" width="12" height="8" fill="#0d366b"/><text x="' + (L + 266) + '" y="' + ly + '">alvásblokk (példa)</text>' +
      '<rect x="' + (L + 380) + '" y="' + (ly - 8) + '" width="12" height="8" fill="#fab219" fill-opacity=".3"/><text x="' + (L + 396) + '" y="' + ly + '">17–24. ébrenléti óra</text></g>';
    $('timeline').innerHTML = s + '</svg>';
  }

  // --- sablon
  var F = {}; document.querySelectorAll('#sablon-f textarea').forEach(function (t) { F[t.getAttribute('data-k')] = t; });
  var sv = LS && LS('ht.sablon.04'); if (sv) Object.keys(sv).forEach(function (k) { if (F[k]) F[k].value = sv[k]; });
  var saveS = function () { if (!LS) return; var o = {}; Object.keys(F).forEach(function (k) { o[k] = F[k].value; }); LS('ht.sablon.04', o); };
  Object.keys(F).forEach(function (k) { F[k].addEventListener('input', saveS); });
  $('atvesz').addEventListener('click', function () {
    calc(); var KR = { korai: 'korai', koztes: 'köztes', kesoi: 'késői' };
    var m = R.m0;
    F.verseny.value = ($('verseny').value || '—') + ', ' + $('tav').value + ' km, ' + hrs(R.napok) + ' nap';
    F.rajt.value = 'rajt ' + R.rajt.toLocaleDateString('hu-HU') + ' ' + hm(R.rajt) + ', ébredés ' + hm(R.wake);
    F.h17.value = dayLab(R.h17, m); F.h24.value = dayLab(R.h24, m);
    F.krono.value = KR[$('krono').value] + (kr ? ' (rMEQ ' + kr.score + ')' : '');
    F.melypont.value = hm(new Date(m.getTime() + (P.nadir.start + R.shift) * H)) + '–' + hm(new Date(m.getTime() + (P.nadir.end + R.shift) * H)) + ' (eltolás ' + (R.shift >= 0 ? '+' : '') + hrs(R.shift) + ' h)';
    F.sav.value = hrs(R.band.hours_min) + '–' + hrs(R.band.hours_max) + ' óra/éj (' + R.band.label + ')';
    F.blokkok.value = R.blocks.length ? R.blocks.map(function (b) { return b.n + '. éj ' + hm(b.s) + '–' + hm(b.e); }).join(' · ') : 'nincs blokk — szunyókálás a jelekre';
    F.szunyi.value = (+$('szunyi').value + (P.nap.window_min - P.nap.sleep_min)) + ' perc ablak / ' + $('szunyi').value + ' perc alvás';
    F.koffein.value = '100–200 mg szunyókálás előtt; a főalvás előtti 4–5 órában nem; versenyen nem próbálok ki újat';
    F.arany.value = Math.round(R.arany * 100) + ' % (' + hrs(R.awake) + ' óra ébrenlétből ' + hrs(R.moving) + ' óra mozgás, ≈ ' + Math.round(R.km) + ' km/nap)';
    F.het.value = 'lefekvés ' + hm(R.bedT) + ' (6–7 éjszaka) · utolsó kávé ' + hm(R.c100);
    saveS();
  });
  $('torol').addEventListener('click', function () { Object.keys(F).forEach(function (k) { F[k].value = ''; }); saveS(); });
  $('print').addEventListener('click', function () { document.body.classList.add('print-sablon'); window.print(); setTimeout(function () { document.body.classList.remove('print-sablon'); }, 500); });

  setBand(!saved); calc();
})();
