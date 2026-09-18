// Önellenőrző kvíz — a kérdéseket a build a data/quiz/<modul>.yaml-ból írja a window.HT_QUIZ változóba.
(function () {
  var Q = window.HT_QUIZ; if (!Q) return;
  var root = document.getElementById('quiz'); if (!root) return;
  var LS = window.HT && window.HT.ls;
  var answered = 0, correct = 0;
  var key = 'ht.kviz.' + Q.module;

  var head = document.createElement('div');
  var best = LS ? LS(key) : null;
  head.className = 'note';
  head.innerHTML = 'Válaszd ki a legjobb választ; a helyes megoldás és a modul oldalszáma a válasz után jelenik meg.' + (best ? ' Legjobb eredményed eddig: <b class="mono">' + best.correct + ' / ' + best.total + '</b>.' : '');
  root.appendChild(head);

  Q.questions.forEach(function (q, i) {
    var box = document.createElement('div'); box.className = 'qq';
    var opts = q.options.map(function (o, j) {
      return '<label class="opt" data-j="' + j + '"><input type="radio" name="q' + i + '" value="' + j + '"><span>' + o + '</span></label>';
    }).join('');
    box.innerHTML = '<div class="qn">' + (i + 1) + ' / ' + Q.questions.length + '</div><div class="qt">' + q.q + '</div>' + opts +
      '<div class="why"><b>Miért:</b> ' + q.why + ' <span class="muted">→ <a href="#p-' + String(q.page).padStart(2, '0') + '">' + q.page + '. oldal</a></span></div>';
    box.addEventListener('change', function (e) {
      if (box.classList.contains('done')) return;
      var j = +e.target.value; box.classList.add('done');
      box.querySelectorAll('.opt').forEach(function (l) {
        var jj = +l.getAttribute('data-j');
        if (jj === q.answer) l.classList.add('right'); else if (jj === j) l.classList.add('wrong');
        l.querySelector('input').disabled = true;
      });
      answered++; if (j === q.answer) correct++;
      score();
    });
    root.appendChild(box);
  });

  var sc = document.createElement('div'); sc.className = 'score'; root.appendChild(sc);
  var again = document.createElement('button'); again.className = 'btn sec noprint'; again.textContent = 'Újra'; again.style.display = 'none';
  again.addEventListener('click', function () { location.reload(); }); root.appendChild(again);

  function score() {
    sc.textContent = 'Eredmény: ' + correct + ' / ' + answered + (answered < Q.questions.length ? ' (' + (Q.questions.length - answered) + ' hátra)' : '');
    if (answered === Q.questions.length) {
      var msg = correct >= 9 ? 'Mehet a következő modul.' : correct >= 6 ? 'A hibás kérdéseknél lapozz vissza a jelzett oldalra.' : 'Olvasd újra az összefoglalót (16. oldal), majd próbáld újra.';
      sc.textContent += ' — ' + msg;
      again.style.display = '';
      if (LS) { var b = LS(key); if (!b || correct > b.correct) LS(key, { correct: correct, total: Q.questions.length, when: new Date().toISOString().slice(0, 10) }); }
    }
  }
})();
