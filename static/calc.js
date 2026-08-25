async function post(url, data) {
  const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
  const j = await r.json();
  if (!r.ok) throw Error(j.error || 'Calculation error');
  return j;
}
function n(id) { return Number(document.getElementById(id).value); }
function f(x) { return Number(x).toLocaleString(undefined, { maximumFractionDigits: 3 }); }

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

async function calc038() {
  try {
    const j = await post('/api/calc/ais038', { u: n('u38'), v1: n('v138'), vp: n('vp38'), v2: n('v238') });
    document.getElementById('out038').innerHTML =
      `Minimum: ${f(j.minimum_ohm)} Ω\nCalculated insulation resistance: ${f(j.resistance_ohm)} Ω\n<b class="${j.pass ? 'pass' : 'fail'}">${j.pass ? 'PASS' : 'FAIL'}</b>`;
  } catch (e) { document.getElementById('out038').textContent = e.message; }
}

async function calc039() {
  try {
    const j = await post('/api/calc/ais039', { ct: n('ct39'), t: n('t39'), r: n('r39'), energy: n('e39'), distance: n('d39'), declared: n('m39') });
    document.getElementById('out039').innerHTML =
      `Corrected capacity at 27°C: ${f(j.corrected_capacity)}\nEnergy consumption: ${f(j.energy_consumption)} Wh/km\n4% upper limit: ${f(j.four_percent_limit)} Wh/km\n<b class="${j.within_limit ? 'pass' : 'fail'}">${j.within_limit ? 'WITHIN LIMIT' : 'ABOVE LIMIT'}</b>`;
  } catch (e) { document.getElementById('out039').textContent = e.message; }
}

async function calc048() {
  try {
    const j = await post('/api/calc/ais048', { capacity: n('cap48'), crate: n('crate48') });
    document.getElementById('out048').textContent =
      `Current drawn: ${f(j.current)} A\nDuration: ${f(j.hours)} h (${f(j.minutes)} min)`;
  } catch (e) { document.getElementById('out048').textContent = e.message; }
}

async function calc138() {
  try {
    const j = await post('/api/calc/ais138', { current: n('i138'), range: document.getElementById('range138').value, vdc: n('vdc138'), r: n('rg138'), rf: n('rf138') });
    document.getElementById('out138').textContent =
      `Duty cycle: ${f(j.duty_cycle)}\nMaximum current: ${f(j.available_current)} A\nDC body current Ih: ${f(j.body_current)} A\nDC earth leakage current Ig: ${f(j.earth_leakage)} A`;
  } catch (e) { document.getElementById('out138').textContent = e.message; }
}
