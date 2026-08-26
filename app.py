import os
import sys
import math
from flask import Flask, render_template, jsonify, request, abort

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.standards import STANDARDS

app = Flask(__name__)


# ============================================================
# STANDALONE CALCULATOR PAGES
# ============================================================

CALC_PAGES = {
    "ais-003": {
        "template": "calc_ais003.html",
        "code": "AIS-003",
        "title": "Starting Gradeability",
    },

    "ais-004": {
        "template": "calc_ais004.html",
        "code": "AIS-004",
        "title": "Electromagnetic Radiation Limits",
    },

    "ais-038": {
        "template": "calc_ais038.html",
        "code": "AIS-038",
        "title": "Traction Battery Insulation Resistance",
    },

    "ais-039": {
        "template": "calc_ais039.html",
        "code": "AIS-039",
        "title": "Energy Consumption & Capacity Correction",
    },

    "ais-040": {
        "template": "calc_ais040.html",
        "code": "AIS-040",
        "title": "Electric Range & Charging Time",
    },

    "ais-048": {
        "template": "calc_ais048.html",
        "code": "AIS-048",
        "title": "Battery Capacity & C Rate",
    },

    "ais-138": {
        "template": "calc_ais138.html",
        "code": "AIS-138",
        "title": "Charging / Body / Leakage Current",
    },
}


def _standard_for(code):
    """Return one standard by code."""
    return STANDARDS.get(code)


# ============================================================
# MAIN DASHBOARD
# ============================================================

@app.route("/")
def index():

    dashboard_standards = []

    for code, standard in STANDARDS.items():

        dashboard_standards.append({
            "code": standard["code"],
            "title": standard["title"],
            "ready": standard.get("calculator_available", False),
            "ev": standard.get("ev_related", False),
            "category": standard.get("category", ""),
            "vehicle_type": standard.get("vehicle_type", ""),
            "overview": standard.get("overview", ""),
            "formulas": [standard.get("category", "")] if standard.get("category") else [],
            "source": standard.get("source", ""),
        })

    return render_template(
        "index.html",
        standards=dashboard_standards,
        calc_pages=CALC_PAGES,
    )


# ============================================================
# STANDARDS API
# ============================================================

@app.route("/api/standards")
def api_standards():
    return jsonify(STANDARDS)


# ============================================================
# CALCULATOR PAGE
# ============================================================

@app.route("/calculator/<slug>")
def calculator_page(slug):

    meta = CALC_PAGES.get(slug)

    if not meta:
        abort(404)

    return render_template(
        meta["template"],
        standard=_standard_for(meta["code"]),
        slug=slug,
    )


# ============================================================
# STANDARDS OVERVIEW
# ============================================================

@app.route("/standards")
def standards():

    return render_template(
        "standards.html",
        standards=STANDARDS,
    )


# ============================================================
# STANDARD DETAIL
# ============================================================

@app.route("/standards/<code>")
def standard_detail(code):

    standard = _standard_for(code)

    if standard is None:
        return "Standard not found", 404

    return render_template(
        "standard.html",
        standard=standard,
    )


# ============================================================
# AIS-003
# STARTING GRADEABILITY
# ============================================================

@app.route("/api/calc/ais003", methods=["POST"])
def ais003():

    d = request.get_json()

    q, wt, wr = map(
        float,
        (d["q"], d["wt"], d["wr"]),
    )

    x = math.sin(math.radians(q)) * wt / wr

    if x > 1 or x < -1:
        return jsonify({
            "error": "Invalid input: (sin q × WT) / WR must be between -1 and 1."
        }), 400

    grade = 100 * math.tan(math.asin(x))

    to, tn, gro, grn, gvwo, gvwn, tro, trn, go = map(
        float,
        (
            d["to"],
            d["tn"],
            d["gro"],
            d["grn"],
            d["gvwo"],
            d["gvwn"],
            d["tro"],
            d["trn"],
            d["go"],
        ),
    )

    extra = (
        (tn / to)
        * (grn / gro)
        * (gvwo / gvwn)
        * (tro / trn)
        * go
    )

    return jsonify({
        "gradeability": grade,
        "extrapolated_gradeability": extra,
    })


# ============================================================
# AIS-004
# ELECTROMAGNETIC RADIATION
# ============================================================

@app.route("/api/calc/ais004", methods=["POST"])
def ais004():

    d = request.get_json() or {}

    try:
        req_keys = [
            "vehicle_broadband_10m_f",
            "vehicle_broadband_3m_f",
            "vehicle_narrowband_10m_f",
            "vehicle_narrowband_3m_f",
            "subsystem_broadband_30_75_f",
            "subsystem_broadband_75_400_f",
            "subsystem_narrowband_30_75_f",
            "subsystem_narrowband_75_400_f",
        ]
        for k in req_keys:
            if k not in d or float(d[k]) <= 0:
                return jsonify({
                    "error": f"Frequency '{k}' must be greater than zero."
                }), 400

        # --------------------------------------------------------
        # Vehicle - Broadband
        # --------------------------------------------------------

        vehicle_broadband_10m_f = float(d["vehicle_broadband_10m_f"])
        vehicle_broadband_3m_f = float(d["vehicle_broadband_3m_f"])

        vehicle_broadband_10m = (
            34 + 15.13 * math.log10(vehicle_broadband_10m_f / 75)
        )

        vehicle_broadband_3m = (
            44 + 15.13 * math.log10(vehicle_broadband_3m_f / 75)
        )

        # --------------------------------------------------------
        # Vehicle - Narrowband
        # --------------------------------------------------------

        vehicle_narrowband_10m_f = float(d["vehicle_narrowband_10m_f"])
        vehicle_narrowband_3m_f = float(d["vehicle_narrowband_3m_f"])

        vehicle_narrowband_10m = (
            24 + 15.13 * math.log10(vehicle_narrowband_10m_f / 75)
        )

        vehicle_narrowband_3m = (
            34 + 15.13 * math.log10(vehicle_narrowband_3m_f / 75)
        )

        # --------------------------------------------------------
        # Electronic Subsystem - Broadband
        # --------------------------------------------------------

        subsystem_broadband_30_75_f = float(
            d["subsystem_broadband_30_75_f"]
        )

        subsystem_broadband_75_400_f = float(
            d["subsystem_broadband_75_400_f"]
        )

        subsystem_broadband_30_75 = (
            64 - 25.13 * math.log10(
                subsystem_broadband_30_75_f / 30
            )
        )

        subsystem_broadband_75_400 = (
            54 + 15.13 * math.log10(
                subsystem_broadband_75_400_f / 75
            )
        )

        # --------------------------------------------------------
        # Electronic Subsystem - Narrowband
        # --------------------------------------------------------

        subsystem_narrowband_30_75_f = float(
            d["subsystem_narrowband_30_75_f"]
        )

        subsystem_narrowband_75_400_f = float(
            d["subsystem_narrowband_75_400_f"]
        )

        subsystem_narrowband_30_75 = (
            54 - 25.13 * math.log10(
                subsystem_narrowband_30_75_f / 30
            )
        )

        subsystem_narrowband_75_400 = (
            44 + 15.13 * math.log10(
                subsystem_narrowband_75_400_f / 75
            )
        )

        return jsonify({

            "vehicle_broadband_10m": vehicle_broadband_10m,

            "vehicle_broadband_3m": vehicle_broadband_3m,

            "vehicle_narrowband_10m": vehicle_narrowband_10m,

            "vehicle_narrowband_3m": vehicle_narrowband_3m,

            "subsystem_broadband_30_75": subsystem_broadband_30_75,

            "subsystem_broadband_75_400": subsystem_broadband_75_400,

            "subsystem_narrowband_30_75": subsystem_narrowband_30_75,

            "subsystem_narrowband_75_400": subsystem_narrowband_75_400,
        })

    except (ValueError, TypeError, KeyError) as e:
        return jsonify({"error": f"Invalid input parameter: {str(e)}"}), 400


# ============================================================
# AIS-038
# TRACTION BATTERY INSULATION RESISTANCE
# ============================================================

@app.route("/api/calc/ais038", methods=["POST"])
def ais038():

    d = request.get_json()

    u, v1, vp, v2 = map(
        float,
        (d["u"], d["v1"], d["vp"], d["v2"]),
    )

    minimum = u * 500

    ri = ((max(v1, vp) - v2) / v2) * 500

    return jsonify({
        "minimum_ohm": minimum,
        "resistance_ohm": ri,
        "pass": ri >= minimum,
    })


# ============================================================
# AIS-039
# ENERGY CONSUMPTION
# ============================================================

@app.route("/api/calc/ais039", methods=["POST"])
def ais039():

    d = request.get_json()

    ct, t, r = map(
        float,
        (d["ct"], d["t"], d["r"]),
    )

    corrected = ct + (
        ct * r * (27 - t) / 100
    )

    e = float(d["energy"])
    distance = float(d["distance"])

    consumption = (
        e / distance
        if distance
        else None
    )

    declared = d.get("declared")

    limit = (
        None
        if declared in (None, "")
        else float(declared) * 1.04
    )

    return jsonify({
        "corrected_capacity": corrected,
        "energy_consumption": consumption,
        "four_percent_limit": limit,
        "within_limit": (
            None
            if limit is None or consumption is None
            else consumption <= limit
        ),
    })


# ============================================================
# AIS-040
# ELECTRIC POWER TRAIN VEHICLES
# ============================================================

@app.route("/api/calc/ais040", methods=["POST"])
def ais040():

    d = request.get_json() or {}

    try:
        req_keys = [
            "battery_capacity",
            "mains_power",
            "covered_distance",
            "cycle_max_speed",
            "vehicle_max_speed",
        ]
        for k in req_keys:
            if k not in d:
                return jsonify({"error": f"Missing required parameter '{k}'."}), 400

        # --------------------------------------------------------
        # 1. Maximum Charging Time
        #
        # Excel:
        # =3*C7/C8
        #
        # Maximum Time = 3 × Battery Capacity / Mains Power
        # --------------------------------------------------------

        battery_capacity = float(
            d["battery_capacity"]
        )

        mains_power = float(
            d["mains_power"]
        )

        if mains_power <= 0:
            return jsonify({
                "error": "Mains power must be greater than zero."
            }), 400

        maximum_charging_time = (
            3 * battery_capacity / mains_power
        )

        charging_time_ok = (
            maximum_charging_time <= 12
        )

        if charging_time_ok:
            charging_status = "≤ 12 h"
        else:
            charging_status = (
                "Check standard exception condition"
            )

        # --------------------------------------------------------
        # 2. Electric Range
        #
        # Excel:
        # =ROUND(C16,0)
        #
        # Electric Range = rounded covered distance
        # --------------------------------------------------------

        covered_distance = float(
            d["covered_distance"]
        )

        electric_range = round(
            covered_distance
        )

        # --------------------------------------------------------
        # 3. L1 End-of-Test Speed Threshold
        #
        # 85% of maximum driving-cycle speed
        #
        # =0.85*C35
        #
        # 85% of maximum vehicle speed
        #
        # =0.85*C36
        #
        # L1 threshold:
        #
        # =MIN(C37,C38)
        # --------------------------------------------------------

        cycle_max_speed = float(
            d["cycle_max_speed"]
        )

        vehicle_max_speed = float(
            d["vehicle_max_speed"]
        )

        cycle_85 = (
            0.85 * cycle_max_speed
        )

        vehicle_85 = (
            0.85 * vehicle_max_speed
        )

        l1_threshold = min(
            cycle_85,
            vehicle_85,
        )

        return jsonify({

            "maximum_charging_time": maximum_charging_time,

            "charging_status": charging_status,

            "charging_time_ok": charging_time_ok,

            "electric_range": electric_range,

            "cycle_85": cycle_85,

            "vehicle_85": vehicle_85,

            "l1_threshold": l1_threshold,
        })

    except (ValueError, TypeError, KeyError) as e:
        return jsonify({"error": f"Invalid input parameter: {str(e)}"}), 400


# ============================================================
# AIS-048
# BATTERY CAPACITY & C RATE
# ============================================================

@app.route("/api/calc/ais048", methods=["POST"])
def ais048():

    d = request.get_json()

    cap, cr = map(
        float,
        (d["capacity"], d["crate"]),
    )

    return jsonify({
        "current": cap * cr,
        "hours": 1 / cr,
        "minutes": 60 / cr,
    })


# ============================================================
# AIS-138
# CHARGING / BODY / LEAKAGE CURRENT
# ============================================================

@app.route("/api/calc/ais138", methods=["POST"])
def ais138():

    d = request.get_json()

    current = float(
        d["current"]
    )

    low = (
        d.get("range", "low") == "low"
    )

    if low:
        duty = current / 0.6
        available = duty * 0.6

    else:
        duty = current / 2.5 + 64
        available = (
            duty - 64
        ) * 2.5

    vdc, r, rf = map(
        float,
        (
            d["vdc"],
            d["r"],
            d["rf"],
        ),
    )

    body = (
        vdc * (r + rf)
        / (r * rf)
    )

    leakage = (
        vdc / (r + 2 * rf)
    )

    return jsonify({

        "duty_cycle": duty,

        "available_current": available,

        "body_current": body,

        "earth_leakage": leakage,
    })


# ============================================================
# COMPARE
# ============================================================

@app.route("/compare")
def compare():

    return render_template(
        "compare.html",
        standards=STANDARDS,
    )


# ============================================================
# RUN LOCAL SERVER
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)