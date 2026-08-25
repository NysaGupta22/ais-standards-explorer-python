# data/standards.py
#
# Standards overview / comparison data ONLY.
# Calculator formulas are intentionally kept in their
# respective calculator HTML / JS files.

STANDARDS = {

    "AIS-003": {
        "code": "AIS-003",
        "title": "Starting Gradeability",

        "overview": (
            "Covers the method of measurement and requirements for "
            "starting gradeability of a vehicle."
        ),

        "scope": (
            "Provides a method for assessing the ability of a vehicle "
            "to start on a specified gradient and includes the "
            "calculation used for gradeability assessment."
        ),

        "category": "Vehicle Performance",

        "vehicle_type": "Automotive vehicles",

        "purpose": (
            "To determine and assess the starting gradeability of "
            "a vehicle under the specified test conditions."
        ),

        "ev_related": False,

        # This only indicates whether the project has a calculator.
        # The actual formula remains on the calculator page.
        "formula_available": True,

        "calculator_available": True,

        "revision_history": [
            "AIS-003"
        ],

        "amendments": [],

        "related_standards": [],

        "source": "ARAI AIS publication"
    },


    "AIS-038": {
        "code": "AIS-038",

        "title": (
            "Electric Power Train Vehicles — "
            "Construction and Functional Safety"
        ),

        "overview": (
            "Covers requirements relating to the construction and "
            "functional safety of electric power train vehicles."
        ),

        "scope": (
            "Addresses construction and functional safety requirements "
            "associated with electric power train vehicles, including "
            "relevant electrical and traction-battery safety provisions."
        ),

        "category": "EV / Functional Safety",

        "vehicle_type": (
            "Electric power train / battery operated vehicles"
        ),

        "purpose": (
            "To establish requirements intended to address the "
            "construction and functional safety of electric power "
            "train vehicles."
        ),

        "ev_related": True,

        "formula_available": True,

        "calculator_available": True,

        "revision_history": [
            "AIS-038",
            "AIS-038 (Rev.1)",
            "AIS-038 (Rev.2)"
        ],

        "amendments": [
            "Amendments associated with the applicable revision"
        ],

        "related_standards": [
            "AIS-039",
            "AIS-040",
            "AIS-041"
        ],

        "source": "ARAI AIS publication"
    },


    "AIS-039": {
        "code": "AIS-039",

        "title": (
            "Electric Power Train Vehicles — "
            "Measurement of Electrical Energy Consumption"
        ),

        "overview": (
            "Covers the measurement of electrical energy consumption "
            "of electric power train vehicles."
        ),

        "scope": (
            "Provides the measurement methodology for determining "
            "electrical energy consumption under the conditions "
            "specified by the standard."
        ),

        "category": "EV / Energy Consumption",

        "vehicle_type": (
            "Electric power train / battery operated vehicles"
        ),

        "purpose": (
            "To provide a standardized method for determining the "
            "electrical energy consumption of electric power train "
            "vehicles."
        ),

        "ev_related": True,

        "formula_available": True,

        "calculator_available": True,

        "revision_history": [
            "AIS-039",
            "AIS-039 (Rev.1)"
        ],

        "amendments": [
            "Amendments / corrigenda associated with the applicable revision"
        ],

        "related_standards": [
            "AIS-038",
            "AIS-040",
            "AIS-041"
        ],

        "source": "ARAI AIS publication"
    }

}