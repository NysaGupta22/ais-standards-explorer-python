from flask import Flask, render_template, jsonify, request, abort
import math
from data.standards import STANDARDS
app = Flask(__name__)

STANDARDS = [
 {"code":"AIS-003","title":"Automotive Vehicles — Starting Gradeability — Method of Measurement and Requirements","ready":True,"ev":False,"formulas":["Starting gradeability","Extrapolated gradeability"],"source":"Reference screenshot"},
 {"code":"AIS-004","title":"Electromagnetic Radiation / Compatibility Requirements for Automotive Vehicles","ready":True,"ev":False,"formulas":["Vehicle radiation limits","Electronic subsystem radiation limits"],"source":"AIS-004.xlsx"},
 {"code":"AIS-038","title":"Electric Power Train Vehicles — Construction and Functional Safety Requirements","ready":True,"ev":True,"formulas":["Traction battery insulation resistance"],"source":"AIS_038_Insulation_Resistance_Calculator.xlsx"},
 {"code":"AIS-039","title":"Electric Power Train Vehicles — Measurement of Electrical Energy Consumption","ready":True,"ev":True,"formulas":["Capacity correction to 27°C","Energy consumption","4% comparison"],"source":"AIS_039_Excel_Calculator.xlsx"},
 {"code":"AIS-040","title":"Electric Power Train Vehicles — Method of Measuring the Range","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-041","title":"Electric Power Train Vehicles — Measurement of Net Power and Maximum 30 Minute Power","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-048","title":"Battery Capacity and C Rate","ready":True,"ev":True,"formulas":["Battery current","Discharge duration"],"source":"AIS_48.xlsx"},
 {"code":"AIS-049","title":"AIS-049 — standard metadata","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-053","title":"AIS-053 — standard metadata","ready":False,"ev":False,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-071","title":"AIS-071 — standard metadata","ready":False,"ev":False,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-137","title":"AIS-137 — standard metadata","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-138","title":"Charging current, body current and earth leakage current","ready":True,"ev":True,"formulas":["AC charging current","DC body current","DC earth leakage current"],"source":"AIS-138_Combined.xlsx"},
 {"code":"AIS-156","title":"AIS-156 — standard metadata","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-189","title":"AIS-189 — standard metadata","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
 {"code":"AIS-190","title":"AIS-190 — standard metadata","ready":False,"ev":True,"formulas":[],"source":"Not supplied"},
]

# One entry per standalone calculator page: url slug -> template + short standing data.
CALC_PAGES = {
 "ais-003": {"template": "calc_ais003.html", "code": "AIS-003", "title": "Starting Gradeability"},
 "ais-038": {"template": "calc_ais038.html", "code": "AIS-038", "title": "Traction Battery Insulation Resistance"},
 "ais-039": {"template": "calc_ais039.html", "code": "AIS-039", "title": "Energy Consumption & Capacity Correction"},
 "ais-048": {"template": "calc_ais048.html", "code": "AIS-048", "title": "Battery Capacity & C Rate"},
 "ais-138": {"template": "calc_ais138.html", "code": "AIS-138", "title": "Charging / Body / Leakage Current"},
}


def _standard_for(code):
    return next((s for s in STANDARDS if s["code"] == code), None)


@app.route('/')
def index():
    return render_template('index.html', standards=STANDARDS, calc_pages=CALC_PAGES)


@app.route('/api/standards')
def standards():
    return jsonify(STANDARDS)


@app.route('/calculator/<slug>')
def calculator_page(slug):
    meta = CALC_PAGES.get(slug)
    if not meta:
        abort(404)
    return render_template(meta["template"], standard=_standard_for(meta["code"]), slug=slug)


@app.route('/api/calc/ais003', methods=['POST'])
def ais003():
    d = request.get_json()
    q, wt, wr = map(float, (d['q'], d['wt'], d['wr']))
    x = math.sin(math.radians(q)) * wt / wr
    if x > 1:
        return jsonify({'error': 'Invalid input: sine expression must be ≤ 1.'}), 400
    grade = 100 * math.tan(math.asin(x))
    to, tn, gro, grn, gvwo, gvwn, tro, trn, go = map(
        float, (d['to'], d['tn'], d['gro'], d['grn'], d['gvwo'], d['gvwn'], d['tro'], d['trn'], d['go'])
    )
    extra = (tn / to) * (grn / gro) * (gvwo / gvwn) * (tro / trn) * go
    return jsonify({'gradeability': grade, 'extrapolated_gradeability': extra})


@app.route('/api/calc/ais038', methods=['POST'])
def ais038():
    d = request.get_json()
    u, v1, vp, v2 = map(float, (d['u'], d['v1'], d['vp'], d['v2']))
    minimum = u * 500
    ri = ((max(v1, vp) - v2) / v2) * 500
    return jsonify({'minimum_ohm': minimum, 'resistance_ohm': ri, 'pass': ri >= minimum})


@app.route('/api/calc/ais039', methods=['POST'])
def ais039():
    d = request.get_json()
    ct, t, r = map(float, (d['ct'], d['t'], d['r']))
    corrected = ct + (ct * r * (27 - t) / 100)
    e, distance = float(d['energy']), float(d['distance'])
    consumption = e / distance if distance else None
    declared = d.get('declared')
    limit = None if declared in (None, '') else float(declared) * 1.04
    return jsonify({
        'corrected_capacity': corrected,
        'energy_consumption': consumption,
        'four_percent_limit': limit,
        'within_limit': None if limit is None or consumption is None else consumption <= limit,
    })


@app.route('/api/calc/ais048', methods=['POST'])
def ais048():
    d = request.get_json()
    cap, cr = map(float, (d['capacity'], d['crate']))
    return jsonify({'current': cap * cr, 'hours': 1 / cr, 'minutes': 60 / cr})


@app.route('/api/calc/ais138', methods=['POST'])
def ais138():
    d = request.get_json()
    current = float(d['current'])
    low = d.get('range', 'low') == 'low'
    duty = current / 0.6 if low else current / 2.5 + 64
    available = duty * 0.6 if low else (duty - 64) * 2.5
    vdc, r, rf = map(float, (d['vdc'], d['r'], d['rf']))
    body = vdc * (r + rf) / (r * rf)
    leakage = vdc / (r + 2 * rf)
    return jsonify({
        'duty_cycle': duty,
        'available_current': available,
        'body_current': body,
        'earth_leakage': leakage,
    })

@app.route("/compare")
def compare():
    return render_template("compare.html")


if __name__ == '__main__':
    app.run(debug=True)

@app.route("/standards")
def standards():
    return render_template(
        "standards.html",
        standards=STANDARDS
    )


@app.route("/standards/<code>")
def standard_detail(code):
    standard = STANDARDS.get(code)

    if standard is None:
        return "Standard not found", 404

    return render_template(
        "standard.html",
        standard=standard
    )


@app.route("/compare")
def compare():
    return render_template(
        "compare.html",
        standards=STANDARDS
    )