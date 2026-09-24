// Etetési és hidratálási terv — paraméterek: data/tools/etetesiterv.yaml → window.HT_TOOL.
(function () {
  var P = window.HT_TOOL; if (!P) return;
  var LS = window.HT && window.HT.ls;
  var $ = function (id) { return document.getElementById(id); };
  var f1 = function (x) { return String(Math.round(x * 10) / 10).replace('.', ','); };
  var f0 = function (x) { return String(Math.round(x)); };
  var f2 = function (x) { return String(Math.round(x * 100) / 100).replace('.', ','); };
  var fk = function (x) { return f0(x).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); };
  var kv = function (rows) { return rows.map(function (r) { return '<div class="k">' + r[0] + '</div><div class="v ' + (r[2] || '') + '">' + r[1] + '</div>'; }).join(''); };
  var warnBox = function (id, arr) { $(id).innerHTML = arr.map(function (s) { return '<p class="note" style="border-left:4px solid var(--warning);padding-left:10px">' + s + '</p>'; }).join(''); };

  // --- selects
  P.formats.forEach(function (f) { var o = document.createElement('option'); o.value = f.id; o.textContent = f.label; $('fmt').appendChild(o); });
  P.sweat.bands.forEach(function (b) { var o = document.createElement('option'); o.value = b.id; o.textContent = b.label + ' · ' + f1(b.l_h[0]) + '–' + f1(b.l_h[1]) + ' l/h'; $('sweat-band').appendChild(o); });
  P.sweat.na_bands.forEach(function (b) { var o = document.createElement('option'); o.value = b.mg_l; o.textContent = b.label + ' · ~' + b.mg_l + ' mg/l'; $('na-band').appendChild(o); });
  $('fmt').value = 'onellato'; $('sweat-band').selectedIndex = 1; $('na-band').selectedIndex = 1;

  var IDS = ['fmt', 'kg', 'cm', 'ev', 'sex', 'rideh', 'days', 'kcalh', 'choh', 'sweat-band', 'sweat-own', 'na-band', 'na-own', 'sleep-at', 'caf-start', 'caf-dose', 'caf-nap'];
  var saved = LS && LS('ht.etetesiterv');
  if (saved) Object.keys(saved).forEach(function (k) { if ($(k) && saved[k] !== undefined && saved[k] !== '') $(k).value = saved[k]; });

  function fmt() { return P.formats.filter(function (x) { return x.id === $('fmt').value; })[0] || P.formats[0]; }
  function applyFmt() {
    var f = fmt();
    $('rideh').value = f.ride_h_default; $('days').value = f.days_default;
    $('kcalh').value = Math.round((f.intake_kcal_h[0] + f.intake_kcal_h[1]) / 2 / 10) * 10;
    var kmid = +$('kcalh').value; $('choh').value = Math.min(Math.round((f.cho_g_h[0] + f.cho_g_h[1]) / 2 / 5) * 5, Math.floor(kmid * 0.9 / P.cho_kcal_per_g / 5) * 5);
    $('fmt-note').textContent = f.note;
  }
  $('fmt').addEventListener('change', function () { applyFmt(); calc(); });
  IDS.forEach(function (id) { if (id !== 'fmt') $(id).addEventListener('input', calc); });
  if (!saved) applyFmt();

  function bmr() {
    var kg = +$('kg').value || 75, cm = +$('cm').value || 180, ev = +$('ev').value || 40;
    return 10 * kg + 6.25 * cm - 5 * ev + ($('sex').value === 'f' ? -161 : 5);
  }

  var R = {};
  function calc() {
    var f = fmt(), kg = +$('kg').value || 75, rideh = Math.min(24, +$('rideh').value || 16), days = +$('days').value || 1;
    var kcalh = +$('kcalh').value || 250, choh = +$('choh').value || 75, B = bmr();
    var resth = 24 - rideh;
    var tee = f.tee_kcal_h_elapsed * rideh + P.rest_kcal_h * resth;          // eltelt órára vetített forgalom, nyereg + pihenő
    var teeNonstop = f.tee_kcal_h_elapsed * 24;
    var intakeDay = kcalh * rideh;                                            // első fél
    var drop = P.second_half_drop_pct / 100;
    var intakeAvg = days > 1 ? intakeDay * (1 - drop / 2) : intakeDay;        // verseny egészére: második fél −drop
    var ceiling = P.intake_ceiling_x_bmr * B;
    var deficit = tee - Math.min(intakeAvg, ceiling * 1.6);                   // a plafon fölött nem számolunk többet (egyéni 4× korlát)
    var fatKgDay = deficit / P.fat_kcal_per_kg;
    var choKcal = choh * P.cho_kcal_per_g;
    var ib = f.intake_kcal_h;
    $('kcalh-hint').textContent = f.label + ': ' + ib[0] + '–' + ib[1] + ' kcal/h sáv';
    R = { B: B, tee: tee, intakeDay: intakeDay, intakeAvg: intakeAvg, ceiling: ceiling, deficit: deficit, fatKgDay: fatKgDay, kg: kg, rideh: rideh, days: days, kcalh: kcalh, choh: choh, f: f };
    $('energy').innerHTML = kv([
      ['Alapanyagcsere (Mifflin–St Jeor)', fk(B) + ' kcal/nap'],
      ['Napi forgalom (' + f1(rideh) + ' nyeregóra × ' + f.tee_kcal_h_elapsed + ' + ' + f1(resth) + ' pihenőóra × ' + P.rest_kcal_h + ')', fk(tee) + ' kcal/nap', 'big'],
      ['Ugyanez nonstop tempón (24 × ' + f.tee_kcal_h_elapsed + ')', fk(teeNonstop) + ' kcal/nap'],
      ['Bevitel a nyeregben (' + f1(rideh) + ' × ' + kcalh + ' kcal/h)', fk(intakeDay) + ' kcal/nap'],
      ['Szénhidrátból ebből (' + choh + ' g/h × 4 kcal)', fk(choKcal * rideh) + ' kcal/nap (' + f0(choKcal / kcalh * 100) + ' %)'],
      ['Tartós bevitel-plafon (' + P.intake_ceiling_x_bmr + ' × alapanyagcsere, populációs átlag)', fk(ceiling) + ' kcal/nap'],
      ['Napi hiány (a második fél ' + P.second_half_drop_pct + ' %-os esésével)', fk(deficit) + ' kcal/nap', deficit > 5000 ? 'warn' : ''],
      ['Zsírban', f2(fatKgDay) + ' kg/nap → ' + f1(fatKgDay * days) + ' kg a versenyen'],
      ['Forgalom / alapanyagcsere', f1(tee / B) + ' ×']
    ]);
    var w = [];
    if (kcalh > ib[1]) w.push('A bevitel-cél (' + kcalh + ' kcal/h) a formátum mért/tapasztalati sávja (' + ib[0] + '–' + ib[1] + ') fölött van: csak folyékony, stáb-adagolt formában és edzett béllel tartható.');
    if (choKcal > kcalh) w.push('A szénhidrát-cél (' + choh + ' g/h = ' + choKcal + ' kcal) több, mint a teljes bevitel-cél — emeld a kcal/h-t vagy csökkentsd a g/h-t.');
    if (choh > 90) w.push('90 g/h fölött: a hasznosulás 72–75 %, és többnapos versenyen a 120 g/h nem bizonyított (4. oldal). Csak a 17. oldal bél-edzése után.');
    if (intakeDay > ceiling) w.push('A tervezett napi bevitel (' + fk(intakeDay) + ') a tartós plafon (' + fk(ceiling) + ') fölött van: egyéni kerékpáros esetekben 4 × alapanyagcserét mértek, de ez nem a mezőny.');
    if (fatKgDay * days > 4) w.push('<b>' + f1(fatKgDay * days) + ' kg zsírnak megfelelő hiány a versenyen:</b> többnapos szólón 2–5 kg a mért tartomány; a döntéseid is romlanak (2. oldal).');
    if (days >= 5 && fatKgDay > 0.8) w.push('5+ napon napi 0,8 kg fölötti hiány: a raktár a 4–6. nap körül a határon — emeld a folyékony bevitelt vagy a pihenő-étkezéseket.');
    warnBox('energy-warn', w);
    drawEnergy(tee, intakeDay, intakeAvg, ceiling);
    fluid(); caffeine();
    if (LS) { var s = {}; IDS.forEach(function (k) { s[k] = $(k).value; }); LS('ht.etetesiterv', s); }
  }

  function drawEnergy(tee, intake, intakeAvg, ceiling) {
    var W = 760, H = 150, L = 210, RW = W - L - 90, max = Math.max(tee, intake, ceiling, 1);
    var rows = [['forgalom / nap', tee, '#2a78d6'], ['bevitel, első fél', intake, '#eb6834'], ['bevitel, verseny-átlag', intakeAvg, '#f0a07c'], ['tartós plafon (2,4 × BMR)', ceiling, '#898781']];
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" font-family="Inter, system-ui, sans-serif" font-size="12">';
    rows.forEach(function (r, i) {
      var y = 10 + i * 34, w = Math.max(2, r[1] / max * RW);
      s += '<text x="' + (L - 10) + '" y="' + (y + 16) + '" text-anchor="end" fill="#52514e" font-weight="500">' + r[0] + '</text>';
      s += '<rect x="' + L + '" y="' + y + '" width="' + w + '" height="22" rx="3" fill="' + r[2] + '"/>';
      s += '<text x="' + (L + w + 8) + '" y="' + (y + 16) + '" fill="#0b0b0b" font-weight="600">' + fk(r[1]) + ' kcal</text>';
    });
    $('energy-bars').innerHTML = s + '</svg>';
  }

  function fluid() {
    var kg = R.kg, rideh = R.rideh;
    var band = P.sweat.bands.filter(function (b) { return b.id === $('sweat-band').value; })[0] || P.sweat.bands[1];
    var own = +$('sweat-own').value;
    var sw = own ? [own, own] : band.l_h;
    var na = +$('na-own').value || +$('na-band').value || P.sweat.na_mg_l_default;
    var floor = [P.fluid.floor_ml_kg_h[0] * kg, P.fluid.floor_ml_kg_h[1] * kg];
    var eah = P.fluid.eah_ml_kg_day * kg;
    var naLoss = [sw[0] * na, sw[1] * na];
    var naRep = [Math.max(P.sodium.base_mg_h[0], naLoss[0] * P.sodium.replace_pct[0] / 100), Math.min(2000, Math.max(P.sodium.base_mg_h[1], naLoss[1] * P.sodium.replace_pct[1] / 100))];
    var dayIn = [Math.min(sw[0], Math.max(floor[0] / 1000, sw[0])) * rideh, sw[1] * rideh];
    var rows = [
      ['Izzadásráta (' + (own ? 'saját mérés' : band.label + ', szerkesztői sáv') + ')', f1(sw[0]) + (own ? '' : '–' + f1(sw[1])) + ' l/h', 'big'],
      ['Órás padló (6–8 ml/kg): ez alatt nőtt a hányinger', f0(floor[0]) + '–' + f0(floor[1]) + ' ml/h'],
      ['Órás plafon: legfeljebb az izzadásráta, és ne hízz', '≤ ' + f0(sw[1] * 1000) + ' ml/h'],
      ['Napi összes (' + f1(rideh) + ' nyeregóra, izzadás szerint)', f1(dayIn[0]) + '–' + f1(dayIn[1]) + ' l'],
      ['Hyponatraemia-küszöb (168 ml/kg/nap összbevitel)', f1(eah / 1000) + ' l/nap', 'warn'],
      ['Nátriumveszteség (' + na + ' mg/l × izzadás)', f0(naLoss[0]) + '–' + f0(naLoss[1]) + ' mg/h'],
      ['Nátrium-cél (alap 300–600; magas veszteségnél 50–80 % pótlás)', f0(naRep[0]) + '–' + f0(naRep[1]) + ' mg/h', 'big'],
      ['Ugyanez sóban (1 g só = 393 mg Na)', f1(naRep[0] / P.sodium.na_per_g_salt_mg) + '–' + f1(naRep[1] / P.sodium.na_per_g_salt_mg) + ' g/h'],
      ['Ital nátriumtartalma', P.sodium.drink_mg_l[0] + '–' + P.sodium.drink_mg_l[1] + ' mg/l']
    ];
    $('fluid').innerHTML = kv(rows);
    R.fluid = { sw: sw, floor: floor, eah: eah, naRep: naRep, na: na, own: own, band: band };
    var w = [];
    if (dayIn[1] * 1000 > eah) w.push('<b>A napi izzadás szerinti maximum (' + f1(dayIn[1]) + ' l) a hyponatraemia-küszöb (' + f1(eah / 1000) + ' l) fölött van:</b> hőségben a vér nátriumának hígulása a valós kockázat — egyél sót az itallal, és a plafon a küszöb, nem az izzadás.');
    if (sw[0] * 1000 < floor[0]) w.push('Az izzadásráta alsó értéke a padló alatt van: hűvösben is igyál legalább ' + f0(floor[0]) + ' ml/h-t — ultrán a kevés folyadék előzi meg a hányingert.');
    if (!own) w.push('Nincs saját izzadásráta: a sáv szerkesztői összeállítás, ultrakerékpáron 12 óránál hosszabb mérés nincs. A 17. oldal 2. tesztje egy edzés.');
    warnBox('fluid-warn', w);
  }

  function caffeine() {
    var kg = R.kg, dose = +$('caf-dose').value || 75, start = +$('caf-start').value || 0, nap = $('caf-nap').value === '1';
    var sleepAt = $('sleep-at').value || '23:00', hh = +sleepAt.split(':')[0], mm = +sleepAt.split(':')[1];
    var sleepMin = hh * 60 + mm;
    var gap107 = P.caffeine.sleep_gap_h[0][1], gap217 = P.caffeine.sleep_gap_h[1][1];
    var gap = dose <= 107 ? gap107 : dose <= 217 ? gap217 : gap217 + (dose - 217) / 110 * 4;  // 217 fölött lineáris extrapoláció (nem mért)
    var lastMin = ((sleepMin - gap * 60) % 1440 + 1440) % 1440;
    var t2 = function (m) { var h = Math.floor(m / 60) % 24, mi = Math.round(m % 60); return (h < 10 ? '0' : '') + h + ':' + (mi < 10 ? '0' : '') + mi; };
    var perDoseMgKg = dose / kg;
    var single = [P.caffeine.dose_mg_kg[0] * kg, P.caffeine.dose_mg_kg[1] * kg];
    var fieldDay = P.caffeine.field_avg_mg_kg_day * kg;
    var rows = [
      ['Egy adag hatásos sávja (1–3 mg/kg)', f0(single[0]) + '–' + f0(single[1]) + ' mg'],
      ['A te ismételt adagod', dose + ' mg = ' + f1(perDoseMgKg) + ' mg/kg', perDoseMgKg > 3 ? 'warn' : ''],
      ['Ritmus', dose + ' mg 60–90 percenként a fáradtság kezdetétől (rajt + ' + start + ' h), nem a rajtnál'],
      ['Utolsó ' + dose + ' mg a ' + sleepAt + '-kor tervezett alvás előtt', 'legkésőbb ' + t2(lastMin) + ' (≥ ' + f1(gap) + ' óra)', 'big'],
      ['Koffein-alvás', nap ? '200 mg közvetlenül a 15–30 perces mikroalvás elején; utána 4–6 óra koffeinmentes' : 'kihagyva'],
      ['Mért terepátlag 24 órás versenyen', f0(fieldDay) + ' mg/nap (~2 mg/kg) — a napi plafonra ultra-adat nincs']
    ];
    $('caf').innerHTML = kv(rows);
    R.caf = { dose: dose, last: t2(lastMin), gap: gap, nap: nap, sleepAt: sleepAt, start: start };
    drawCaf(sleepMin, gap, dose);
  }

  function drawCaf(sleepMin, gap, dose) {
    var W = 760, H = 110, L = 40, RW = W - L - 40;
    var span = 16; // óra az alvás előtt
    var x = function (hBefore) { return L + (span - hBefore) / span * RW; };
    var s = '<svg viewBox="0 0 ' + W + ' ' + H + '" font-family="Inter, system-ui, sans-serif" font-size="11">';
    s += '<rect x="' + x(span) + '" y="30" width="' + (x(gap) - x(span)) + '" height="22" rx="3" fill="#1baf7a" fill-opacity=".45"/>';
    s += '<rect x="' + x(gap) + '" y="30" width="' + (x(0) - x(gap)) + '" height="22" rx="3" fill="#ec835a" fill-opacity=".4"/>';
    s += '<line x1="' + L + '" y1="62" x2="' + (L + RW) + '" y2="62" stroke="#cfcdc4" stroke-width="1.5"/>';
    for (var h = span; h >= 0; h -= 4) s += '<line x1="' + x(h) + '" y1="58" x2="' + x(h) + '" y2="66" stroke="#cfcdc4"/><text x="' + x(h) + '" y="80" text-anchor="middle" fill="#898781">' + (h ? '−' + h + ' h' : 'alvás') + '</text>';
    s += '<text x="' + x(span) + '" y="22" fill="#52514e" font-weight="600">' + dose + ' mg még rendben (zöld) · ' + f1(gap) + ' órán belül már rontja az alvást (narancs)</text>';
    s += '<text x="' + x(gap) + '" y="100" text-anchor="middle" fill="#d03b3b" font-weight="600">utolsó adag: −' + f1(gap) + ' h</text>';
    $('caf-bar').innerHTML = s + '</svg>';
  }

  // --- sablon
  var F = {}; document.querySelectorAll('#sablon-f textarea').forEach(function (t) { F[t.dataset.k] = t; });
  var sv = LS && LS('ht.sablon.03'); if (sv) Object.keys(sv).forEach(function (k) { if (F[k]) F[k].value = sv[k]; });
  var saveS = function () { if (!LS) return; var o = {}; Object.keys(F).forEach(function (k) { o[k] = F[k].value; }); LS('ht.sablon.03', o); };
  Object.keys(F).forEach(function (k) { F[k].addEventListener('input', saveS); });
  $('atvesz').addEventListener('click', function () {
    var f = R.f, fl = R.fluid, c = R.caf;
    F.formatum.value = f.label + ', ' + R.days + ' nap, ' + f1(R.rideh) + ' nyeregóra/nap; hőmérséklet-sáv: ' + (fl.own ? 'saját mérés' : fl.band.label);
    F.bmr.value = fk(R.B) + ' kcal/nap (' + $('kg').value + ' kg, ' + $('cm').value + ' cm, ' + $('ev').value + ' év)';
    F.tee.value = fk(R.tee) + ' kcal/nap (' + f.tee_kcal_h_elapsed + ' kcal/h az eltelt órára a nyeregben, ' + P.rest_kcal_h + ' pihenőn)';
    F.kcalh.value = R.kcalh + ' kcal/h → ' + fk(R.intakeDay) + ' kcal/nap az első félben; tartós plafon ' + fk(R.ceiling) + ' kcal/nap';
    F.cho.value = R.choh + ' g/h, glükóz:fruktóz 2:1 – 1:0,8; a második félben −' + P.second_half_drop_pct + ' % beszámolva' + (R.choh > 90 ? '; 90 fölött csak bél-edzés + teszt után' : '');
    F.deficit.value = fk(R.deficit) + ' kcal/nap ≈ ' + f2(R.fatKgDay) + ' kg zsír/nap → ' + f1(R.fatKgDay * R.days) + ' kg a versenyen';
    F.fluid.value = 'szomj szerint; padló ' + f0(fl.floor[0]) + '–' + f0(fl.floor[1]) + ' ml/h; plafon ≤ ' + f0(fl.sw[1] * 1000) + ' ml/h, ne hízz, <' + f1(fl.eah / 1000) + ' l/nap';
    F.sweat.value = (fl.own ? 'saját mérés: ' + f1(fl.sw[0]) + ' l/h' : 'sáv (' + fl.band.label + '): ' + f1(fl.sw[0]) + '–' + f1(fl.sw[1]) + ' l/h — mérd meg (17. oldal)');
    F.na.value = f0(fl.naRep[0]) + '–' + f0(fl.naRep[1]) + ' mg/h (izzadás-Na ' + fl.na + ' mg/l); ital 230–690 mg/l';
    F.caf.value = c.dose + ' mg 60–90 percenként a rajt + ' + c.start + '. órától; utolsó adag ' + c.last + ' (≥ ' + f1(c.gap) + ' h a ' + c.sleepAt + '-s alvás előtt)' + (c.nap ? '; 200 mg a mikroalvás elején' : '');
    saveS();
  });
  $('print').addEventListener('click', function () { document.body.classList.add('print-sablon'); window.print(); setTimeout(function () { document.body.classList.remove('print-sablon'); }, 500); });
  $('torol').addEventListener('click', function () { Object.keys(F).forEach(function (k) { F[k].value = ''; }); saveS(); });

  calc();
})();
