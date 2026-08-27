async function post(url, data) {
  const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
  const j = await r.json();
  if (!r.ok) throw Error(j.error || 'Calculation error');
  return j;
}
function n(id) {
  const el = document.getElementById(id);
  return el ? Number(el.value) : 0;
}
function f(x) {
  if (x === null || x === undefined || isNaN(x)) return '—';
  return Number(x).toLocaleString(undefined, { minimumFractionDigits: 3, maximumFractionDigits: 3 });
}

// AIS-003
async function calc003() {
  try {
    const j = await post('/api/calc/ais003', {
      q: n('q'), wt: n('wt'), wr: n('wr'), go: n('go'), to: n('to'), tn: n('tn'),
      gro: n('gro'), grn: n('grn'), gvwo: n('gvwo'), gvwn: n('gvwn'), tro: n('tro'), trn: n('trn')
    });
    document.getElementById('out003').textContent =
      `Starting gradeability: ${f(j.gradeability)} %\nExtrapolated gradeability: ${f(j.extrapolated_gradeability)} %`;
  } catch (e) { document.getElementById('out003').textContent = e.message; }
}

// AIS-038
async function calc038() {
  try {
    const j = await post('/api/calc/ais038', { u: n('u38'), v1: n('v138'), vp: n('vp38'), v2: n('v238') });
    document.getElementById('out038').innerHTML =
      `Minimum: ${f(j.minimum_ohm)} Ω\nCalculated insulation resistance: ${f(j.resistance_ohm)} Ω\n<b class="${j.pass ? 'pass' : 'fail'}">${j.pass ? 'PASS' : 'FAIL'}</b>`;
  } catch (e) { document.getElementById('out038').textContent = e.message; }
}

// AIS-039
async function calc039() {
  try {
    const j = await post('/api/calc/ais039', { ct: n('ct39'), t: n('t39'), r: n('r39'), energy: n('e39'), distance: n('d39'), declared: n('m39') });
    document.getElementById('out039').innerHTML =
      `Corrected capacity at 27°C: ${f(j.corrected_capacity)}\nEnergy consumption: ${f(j.energy_consumption)} Wh/km\n4% upper limit: ${f(j.four_percent_limit)} Wh/km\n<b class="${j.within_limit ? 'pass' : 'fail'}">${j.within_limit ? 'WITHIN LIMIT' : 'ABOVE LIMIT'}</b>`;
  } catch (e) { document.getElementById('out039').textContent = e.message; }
}

// AIS-048
async function calc048() {
  try {
    const j = await post('/api/calc/ais048', { capacity: n('cap48'), crate: n('crate48') });
    document.getElementById('out048').textContent =
      `Current drawn: ${f(j.current)} A\nDuration: ${f(j.hours)} h (${f(j.minutes)} min)`;
  } catch (e) { document.getElementById('out048').textContent = e.message; }
}

// AIS-004
async function calc004() {
  try {
    const j = await post('/api/calc/ais004', {
      vehicle_broadband_10m_f: n('vbb10'),
      vehicle_broadband_3m_f: n('vbb3'),
      vehicle_narrowband_10m_f: n('vnb10'),
      vehicle_narrowband_3m_f: n('vnb3'),
      subsystem_broadband_30_75_f: n('sbb3075'),
      subsystem_broadband_75_400_f: n('sbb75400'),
      subsystem_narrowband_30_75_f: n('snb3075'),
      subsystem_narrowband_75_400_f: n('snb75400')
    });

    document.getElementById('out004').textContent =
      `Vehicle Broadband (10 m): ${f(j.vehicle_broadband_10m)} dBµV/m\n` +
      `Vehicle Broadband (3 m): ${f(j.vehicle_broadband_3m)} dBµV/m\n` +
      `Vehicle Narrowband (10 m): ${f(j.vehicle_narrowband_10m)} dBµV/m\n` +
      `Vehicle Narrowband (3 m): ${f(j.vehicle_narrowband_3m)} dBµV/m\n\n` +
      `Subsystem Broadband (30–75 MHz): ${f(j.subsystem_broadband_30_75)} dBµV/m\n` +
      `Subsystem Broadband (75–400 MHz): ${f(j.subsystem_broadband_75_400)} dBµV/m\n` +
      `Subsystem Narrowband (30–75 MHz): ${f(j.subsystem_narrowband_30_75)} dBµV/m\n` +
      `Subsystem Narrowband (75–400 MHz): ${f(j.subsystem_narrowband_75_400)} dBµV/m`;
  } catch (e) {
    document.getElementById('out004').textContent = e.message;
  }
}

// AIS-040
async function calc040() {
  try {
    const j = await post('/api/calc/ais040', {
      battery_capacity: n('cap40'),
      mains_power: n('power40'),
      covered_distance: n('distance40'),
      cycle_max_speed: n('cycle40'),
      vehicle_max_speed: n('vehicle40')
    });

    document.getElementById('out040').innerHTML =
      `Maximum charging time: ${f(j.maximum_charging_time)} h (${j.charging_status}) ` +
      `<b class="${j.charging_time_ok ? 'pass' : 'fail'}">${j.charging_time_ok ? 'PASS (≤ 12 h)' : 'REVIEW'}</b>\n` +
      `Electric range: ${f(j.electric_range)} km\n` +
      `85% Cycle max speed: ${f(j.cycle_85)} km/h\n` +
      `85% Vehicle max speed: ${f(j.vehicle_85)} km/h\n` +
      `L1 End-of-test speed threshold: ${f(j.l1_threshold)} km/h`;
  } catch (e) {
    document.getElementById('out040').textContent = e.message;
  }
}

// =========================================================
// AIS-138 DEDICATED SEPARATED CALCULATIONS
// =========================================================

// Card 1: AC Charging 6A–51A Range
function calc138_ac_low() {
  const current = n('ac_low_i');
  if (current <= 0) {
    if (document.getElementById('out_ac_low_duty')) document.getElementById('out_ac_low_duty').textContent = '—';
    if (document.getElementById('out_ac_low_current')) document.getElementById('out_ac_low_current').textContent = '—';
    return;
  }
  const duty = current / 0.6;
  const maxCurrent = duty * 0.6;

  const dutyEl = document.getElementById('out_ac_low_duty');
  const currEl = document.getElementById('out_ac_low_current');
  if (dutyEl) dutyEl.textContent = `${f(duty)} %`;
  if (currEl) currEl.textContent = `${f(maxCurrent)} A`;
}

// Card 2: AC Charging 51A–80A Range
function calc138_ac_high() {
  const current = n('ac_high_i');
  if (current <= 0) {
    if (document.getElementById('out_ac_high_duty')) document.getElementById('out_ac_high_duty').textContent = '—';
    if (document.getElementById('out_ac_high_current')) document.getElementById('out_ac_high_current').textContent = '—';
    return;
  }
  const duty = (current / 2.5) + 64;
  const maxCurrent = (duty - 64) * 2.5;

  const dutyEl = document.getElementById('out_ac_high_duty');
  const currEl = document.getElementById('out_ac_high_current');
  if (dutyEl) dutyEl.textContent = `${f(duty)} %`;
  if (currEl) currEl.textContent = `${f(maxCurrent)} A`;
}

// Card 3: DC Charging Body & Earth Leakage Current
function calc138_dc() {
  const vdc = n('dc_vdc');
  const r = n('dc_r');
  const rf = n('dc_rf');

  const bodyEl = document.getElementById('out_dc_body');
  const leakEl = document.getElementById('out_dc_leakage');

  if (r <= 0 || rf <= 0) {
    if (bodyEl) bodyEl.textContent = '—';
    if (leakEl) leakEl.textContent = '—';
    return;
  }

  const body = vdc * (r + rf) / (r * rf);
  const leakage = vdc / (r + 2 * rf);

  if (bodyEl) bodyEl.textContent = `${f(body)} A`;
  if (leakEl) leakEl.textContent = `${f(leakage)} A`;
}

// Unified fallback for AIS-138
async function calc138() {
  calc138_ac_low();
  calc138_ac_high();
  calc138_dc();
}
