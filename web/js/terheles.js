// Terhelés-kalkulátor — paraméterek: data/tools/terheles.yaml → window.HT_TOOL.
(function () {
  var P = window.HT_TOOL; if (!P) return;
  var LS = window.HT && window.HT.ls;
  var $ = function (id) { return document.getElementById(id); };
  var f0 = function (x) { return String(Math.round(x)); };
  var f1 = function (x) { return String(Math.round(x * 10) / 10).replace('.', ','); };
  var kv = function (rows) { return rows.map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v ' + (r[2] || '') + '">' + r[1] + '</div>'; }).join(''); };

  var IDS = ['ftp', 'h-z1', 'h-z1b', 'h-z2', 'h-z3', 'ctl0', 'ramp', 'block', 'taperw', 'fresh', 'tired', 'kj'];
  var saved = LS && LS('ht.terheles');
  if (saved) IDS.forEach(function (k) { if ($(k) && saved[k] !== undefined && saved[k] !== '') $(k).value = saved[k]; });
  IDS.forEach(function (id) { $(id).addEventListener('input', calc); });

  function midIF(z) { return (z.if_range[0] + z.if_range[1]) / 2; }

  function calc() {
    var hs = [+$('h-z1').value || 0, +$('h-z1b').value || 0, +$('h-z2').value || 0, +$('h-z3').value || 0];
    var total = hs.reduce(function (a, b) { return a + b; }, 0) || 0.001;
    var tss = 0, srpeGuess = 0;
    var rpeByZone = [2.5, 4, 6, 8];
    hs.forEach(function (h, i) {
      var z = P.zones[i];
      tss += h * (z.tss_h[0] + z.tss_h[1]) / 2;
      srpeGuess += h * 60 * rpeByZone[i];
    });
    var z1sum = hs[0] + hs[1];
    var z1pct = z1sum / total * 100, z2pct = hs[2] / total * 100, z3pct = hs[3] / total * 100;
    var band = null;
    for (var i = 0; i < P.distribution_bands.length; i++) { var b = P.distribution_bands[i]; if (total >= b.hours[0] && total <= b.hours[1] + 0.01) band = b; }
    if (!band) band = total < 6 ? P.distribution_bands[0] : P.distribution_bands[P.distribution_bands.length - 1];
    $('week-out').innerHTML = kv([
      ['Heti összóra', f1(total) + ' óra', 'big'],
      ['Becsült heti TSS (zóna-középértékekkel)', f0(tss) + ' pont', 'big'],
      ['Ugyanez sRPE-ben (perc × 0–10 — eszköz nélkül)', f0(srpeGuess) + ' pont'],
      ['Z1-arány (könnyű + ultra-alap) · tempó · kemény', f0(z1pct) + ' % · ' + f0(z2pct) + ' % · ' + f0(z3pct) + ' %'],
      ['A sávodhoz (' + band.hours[0] + '–' + band.hours[1] + ' h) ajánlott Z1', band.z1_pct[0] + '–' + band.z1_pct[1] + ' %'],
      ['Amatőr referencia (6–15 h, zömmel Z2)', P.weekly_reference.tss_range[0] + '–' + P.weekly_reference.tss_range[1] + ' TSS/hét']
    ]);
    var w = [];
    if (z1pct < band.z1_pct[0] - 3) w.push('A Z1-arányod (' + f0(z1pct) + ' %) a sávod ajánlása (' + band.z1_pct[0] + '–' + band.z1_pct[1] + ' %) alatt van: a szürke középzóna a legdrágább szokás — tedd lassabbá a könnyű napokat (3. oldal).');
    if (z3pct > 15) w.push('A kemény órák aránya magas (' + f0(z3pct) + ' %): heti 1–2 minőségi edzés tartja a plafont, a többlet inkább elhasznál (3. oldal).');
    if (hs[1] < 2 && total >= 6) w.push('Kevés a hosszú Z1–Z2 óra: a fáradtságállóság volumen-függő — a hétvégi hosszú nem alku tárgya (5–6. oldal).');
    $('dist-warn').innerHTML = w.map(function (s) { return '<p class="note" style="border-left:4px solid var(--warning);padding-left:10px">' + s + '</p>'; }).join('');
    sim(tss);
    dur();
    if (LS) { var s = {}; IDS.forEach(function (k) { s[k] = $(k).value; }); LS('ht.terheles', s); }
  }

  function sim(weekTss) {
    var ramp = +$('ramp').value, blockLen = +$('block').value, taperw = +$('taperw').value;
    var weeks = 16, ctl = +$('ctl0').value || 45, atl = ctl;
    var wt = Math.max(weekTss, ctl * 7 * 0.8);
    var pts = [], day = 0, maxRamp = 0, prevCtl = ctl;
    for (var wk = 0; wk < weeks; wk++) {
      var light = (wk % blockLen === blockLen - 1);
      var taper = (wk >= weeks - taperw);
      var target = wt * (light ? 0.55 : 1) * (taper ? 0.5 : 1);
      for (var d = 0; d < 7; d++) {
        var daily = target / 7;
        ctl += (daily - ctl) / 42;
        atl += (daily - atl) / 7;
        day++; pts.push([day, ctl, ctl - atl]);
      }
      maxRamp = Math.max(maxRamp, ctl - prevCtl); prevCtl = ctl;
      if (!light && !taper) wt += ramp * 7;   // heti +ramp CTL-pontnak megfelelő TSS-emelés (közelítés)
    }
    var W = 760, H = 220, L = 46, RW = W - L - 20, top = 20, bot = 175;
    var vmax = Math.max.apply(null, pts.map(function (p) { return p[1]; })) * 1.1;
    var vmin = Math.min(+$('ctl0').value || 45, 40) * 0.8;
    var x = function (d) { return L + d / (weeks * 7) * RW; };
    var y = function (v) { return bot - (v - vmin) / (vmax - vmin) * (bot - top); };
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" font-family="Inter, system-ui, sans-serif" font-size="11">';
    for (var g = Math.ceil(vmin / 10) * 10; g <= vmax; g += 15) s += '<line x1="' + L + '" y1="' + y(g) + '" x2="' + (L + RW) + '" y2="' + y(g) + '" stroke="#e1e0d9"/><text x="' + (L - 6) + '" y="' + (y(g) + 4) + '" text-anchor="end" fill="#898781">' + Math.round(g) + '</text>';
    s += '<rect x="' + x((weeks - taperw) * 7) + '" y="' + top + '" width="' + (x(weeks * 7) - x((weeks - taperw) * 7)) + '" height="' + (bot - top) + '" fill="#1baf7a" fill-opacity=".1"/>';
    s += '<path d="M' + pts.map(function (p) { return x(p[0]) + ' ' + y(p[1]); }).join(' L') + '" fill="none" stroke="#2a78d6" stroke-width="2.4"/>';
    for (var wq = 0; wq <= weeks; wq += 4) s += '<text x="' + x(wq * 7) + '" y="' + (bot + 16) + '" text-anchor="middle" fill="#898781">' + wq + '. hét</text>';
    s += '<text x="' + x((weeks - taperw / 2) * 7) + '" y="' + (top + 14) + '" text-anchor="middle" fill="#1baf7a" font-weight="600">taper</text>';
    $('ctl-chart').innerHTML = s + '</svg>';
    var end = pts[pts.length - 1];
    $('ctl-out').innerHTML = kv([
      ['CTL a 16. hét végén', f0(end[1]) + ' pont', 'big'],
      ['Legnagyobb heti CTL-emelkedés a szimulációban', '+' + f1(maxRamp) + ' pont' + (maxRamp > 8 ? ' — a heurisztikus plafon fölött!' : ''), maxRamp > 8 ? 'warn' : ''],
      ['TSB (frissesség) a végén', (end[2] >= 0 ? '+' : '') + f0(end[2]) + ' pont — a taper célja a pozitív tartomány']
    ]);
  }

  function dur() {
    var fr = +$('fresh').value, ti = +$('tired').value;
    if (!fr || !ti) { $('dur-out').innerHTML = '<div class="k">Írd be a két tesztértéket</div><div class="v">—</div>'; return; }
    var drop = (fr - ti) / fr * 100;
    var band = P.durability_test.bands.filter(function (b) { return drop <= b.max_drop_pct; })[0];
    var lab = band ? band.label : 'fejlesztendő — a következő blokk fókusza a Z1-volumen és az erősítés';
    $('dur-out').innerHTML = kv([
      ['Esés fáradtan', f1(drop) + ' %', 'big'],
      ['Sáv (edzői protokoll, C)', lab],
      ['Emlékeztető', 'a 08. modul 13. oldalának tesztje, kJ-célokkal; szénhidráttal az esésnek kisebbnek kell lennie']
    ]);
  }

  calc();
})();
