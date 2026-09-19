// Időköltségvetés-kalkulátor — paraméterek: data/tools/idokoltsegvetes.yaml → window.HT_TOOL.
(function () {
  var P = window.HT_TOOL; if (!P) return;
  var LS = window.HT && window.HT.ls;
  var $ = function (id) { return document.getElementById(id); };
  var f1 = function (x) { return String(Math.round(x * 10) / 10).replace('.', ','); };
  var f0 = function (x) { return String(Math.round(x)); };
  var kv = function (rows) { return rows.map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v ' + (r[2] || '') + '">' + r[1] + '</div>'; }).join(''); };

  // --- előbeállítások
  P.presets.forEach(function (p) { var o = document.createElement('option'); o.value = p.id; o.textContent = p.label; $('preset').appendChild(o); });
  var custom = document.createElement('option'); custom.value = ''; custom.textContent = 'saját értékek'; $('preset').appendChild(custom);
  P.physics.cda_options.forEach(function (o) { var e = document.createElement('option'); e.value = o.cda; e.textContent = o.label + ' · ' + String(o.cda).replace('.', ','); $('cda').appendChild(e); });
  P.physics.crr_options.forEach(function (o) { var e = document.createElement('option'); e.value = o.crr; e.textContent = o.label + ' · ' + String(o.crr).replace('.', ','); $('crr').appendChild(e); });
  $('cda').selectedIndex = 2; $('crr').selectedIndex = 1;

  var saved = LS && LS('ht.idokoltsegvetes');
  if (saved) Object.keys(saved).forEach(function (k) { if ($(k) && saved[k] !== undefined && saved[k] !== '') $(k).value = saved[k]; });
  function applyPreset() {
    var p = P.presets.filter(function (x) { return x.id === $('preset').value; })[0];
    if (!p) { $('preset-note').textContent = ''; return; }
    $('tav').value = p.distance_km; $('v').value = p.speed_kmh; $('alvas').value = p.sleep_h; $('egyeb').value = p.other_h;
    $('brevet').value = p.id === 'pbp' ? '1' : '0';
    $('preset-note').textContent = p.note;
  }
  $('preset').addEventListener('change', function () { applyPreset(); calc(); });
  ['tav', 'v', 'alvas', 'egyeb', 'brevet'].forEach(function (id) { $(id).addEventListener('input', function () { $('preset').value = ''; $('preset-note').textContent = ''; calc(); }); });
  ['cda', 'cda-own', 'crr', 'm', 'grade', 'wind', 'alt', 'temp', 'p'].forEach(function (id) { $(id).addEventListener('input', calc); });

  // --- fizika (Martin 1998)
  function rho(altM, tempC) { var pPa = 101325 * Math.pow(1 - 2.25577e-5 * altM, 5.25588); return pPa / (287.05 * (tempC + 273.15)); }
  function powerAt(vKmh, o) {
    var v = vKmh / 3.6, th = Math.atan(o.grade / 100), vw = v + o.wind / 3.6;
    return (0.5 * o.rho * o.cda * vw * Math.abs(vw) * v + o.crr * o.m * P.physics.g * Math.cos(th) * v + o.m * P.physics.g * Math.sin(th) * v) / P.physics.eta;
  }
  function speedAt(Pw, o) { var lo = 0, hi = 120; for (var i = 0; i < 60; i++) { var mid = (lo + hi) / 2; if (powerAt(mid, o) < Pw) lo = mid; else hi = mid; } return (lo + hi) / 2; }

  var R = {};
  function calc() {
    var D = +$('tav').value || 0, v = +$('v').value || 1, sl = +$('alvas').value || 0, ot = +$('egyeb').value || 0;
    var h = Math.max(0.5, 24 - sl - ot), km = v * h, days = D / km, hours = days * 24;
    var T = function (vv, hh) { return D / (vv * hh) * 24; };
    var lev = [T(v, h) - T(v + 1, h), T(v, h) - T(v, h + 1), T(v, h) - T(v, h + 0.5)];
    var wattFor1 = null;
    var o = phys();
    if (o) { wattFor1 = powerAt(v + 1, o) - powerAt(v, o); }
    R = { D: D, v: v, sl: sl, ot: ot, h: h, km: km, days: days, hours: hours, lev: lev, wattFor1: wattFor1 };
    var brevet = $('brevet').value === '1';
    var rows = [
      ['Napi mozgásóra (24 − ' + f1(sl) + ' alvás − ' + f1(ot) + ' egyéb)', f1(h) + ' óra'],
      ['Mozgáshányad az eltelt időre · az ébren töltött időre', f0(h / 24 * 100) + ' % · ' + f0(h / (24 - sl) * 100) + ' %'],
      ['Napi táv', f0(km) + ' km/nap', 'big'],
      ['Célidő', f1(days) + ' nap (' + f0(hours) + ' óra)', 'big'],
      ['Célidő + ' + P.reserve_pct + ' % tartalék', f1(days * (1 + P.reserve_pct / 100)) + ' nap'],
      ['Bruttó átlagsebesség', f1(D / hours) + ' km/h']
    ];
    $('out').innerHTML = kv(rows);
    var w = [];
    if (h / 24 < 0.5) w.push('50 % alatti mozgáshányad: ez túrázás, nem verseny — a következő verseny nem a wattról szól (5–6. oldal).');
    if (sl < 1.5 && days > 4) w.push('5+ napos versenyen 1,5 óra alatti alvás: a „ma kihagyom, holnap pótolom” nem működik (04. modul).');
    if (brevet) {
      var lim = brevetLimit(D); var okB = hours <= lim;
      w.push((okB ? 'Brevet-időlimit: ' : '<b>Brevet-időlimit túllépve:</b> ') + f0(lim) + ' óra a ' + f0(D) + ' km-re (ACP kontrollzárás, ' + f1(D / lim) + ' km/h bruttó); a terved ' + f0(hours) + ' óra.');
    }
    $('warn').innerHTML = w.map(function (s) { return '<p class="note" style="border-left:4px solid var(--warning);padding-left:10px">' + s + '</p>'; }).join('');

    $('levers').innerHTML = kv([
      ['+1 km/h mozgósebesség' + (wattFor1 !== null ? ' (≈ +' + f0(wattFor1) + ' W a te bringádon)' : ''), '−' + f1(lev[0]) + ' óra'],
      ['+1 óra mozgás naponta (= −1 h alvás vagy −1 h egyéb állás)', '−' + f1(lev[1]) + ' óra'],
      ['−30 perc egyéb állás naponta', '−' + f1(lev[2]) + ' óra'],
      ['1 óra mozgás ≡ sebesség', f1(v / h) + ' km/h']
    ]);
    var best = lev.indexOf(Math.max.apply(null, lev));
    var names = ['a sebesség (watt, aero, gumi)', 'a mozgásidő (alvás és megállás együtt)', 'a megállások'];
    $('verdict').innerHTML = '<b>Szűk keresztmetszet nálad: ' + names[best] + '.</b> ' + (h / 24 < 0.7 ? 'Alacsony mozgáshányadnál az álló idő a legolcsóbb nyereség; a watt drága (8. oldal).' : 'Magas mozgáshányadnál már csak a sebesség és az alvás minősége marad (5. oldal).');
    drawBars(lev);
    if (o) physOut(o);
    if (LS) { var s = {}; ['preset', 'tav', 'v', 'alvas', 'egyeb', 'brevet', 'cda', 'cda-own', 'crr', 'm', 'grade', 'wind', 'alt', 'temp', 'p'].forEach(function (k) { s[k] = $(k).value; }); LS('ht.idokoltsegvetes', s); }
  }

  function brevetLimit(D) {
    var t = 0, prev = 0;
    for (var i = 0; i < P.brevet_limits.length; i++) {
      var b = P.brevet_limits[i]; var seg = Math.min(D, b.to_km) - prev; if (seg <= 0) break;
      t += seg / b.min_kmh; prev = b.to_km;
    }
    return t;
  }

  function phys() {
    var cda = +$('cda-own').value || +$('cda').value, crr = +$('crr').value, m = +$('m').value || 85;
    if (!cda || !crr) return null;
    return { cda: cda, crr: crr, m: m, grade: +$('grade').value || 0, wind: +$('wind').value || 0, rho: rho(+$('alt').value || 0, +$('temp').value || 15), alt: +$('alt').value || 0 };
  }
  function physOut(o) {
    var Pw = +$('p').value || 150;
    var pAdj = Pw * (1 + P.physics.power_per_100m_pct / 100 * (o.alt / 100));
    var vNow = speedAt(pAdj, o), vFlat = speedAt(Pw, { cda: o.cda, crr: o.crr, m: o.m, grade: 0, wind: 0, rho: 1.2 });
    var needV = +$('v').value || 22;
    var pNeed = powerAt(needV, o) / (1 + P.physics.power_per_100m_pct / 100 * (o.alt / 100));
    var aero = 0.5 * o.rho * o.cda * Math.pow(vNow / 3.6 + o.wind / 3.6, 2) * (vNow / 3.6) / P.physics.eta;
    var share = pAdj > 0 ? aero / pAdj * 100 : 0;
    $('phys').innerHTML = kv([
      ['Sebesség ' + Pw + ' W-on a megadott terepen (lejtés ' + f1(o.grade) + ' %, szél ' + f0(o.wind) + ' km/h, ' + f0(o.alt) + ' m)', f1(vNow) + ' km/h', 'big'],
      ['Ugyanez síkon, szélcsendben, tengerszinten', f1(vFlat) + ' km/h'],
      ['Ehhez a mozgósebességhez (' + f1(needV) + ' km/h) kellő teljesítmény ezen a terepen', f0(pNeed) + ' W'],
      ['Légellenállás aránya az ellenállásban', f0(Math.max(0, Math.min(100, share))) + ' %'],
      ['Magasság miatti teljesítménykorrekció (' + P.physics.power_per_100m_pct + ' % / 100 m)', f0(pAdj) + ' W hasznos ' + Pw + ' W-ból'],
      ['Levegősűrűség', String(Math.round(o.rho * 1000) / 1000).replace('.', ',') + ' kg/m³']
    ]);
    drawCurve(o, Pw);
  }

  function drawBars(lev) {
    var W = 760, H = 150, L = 200, RW = W - L - 60, max = Math.max.apply(null, lev.concat([1]));
    var labs = ['+1 km/h', '+1 óra mozgás / nap', '−30 perc állás / nap'], cols = ['#2a78d6', '#0d366b', '#eb6834'];
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" font-family="Inter, system-ui, sans-serif" font-size="12">';
    lev.forEach(function (v, i) {
      var y = 14 + i * 42, w = Math.max(2, v / max * RW);
      s += '<text x="' + (L - 10) + '" y="' + (y + 18) + '" text-anchor="end" fill="#52514e" font-weight="500">' + labs[i] + '</text>';
      s += '<rect x="' + L + '" y="' + y + '" width="' + w + '" height="26" rx="3" fill="' + cols[i] + '"/>';
      s += '<text x="' + (L + w + 8) + '" y="' + (y + 18) + '" fill="#0b0b0b" font-weight="600">−' + f1(v) + ' óra a célidőn</text>';
    });
    $('bars').innerHTML = s + '</svg>';
  }

  function drawCurve(o, Pw) {
    var W = 760, H = 220, L = 50, RW = W - L - 20, top = 20, bot = 180;
    var x = function (p) { return L + (p - 80) / (260 - 80) * RW; };
    var vmax = speedAt(260, { cda: 0.25, crr: 0.0035, m: o.m, grade: 0, wind: 0, rho: 1.2 }) + 2;
    var y = function (v) { return bot - v / vmax * (bot - top); };
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" font-family="Inter, system-ui, sans-serif" font-size="11">';
    for (var v = 10; v <= vmax; v += 10) s += '<line x1="' + L + '" y1="' + y(v) + '" x2="' + (L + RW) + '" y2="' + y(v) + '" stroke="#e1e0d9"/><text x="' + (L - 6) + '" y="' + (y(v) + 4) + '" text-anchor="end" fill="#898781">' + v + '</text>';
    for (var p = 100; p <= 250; p += 50) s += '<text x="' + x(p) + '" y="' + (bot + 16) + '" text-anchor="middle" fill="#898781">' + p + ' W</text>';
    var series = [[o, '#184f95', 'a te beállításod'], [{ cda: o.cda, crr: o.crr, m: o.m, grade: 0, wind: 0, rho: 1.2 }, '#5598e7', 'ugyanez síkon, szélcsendben'], [{ cda: 0.26, crr: 0.0035, m: o.m, grade: 0, wind: 0, rho: 1.2 }, '#eda100', 'aerobar + prémium gumi, síkon']];
    series.forEach(function (sr) {
      var pts = []; for (var p = 80; p <= 260; p += 10) pts.push(x(p) + ' ' + y(speedAt(p, sr[0])));
      s += '<path d="M' + pts.join(' L') + '" fill="none" stroke="' + sr[1] + '" stroke-width="2.2"/>';
    });
    var vNow = speedAt(Pw * (1 + P.physics.power_per_100m_pct / 100 * (o.alt / 100)), o);
    s += '<circle cx="' + x(Pw) + '" cy="' + y(vNow) + '" r="4" fill="#184f95" stroke="#fff" stroke-width="1.5"/>';
    s += '<text x="' + (x(Pw) + 8) + '" y="' + (y(vNow) - 6) + '" fill="#184f95" font-weight="600">' + f1(vNow) + ' km/h @ ' + Pw + ' W</text>';
    var ly = H - 6;
    series.forEach(function (sr, i) { s += '<rect x="' + (L + i * 230) + '" y="' + (ly - 8) + '" width="12" height="8" fill="' + sr[1] + '"/><text x="' + (L + i * 230 + 16) + '" y="' + ly + '" fill="#52514e" font-size="10">' + sr[2] + '</text>'; });
    $('curve').innerHTML = s + '</svg>';
  }

  // --- sablon
  var F = {}; document.querySelectorAll('#sablon-f textarea').forEach(function (t) { F[t.getAttribute('data-k')] = t; });
  var sv = LS && LS('ht.sablon.08'); if (sv) Object.keys(sv).forEach(function (k) { if (F[k]) F[k].value = sv[k]; });
  var saveS = function () { if (!LS) return; var o = {}; Object.keys(F).forEach(function (k) { o[k] = F[k].value; }); LS('ht.sablon.08', o); };
  Object.keys(F).forEach(function (k) { F[k].addEventListener('input', saveS); });
  $('atvesz').addEventListener('click', function () {
    calc();
    var names = ['a sebesség', 'a mozgásidő', 'a megállások']; var best = R.lev.indexOf(Math.max.apply(null, R.lev));
    F.verseny.value = f0(R.D) + ' km';
    F.v.value = f1(R.v) + ' km/h';
    F.alvas.value = f1(R.sl) + ' óra/éj';
    F.egyeb.value = f1(R.ot) + ' óra/nap → mozgáshányad ' + f0(R.h / (24 - R.sl) * 100) + ' % az ébren töltött időre';
    F.napi.value = '24 − ' + f1(R.sl) + ' − ' + f1(R.ot) + ' = ' + f1(R.h) + ' óra × ' + f1(R.v) + ' km/h = ' + f0(R.km) + ' km/nap';
    F.celido.value = f1(R.days) + ' nap → ' + f1(R.days * (1 + P.reserve_pct / 100)) + ' nap tartalékkal';
    F.karok.value = '−' + f1(R.lev[0]) + ' h · −' + f1(R.lev[1]) + ' h · −' + f1(R.lev[2]) + ' h → ' + names[best];
    if ($('brevet').value === '1') F.brevet.value = 'ACP zárás: ' + f0(brevetLimit(R.D)) + ' óra a ' + f0(R.D) + ' km-re (' + f1(R.D / brevetLimit(R.D)) + ' km/h bruttó)';
    saveS();
  });
  $('torol').addEventListener('click', function () { Object.keys(F).forEach(function (k) { F[k].value = ''; }); saveS(); });
  $('print').addEventListener('click', function () { document.body.classList.add('print-sablon'); window.print(); setTimeout(function () { document.body.classList.remove('print-sablon'); }, 500); });

  if (!saved) { $('preset').value = 'tcr-kozep'; applyPreset(); }
  calc();
})();
