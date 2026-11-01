/* STR2G Athletes – member profile: view, edit, photo crop. Runs once the members area has loaded. */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var FIELDS = ['displayName', 'city', 'club', 'instagram', 'bio', 'division', 'pbTime', 'goalTime', 'nextRace', 'nextRaceDate', 'goal', 'weightKg', 'goalWeightKg', 'resultsUrl', 'roxfitUrl', 'otherUrl'];
  var LABELS = { club: { prague: 'Prague', brno: 'Brno', ostrava: 'Ostrava', other: 'Elsewhere' }, division: { open: 'Open', pro: 'Pro', doubles: 'Doubles', relay: 'Relay' } };
  var ERRORS = {
    pbTime: 'PB time must look like 1:24:30.', goalTime: 'Goal time must look like 1:15:00.',
    weightKg: 'Weight must be a number between 30 and 250 kg.', goalWeightKg: 'Goal weight must be a number between 30 and 250 kg.',
    resultsUrl: 'Paste a link from results.hyrox.com.', roxfitUrl: 'Paste a link from roxfit.com.', otherUrl: 'Paste a full link starting with https://',
    instagram: 'Instagram handle: letters, numbers, dots and underscores only.', nextRaceDate: 'Pick a valid date.'
  };

  var state = { email: '', profile: null, hasPhoto: false, photoVersion: null };

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function initials() {
    var src = (state.profile && state.profile.displayName) || state.email || 'S';
    var parts = src.split(/[\s@._-]+/).filter(Boolean);
    return ((parts[0] || 'S')[0] + (parts[1] ? parts[1][0] : '')).toUpperCase();
  }
  function photoUrl() { return '/api/athletes/photo?v=' + encodeURIComponent(state.photoVersion || '0'); }

  function paintAvatar(box, size) {
    box.textContent = '';
    if (state.hasPhoto) {
      var img = el('img'); img.src = photoUrl(); img.alt = 'Your profile photo'; img.width = size; img.height = size;
      box.appendChild(img);
    } else {
      var s = el('span', 'initials', initials()); if (size < 140) s.style.fontSize = '48px';
      box.appendChild(s);
    }
  }

  function cell(label, value) {
    var d = el('div'); d.appendChild(el('span', 'meta', label)); d.appendChild(el('span', 'v', value)); return d;
  }
  function chip(label, href) {
    var a = el('a', 'chip', label); a.href = href; a.target = '_blank'; a.rel = 'noopener'; return a;
  }
  function fmtDate(s) {
    try { return new Date(s + 'T12:00:00').toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }); } catch (e) { return s; }
  }

  function renderSummary() {
    var p = state.profile || {};
    paintAvatar($('p-avatar'), 160);
    var has = Object.keys(p).some(function (k) { return k !== 'updatedAt' && p[k] !== '' && p[k] != null; });
    $('p-name').textContent = p.displayName || (has ? 'STR2G Athlete' : 'Set up your profile');
    var sub = [LABELS.club[p.club] ? 'STR2G ' + LABELS.club[p.club] : '', p.city].filter(Boolean).join(' · ');
    $('p-sub').textContent = has ? (sub || 'STR2G Athlete') : 'Add a photo, your race goals and links. Only you can see it.';
    $('p-bio').textContent = p.bio || ''; $('p-bio').hidden = !p.bio;

    var grid = $('p-grid'); grid.textContent = '';
    if (LABELS.division[p.division]) grid.appendChild(cell('Division', LABELS.division[p.division]));
    if (p.pbTime) grid.appendChild(cell('PB', p.pbTime));
    if (p.goalTime) grid.appendChild(cell('Goal time', p.goalTime));
    if (p.nextRace || p.nextRaceDate) grid.appendChild(cell('Next race', [p.nextRace, p.nextRaceDate ? fmtDate(p.nextRaceDate) : ''].filter(Boolean).join(' · ')));
    if (p.weightKg != null || p.goalWeightKg != null) {
      var w = (p.weightKg != null ? p.weightKg : '–') + (p.goalWeightKg != null ? ' → ' + p.goalWeightKg : '') + ' kg';
      grid.appendChild(cell(p.goalWeightKg != null ? 'Weight → goal' : 'Weight', w));
    }
    if (p.goal) { var g = cell('Season goal', p.goal); g.style.gridColumn = '1 / -1'; grid.appendChild(g); }
    grid.hidden = !grid.children.length;

    var links = $('p-links'); links.textContent = '';
    if (p.resultsUrl) links.appendChild(chip('HYROX RESULTS ↗', p.resultsUrl));
    if (p.roxfitUrl) links.appendChild(chip('ROXFIT ↗', p.roxfitUrl));
    if (p.instagram) links.appendChild(chip('@' + p.instagram.toUpperCase() + ' ↗', 'https://instagram.com/' + encodeURIComponent(p.instagram)));
    if (p.otherUrl) links.appendChild(chip('PROFILE ↗', p.otherUrl));
    links.hidden = !links.children.length;
  }

  function load() {
    return fetch('/api/athletes/profile', { credentials: 'same-origin', headers: { accept: 'application/json' } })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (!d) return;
        state.profile = d.profile; state.hasPhoto = d.hasPhoto; state.photoVersion = d.photoVersion;
        renderSummary();
      })
      .catch(function () {});
  }

  /* ---------- editor ---------- */
  var dialog = $('profile-dialog'), form = $('profile-form');

  function fillForm() {
    var p = state.profile || {};
    FIELDS.forEach(function (f) {
      var input = form.elements[f]; if (!input) return;
      var v = p[f]; input.value = v == null ? '' : String(v);
      if (f === 'instagram' && v) input.value = '@' + v;
      input.removeAttribute('aria-invalid');
    });
    $('pd-error').hidden = true;
    paintAvatar($('pd-avatar'), 120);
    $('pd-photo-remove').hidden = !state.hasPhoto;
    closeCropper();
  }

  function openEditor() { fillForm(); if (dialog.showModal) dialog.showModal(); else dialog.setAttribute('open', ''); }
  function closeEditor() { closeCropper(); if (dialog.close) dialog.close(); else dialog.removeAttribute('open'); }

  $('profile-edit-btn').addEventListener('click', openEditor);
  $('pd-close').addEventListener('click', closeEditor);
  $('pd-cancel').addEventListener('click', closeEditor);

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var body = {};
    FIELDS.forEach(function (f) { var i = form.elements[f]; if (i) { body[f] = i.value.trim(); i.removeAttribute('aria-invalid'); } });
    $('pd-error').hidden = true;
    var btn = $('pd-save'); btn.disabled = true; btn.textContent = 'Saving…';
    fetch('/api/athletes/profile', { method: 'PUT', credentials: 'same-origin', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) })
      .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, d: d }; }); })
      .then(function (res) {
        if (!res.ok) {
          var code = (res.d && res.d.error) || '';
          var field = code.indexOf('invalid:') === 0 ? code.slice(8) : null;
          var msg = field && ERRORS[field] ? ERRORS[field] : code.indexOf('too_long') === 0 ? 'One of the texts is too long.' : 'Could not save. Try again.';
          if (field && form.elements[field]) { form.elements[field].setAttribute('aria-invalid', 'true'); form.elements[field].focus(); }
          $('pd-error').textContent = msg; $('pd-error').hidden = false;
          return;
        }
        state.profile = res.d.profile; renderSummary(); closeEditor();
      })
      .catch(function () { $('pd-error').textContent = 'Could not save. Check your connection.'; $('pd-error').hidden = false; })
      .finally(function () { btn.disabled = false; btn.textContent = 'Save profile'; });
  });

  $('pd-delete').addEventListener('click', function () {
    if (!confirm('Delete your profile and photo? This cannot be undone.')) return;
    fetch('/api/athletes/profile', { method: 'DELETE', credentials: 'same-origin' })
      .then(function (r) { if (!r.ok) throw 0; state.profile = null; state.hasPhoto = false; state.photoVersion = null; renderSummary(); closeEditor(); })
      .catch(function () { $('pd-error').textContent = 'Could not delete. Try again.'; $('pd-error').hidden = false; });
  });

  $('pd-photo-remove').addEventListener('click', function () {
    fetch('/api/athletes/photo', { method: 'DELETE', credentials: 'same-origin' })
      .then(function (r) { if (!r.ok) throw 0; state.hasPhoto = false; state.photoVersion = null; paintAvatar($('pd-avatar'), 120); renderSummary(); $('pd-photo-remove').hidden = true; })
      .catch(function () {});
  });

  /* ---------- cropper ---------- */
  var canvas = $('pd-canvas'), ctx = canvas.getContext('2d'), S = canvas.width;
  var crop = { img: null, base: 1, zoom: 1, x: 0, y: 0, drag: null };

  function scale() { return crop.base * crop.zoom; }
  function clamp() {
    var s = scale(), mx = Math.max(0, (crop.img.width * s - S) / 2), my = Math.max(0, (crop.img.height * s - S) / 2);
    crop.x = Math.min(mx, Math.max(-mx, crop.x)); crop.y = Math.min(my, Math.max(-my, crop.y));
  }
  function draw() {
    if (!crop.img) return;
    clamp();
    var s = scale(), w = crop.img.width * s, h = crop.img.height * s;
    ctx.fillStyle = '#050505'; ctx.fillRect(0, 0, S, S);
    ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(crop.img, S / 2 + crop.x - w / 2, S / 2 + crop.y - h / 2, w, h);
  }
  function setZoom(z, keepCenter) {
    crop.zoom = Math.min(4, Math.max(1, z)); $('pd-zoom').value = crop.zoom; draw();
  }
  function closeCropper() {
    $('pd-cropper').hidden = true; crop.img = null; $('pd-file').value = ''; $('pd-photo-err').hidden = true;
  }

  $('pd-file').addEventListener('change', function () {
    var file = this.files && this.files[0]; if (!file) return;
    $('pd-photo-err').hidden = true;
    if (file.size > 25 * 1024 * 1024) { showPhotoErr('That photo is too big (max 25 MB).'); return; }
    var url = URL.createObjectURL(file), img = new Image();
    img.onload = function () {
      URL.revokeObjectURL(url);
      crop.img = img; crop.base = Math.max(S / img.width, S / img.height); crop.x = 0; crop.y = 0;
      $('pd-cropper').hidden = false; setZoom(1); $('pd-stage').focus();
    };
    img.onerror = function () { URL.revokeObjectURL(url); showPhotoErr('This photo format can’t be opened here. Try a JPG or PNG.'); };
    img.src = url;
  });
  function showPhotoErr(msg) { $('pd-cropper').hidden = false; $('pd-photo-err').textContent = msg; $('pd-photo-err').hidden = false; }

  $('pd-zoom').addEventListener('input', function () { setZoom(parseFloat(this.value)); });

  var stage = $('pd-stage');
  function ratio() { return S / stage.getBoundingClientRect().width; }
  stage.addEventListener('pointerdown', function (e) {
    if (!crop.img) return; stage.setPointerCapture(e.pointerId);
    crop.drag = { px: e.clientX, py: e.clientY, x: crop.x, y: crop.y };
  });
  stage.addEventListener('pointermove', function (e) {
    if (!crop.drag) return; var r = ratio();
    crop.x = crop.drag.x + (e.clientX - crop.drag.px) * r; crop.y = crop.drag.y + (e.clientY - crop.drag.py) * r; draw();
  });
  ['pointerup', 'pointercancel'].forEach(function (t) { stage.addEventListener(t, function () { crop.drag = null; }); });
  stage.addEventListener('wheel', function (e) { if (!crop.img) return; e.preventDefault(); setZoom(crop.zoom * (e.deltaY < 0 ? 1.08 : 1 / 1.08)); }, { passive: false });
  stage.addEventListener('keydown', function (e) {
    if (!crop.img) return; var step = 20, k = e.key;
    if (k === 'ArrowLeft') crop.x += step; else if (k === 'ArrowRight') crop.x -= step;
    else if (k === 'ArrowUp') crop.y += step; else if (k === 'ArrowDown') crop.y -= step;
    else if (k === '+' || k === '=') { setZoom(crop.zoom * 1.1); e.preventDefault(); return; }
    else if (k === '-' || k === '_') { setZoom(crop.zoom / 1.1); e.preventDefault(); return; }
    else return;
    e.preventDefault(); draw();
  });

  $('pd-crop-cancel').addEventListener('click', closeCropper);
  $('pd-crop-save').addEventListener('click', function () {
    var btn = this; draw(); btn.disabled = true; btn.textContent = 'Uploading…';
    canvas.toBlob(function (blob) {
      if (!blob) { btn.disabled = false; btn.textContent = 'Use this crop'; showPhotoErr('Could not process the photo.'); return; }
      fetch('/api/athletes/photo', { method: 'PUT', credentials: 'same-origin', headers: { 'content-type': 'image/jpeg' }, body: blob })
        .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, d: d }; }); })
        .then(function (res) {
          if (!res.ok) throw new Error(res.d && res.d.error === 'too_large' ? 'The photo is too large.' : 'Upload failed. Try again.');
          state.hasPhoto = true; state.photoVersion = res.d.photoVersion;
          paintAvatar($('pd-avatar'), 120); renderSummary(); $('pd-photo-remove').hidden = false; closeCropper();
        })
        .catch(function (err) { showPhotoErr(err.message || 'Upload failed. Try again.'); })
        .finally(function () { btn.disabled = false; btn.textContent = 'Use this crop'; });
    }, 'image/jpeg', 0.88);
  });

  document.addEventListener('athlete:ready', function (e) {
    state.email = (e.detail && e.detail.email) || '';
    renderSummary();
    load();
  });
})();
