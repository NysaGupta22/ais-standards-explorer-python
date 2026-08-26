# data/standards.py
#
# Standards overview / comparison data.
# Source basis: Official ARAI published AIS standards (AIS-003 through AIS-190)
# and CMVR technical reference material.
#
# Calculator formulas remain in their respective calculator
# HTML / JS / API implementations.

STANDARDS = {

    "AIS-003": {
        "code": "AIS-003",
        "title": "Automotive Vehicles — Starting Gradeability — Method of Measurement and Requirements",
        "overview": (
            "Specifies the test methodology, physical requirements, and mathematical formulas "
            "for measuring and verifying the starting gradeability capability of automotive vehicles "
            "on specified inclined road gradients."
        ),
        "scope": (
            "Applies to automotive vehicles of categories M and N. Defines procedures for "
            "evaluating the capability of a vehicle to start from rest on an inclined surface "
            "under specified gross vehicle weight (GVW) conditions, as well as the extrapolation "
            "of test results to variant configurations."
        ),
        "category": "Vehicle Dynamics / Powertrain Performance",
        "vehicle_type": "M and N Category Motor Vehicles",
        "purpose": (
            "To evaluate whether a loaded vehicle has sufficient powertrain torque, traction, "
            "and gear multiplication to reliably start from a complete standstill on steep road gradients."
        ),
        "applicability": (
            "Mandatory performance evaluation under Central Motor Vehicle Rules (CMVR) for type approval "
            "and homologation of commercial and passenger vehicles."
        ),
        "ev_related": False,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "Vehicle loaded to maximum gross vehicle weight (GVW / WR)",
            "Measured starting gradeability on test gradient or chassis dynamometer",
            "Extrapolation formula to adjust for changes in test weight, engine/motor torque, gear ratios, and tyre rolling radius",
            "Verification that the calculated slope sine ratio (sin q * WT / WR) does not exceed unity (-1 to 1)",
        ],
        "test_focus": [
            "Starting on gradient from standstill",
            "Vehicle axle loading and adhesion verification",
            "Engine / motor peak starting torque assessment",
            "Extrapolated gradeability calculations for vehicle variants",
        ],
        "revision_history": [
            "AIS-003/1999: Automotive Vehicles - Starting Gradeability",
            "Amendment No. 1 (August 2000)",
            "Amendment No. 2 (November 2001)",
            "Amendment No. 3 (May 2002)",
        ],
        "amendments": [
            "Amendment 3 (05/2002): Clarified tyre rolling radius measurement and dynamometer extrapolation procedures.",
        ],
        "related_standards": [
            "AIS-040",
            "AIS-041",
            "AIS-053",
        ],
        "comparative_study": {
            "primary_role": "Vehicle low-speed tractive performance & gradeability",
            "main_output": "Starting Gradeability percentage (%) and Extrapolated Gradeability (%)",
            "engineering_domain": "Powertrain Dynamics & Tractive Effort",
            "compliance_criteria": "Must start cleanly on the specified regulatory gradient without excessive wheel slip or stall",
            "test_methodology": "Track slope test or dyno torque simulation with mathematical extrapolation for variant parameters",
            "best_compared_with": [
                "AIS-041",
                "AIS-040",
                "AIS-053",
            ],
            "comparison_note": (
                "AIS-003 measures low-speed starting tractive ability under incline loads, whereas AIS-041 "
                "evaluates overall electric powertrain continuous and net power, and AIS-040 evaluates "
                "driving range efficiency. Together, AIS-003 and AIS-041 ensure the vehicle possesses both "
                "starting grade capability and cruising power."
            ),
        },
        "source": "ARAI AIS-003/1999 Publication",
    },

    "AIS-004": {
        "code": "AIS-004",
        "title": "Automotive Vehicles — Requirements for Electromagnetic Compatibility (EMC)",
        "overview": (
            "Defines regulatory limits and testing protocols for electromagnetic immunity and radio "
            "frequency radiation emissions from automotive vehicles and their electronic sub-assemblies (ESAs)."
        ),
        "scope": (
            "Covers motor vehicles of categories M, N, L and their electrical/electronic sub-assemblies. "
            "Regulates broadband and narrowband radiated electromagnetic disturbances, radiated immunity "
            "to external electromagnetic fields, and electrical transient conduction."
        ),
        "category": "Automotive Electronics / EMC",
        "vehicle_type": "Motor Vehicles and Electrical/Electronic Sub-Assemblies (ESAs)",
        "purpose": (
            "To prevent vehicle electronic systems (ECUs, BMS, motor controllers) from emitting radio interference "
            "that disrupts communication systems, and to guarantee that safety-critical vehicle functions remain immune "
            "to external electromagnetic radiation."
        ),
        "applicability": (
            "Mandatory compliance requirement under CMVR for all modern ICE, hybrid, and electric vehicles "
            "fitted with electronic control units and power electronics."
        ),
        "ev_related": True,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "Broadband radiated emissions limit from vehicle (10 m and 3 m antenna distance)",
            "Narrowband radiated emissions limit from vehicle (10 m and 3 m antenna distance)",
            "Broadband and narrowband emissions limits for electronic sub-assemblies (30-75 MHz and 75-400 MHz)",
            "Immunity testing of vehicles against electromagnetic fields (20 MHz to 2 GHz at 30 V/m)",
            "Immunity of ESAs against conducted electrical transients along supply lines",
        ],
        "test_focus": [
            "Anechoic chamber RF emission measurement",
            "Logarithmic frequency limit curve calculation",
            "Subsystem immunity testing (Bulk Current Injection / Stripline / Anechoic Chamber)",
            "High-voltage inverter and DC-DC converter EMC validation",
        ],
        "revision_history": [
            "AIS-004 (Part 1): Electromagnetic Radiation from Vehicles",
            "AIS-004 (Part 2): Electromagnetic Immunity of Vehicles",
            "AIS-004 (Part 3): Electromagnetic Compatibility of Electronic Sub-Assemblies",
            "AIS-004 (Part 3 Rev. 1): Updated ESA EMC Requirements",
        ],
        "amendments": [
            "Harmonized with UNECE Regulation 10 (UN R10) for high-voltage electric powertrain testing.",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-156",
            "AIS-189",
        ],
        "comparative_study": {
            "primary_role": "Electromagnetic emissions and RF interference immunity",
            "main_output": "Compliance with radiated emission limits (dBµV/m) and immunity field strength (V/m)",
            "engineering_domain": "Automotive Electronics & High-Voltage EMC",
            "compliance_criteria": "Emissions must remain below the frequency-dependent logarithmic threshold; zero degradation of safety functions during 30 V/m RF exposure",
            "test_methodology": "Semi-anechoic RF chamber testing with biconical and log-periodic antennas at 3 m / 10 m distances",
            "best_compared_with": [
                "AIS-038",
                "AIS-156",
                "AIS-189",
            ],
            "comparison_note": (
                "AIS-004 evaluates electromagnetic interference (EMI/EMC) across high-voltage switching inverters "
                "and ECUs, providing the electrical compatibility foundation for the high-voltage safety standards "
                "like AIS-038 (M/N vehicles) and AIS-156 (L category). While AIS-189 protects against cyber threats, "
                "AIS-004 protects against physical RF electromagnetic disturbance."
            ),
        },
        "source": "ARAI AIS-004 / UNECE R10 Reference",
    },

    "AIS-038": {
        "code": "AIS-038",
        "title": "Electric Power Train Vehicles — Requirements for Construction and Functional Safety",
        "overview": (
            "Comprehensive vehicle-level electrical safety and Rechargeable Electrical Energy Storage System (REESS) "
            "standard for four-wheeled and commercial electric powertrain vehicles (Categories M and N)."
        ),
        "scope": (
            "Applies to electric powertrain vehicles of categories M and N (passenger cars, buses, and commercial trucks). "
            "Specifies requirements for protection against electrical shock (direct/indirect contact), high-voltage isolation, "
            "functional safety, REESS safety, thermal runaway propagation prevention, and water ingress protection."
        ),
        "category": "EV Electrical & Functional Safety",
        "vehicle_type": "M and N Category Electric Power Train Vehicles",
        "purpose": (
            "To guarantee total passenger and service technician safety against high-voltage electrical hazards, "
            "prevent traction battery fires/thermal runaway, and enforce fail-safe vehicle powertrain operation."
        ),
        "applicability": (
            "Core mandatory type-approval standard for all 4W passenger electric cars, commercial electric buses, "
            "and electric trucks under CMVR."
        ),
        "ev_related": True,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "Isolation resistance >= 500 Ω/V for DC high-voltage buses, >= 100 Ω/V for AC buses",
            "IPXXD protection against direct contact with live parts inside passenger compartment, IPXXB in other areas",
            "REESS thermal propagation test: zero external fire or explosion for at least 5 minutes after cell thermal runaway",
            "Battery Management System (BMS) over-charge, over-discharge, over-temperature, and over-current protection",
            "Audible / visual warning signal to driver upon isolation degradation or REESS thermal anomaly",
            "Post-crash electrical safety: voltage < 60 V DC within 60 seconds, or total energy < 0.2 Joules",
        ],
        "test_focus": [
            "Voltmeter-based high-voltage insulation resistance measurement (Ri = [(V1 - V2)/V2] * R0)",
            "Thermal runaway initiation via heating/nail penetration with gas management venting verification",
            "Water wash and flooding immersion testing",
            "Mechanical vibration, impact, and shock testing on REESS",
        ],
        "revision_history": [
            "AIS-038: 2003 (Initial publication for Battery Operated Vehicles)",
            "AIS-038 (Rev. 1): 2015 (Harmonization with UN GTR 20)",
            "AIS-038 (Rev. 2): 2020 (Specific requirements for Construction and Functional Safety)",
            "AIS-038 (Rev. 2) Amendment 1 (2021): Battery management and BMS data recording",
            "AIS-038 (Rev. 2) Amendment 2 (2022): Mandated thermal propagation testing and active safety buzzer",
            "AIS-038 (Rev. 2) Amendment 3 (2023): Enhanced cell-level testing and safety interlocks",
            "AIS-038 (Rev. 2) Amendment 4 (08/2024): Updated charger interlock and high-temperature thermal protection",
        ],
        "amendments": [
            "Amendment 1 (2021): Introduced BMS functional safety and micro-controller requirements.",
            "Amendment 2 (2022): Made 5-minute thermal propagation warning mandatory before fire/smoke enters cabin.",
            "Amendment 3 (2023): Tightened spacing between cells and mandated multi-point temperature sensing.",
            "Amendment 4 (08/2024): Updated fast charging thermal cutoffs and vehicle drive-away interlocks.",
        ],
        "related_standards": [
            "AIS-039",
            "AIS-040",
            "AIS-041",
            "AIS-048",
            "AIS-049",
            "AIS-138",
            "AIS-156",
        ],
        "comparative_study": {
            "primary_role": "Vehicle-level EV electrical & functional safety for 4-wheelers and commercial vehicles (M & N)",
            "main_output": "Type approval certification for high-voltage isolation resistance and REESS thermal safety",
            "engineering_domain": "High-Voltage Electrical Safety & Battery Fire Prevention",
            "compliance_criteria": "Insulation Resistance >= 500 Ω/V; 5-minute passenger escape time during thermal runaway without cabin breach",
            "test_methodology": "Three-voltmeter isolation test method, thermal runaway trigger test, REESS vibration & shock profiles",
            "best_compared_with": [
                "AIS-156",
                "AIS-048",
                "AIS-138",
                "AIS-039",
            ],
            "comparison_note": (
                "AIS-038 is the foundational safety standard for 4W electric cars and commercial buses (Categories M/N), "
                "whereas AIS-156 specifically serves the 2W and 3W market (Category L). AIS-048 focuses exclusively on "
                "component-level battery testing, whereas AIS-038 covers complete vehicle high-voltage isolation, crash safety, "
                "and charging safety interlocks."
            ),
        },
        "source": "ARAI AIS-038 (Rev. 2) including Amendments 1-4 (08/2024)",
    },

    "AIS-039": {
        "code": "AIS-039",
        "title": "Electric Power Train Vehicles — Measurement of Electrical Energy Consumption",
        "overview": (
            "Standardizes the laboratory dynamometer testing procedure and temperature correction calculations "
            "for measuring the electrical energy consumption (Wh/km) of electric vehicles."
        ),
        "scope": (
            "Applies to electric powertrain vehicles of categories M, N, and L. Defines the testing cycle (IDC/WLTC), "
            "measurement of energy taken from the electrical mains during recharge, battery state of charge (SoC) conditioning, "
            "and the 27°C ambient temperature capacity correction formula."
        ),
        "category": "EV Energy Efficiency",
        "vehicle_type": "M, N, and L Category Electric Vehicles",
        "purpose": (
            "To provide a standardized, repeatable, and verified energy consumption value (Wh/km) for EV label compliance, "
            "consumer information, and regulatory energy efficiency standards."
        ),
        "applicability": (
            "Mandatory certification parameter under CMVR; used by ARAI and manufacturers for statutory energy consumption reporting."
        ),
        "ev_related": True,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "Standardized chassis dynamometer test over applicable driving cycle (Modified Indian Driving Cycle / WLTC)",
            "Mains electrical energy measurement using Class 0.5 Wh-meter during post-test recharging",
            "Capacity temperature correction to reference 27°C using formula: C_corrected = C_t * [1 + r * (27 - T) / 100]",
            "Compliance verification: Tested energy consumption must not exceed 4% of the manufacturer-declared value",
            "Pre-test battery conditioning: Minimum 7-day stabilization and defined charge/discharge stabilization cycles",
        ],
        "test_focus": [
            "Wh/km energy consumption calculation from dynamometer distance and AC mains energy",
            "Battery capacity correction factor at varying ambient test temperatures",
            "Recharge energy measurement from AC supply until charging cutoff",
        ],
        "revision_history": [
            "AIS-039: 2003 (Initial standard for Battery Operated Vehicles)",
            "AIS-039 (Rev. 1): 2015 (Measurement of Electrical Energy Consumption)",
            "AIS-039 (Rev. 1) Amendment 1 (2018): Clarification of charging cutoff",
            "AIS-039 (Rev. 1) Amendment 2 (2021): Dynamometer coast-down coefficients",
            "AIS-039 (Rev. 1) Amendment 3 (09/2026 notification): Harmonization with WLTP/WLTC test cycles",
        ],
        "amendments": [
            "Amendment 1: Refined end-of-charge criteria and power meter accuracy specifications.",
            "Amendment 2: Standardized dynamometer parasitic loss compensation.",
            "Amendment 3 (09/2026): Integration of WLTC drive cycles for high-speed M/N category vehicles.",
        ],
        "related_standards": [
            "AIS-040",
            "AIS-041",
            "AIS-038",
            "AIS-137",
        ],
        "comparative_study": {
            "primary_role": "Measurement of EV energy consumption efficiency (Wh/km)",
            "main_output": "Electrical Energy Consumption (Wh/km) & 27°C Corrected Battery Capacity (Ah/Wh)",
            "engineering_domain": "EV Powertrain Efficiency & Energy Metrology",
            "compliance_criteria": "Measured energy consumption must be within 4% of declared value",
            "test_methodology": "Chassis dynamometer driving cycle followed by full recharge energy integration from the AC grid",
            "best_compared_with": [
                "AIS-040",
                "AIS-041",
                "AIS-038",
                "AIS-137",
            ],
            "comparison_note": (
                "AIS-039 measures how much electrical energy a vehicle uses from the grid per kilometer (Wh/km), "
                "whereas AIS-040 measures how far the vehicle can travel on a single full charge (km). Together with "
                "AIS-041 (power capability), these three standards form the complete performance triad of EV homologation."
            ),
        },
        "source": "ARAI AIS-039 (Rev. 1) including Amendments up to 09/2026",
    },

    "AIS-040": {
        "code": "AIS-040",
        "title": "Electric Power Train Vehicles — Method of Measuring the Range",
        "overview": (
            "Specifies the test conditions, vehicle preparation, driving cycle procedures, and end-of-test "
            "criteria for measuring the single-charge driving range (km) of electric vehicles."
        ),
        "scope": (
            "Applies to pure electric vehicles of categories M, N, and L. Defines the continuous drive-cycle "
            "execution until the vehicle can no longer maintain the required cycle speed (L1 speed threshold), "
            "and specifies the 12-hour maximum charging time verification."
        ),
        "category": "EV Driving Range",
        "vehicle_type": "Pure Electric Power Train Vehicles (M, N, L Categories)",
        "purpose": (
            "To provide a standardized and certified single-charge range figure (km) for electric vehicles, "
            "ensuring consistency between manufacturer claims and certified real-world performance."
        ),
        "applicability": (
            "Mandatory type-approval requirement under CMVR for all pure battery-electric vehicles in India."
        ),
        "ev_related": True,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "Range rounded to the nearest integer kilometer: Range = ROUND(Distance, 0)",
            "End-of-test L1 speed criterion: Vehicle cannot maintain 85% of maximum cycle speed or 85% of vehicle max speed",
            "Maximum charging time rule: T_max = 3 * Battery_Capacity / Mains_Power <= 12 hours",
            "Conditioning: Ambient temperature between 20°C and 30°C during test",
            "Constant speed range measurement option for special vehicle categories",
        ],
        "test_focus": [
            "Continuous dynamometer driving cycle testing to battery exhaustion",
            "L1 speed threshold calculation (MIN(0.85 * Cycle_Max, 0.85 * Vehicle_Max))",
            "Recharging time evaluation against 12-hour statutory threshold",
        ],
        "revision_history": [
            "AIS-040: 2003 (Initial Range measurement standard)",
            "AIS-040 (Rev. 1): 2015 (Harmonization with UN ECE R101)",
            "AIS-040 (Rev. 1) Amendment 1 (2018): Specific criteria for 3-wheelers",
            "AIS-040 (Rev. 1) Amendment 2 (2021): Fast-charging range verification",
            "AIS-040 (Rev. 1) Amendment 3 (04/2026 notification): Revised driving cycle tolerances and Intelligent Transport System (ITS) integration",
        ],
        "amendments": [
            "Amendment 2: Introduced standardized fast-recharge range assessment.",
            "Amendment 3 (04/2026): Updated drive cycle termination criteria and ITS compliance mapping.",
        ],
        "related_standards": [
            "AIS-039",
            "AIS-041",
            "AIS-038",
            "AIS-003",
        ],
        "comparative_study": {
            "primary_role": "Certified EV single-charge driving range measurement",
            "main_output": "Certified Electric Driving Range (km) & Charging Time Feasibility",
            "engineering_domain": "EV Range & Energy Management",
            "compliance_criteria": "Must complete range test until L1 cutoff; charging time must satisfy 12h threshold or exception clauses",
            "test_methodology": "Chassis dyno repetitive cycle driving from 100% SoC until inability to maintain 85% cycle speed",
            "best_compared_with": [
                "AIS-039",
                "AIS-041",
                "AIS-003",
                "AIS-049",
            ],
            "comparison_note": (
                "AIS-040 focuses on range (distance travelled until battery depletion), whereas AIS-039 evaluates "
                "energy efficiency (Wh consumed per km). While AIS-040 answers 'how far can it go?', AIS-039 answers "
                "'how much electricity does it cost?'. Both rely on identical dyno coastdown and vehicle preparation procedures."
            ),
        },
        "source": "ARAI AIS-040 (Rev. 1) including Amendments up to 04/2026",
    },

    "AIS-041": {
        "code": "AIS-041",
        "title": "Electric Power Train Vehicles — Measurement of Net Power and Maximum 30 Minute Power",
        "overview": (
            "Specifies the test methods and laboratory procedures for measuring the net power curve, "
            "maximum 30-minute continuous power, and 30-minute maximum speed of electric drive trains."
        ),
        "scope": (
            "Applies to electric drive trains intended for the propulsion of electric power train vehicles of "
            "categories M, N, and L. Specifies bench dynamometer and vehicle dynamometer test setups for "
            "determining motor power across the operating speed range."
        ),
        "category": "EV Powertrain Performance",
        "vehicle_type": "Electric Drive Trains for M, N, L Category Vehicles",
        "purpose": (
            "To determine certified power ratings for motor registration, taxation category classification, "
            "CMVR type approval, and powertrain thermal performance validation under sustained load."
        ),
        "applicability": (
            "Mandatory homologation parameter under CMVR for vehicle registration documents (RC) and motor power rating certification."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Determination of full-load power curve as a function of motor rotational speed (RPM)",
            "Measurement of maximum 30-minute continuous power under sustained thermal equilibrium",
            "Determination of maximum 30-minute vehicle speed under continuous driving load",
            "Accuracy requirements for torque transducer (±0.5%) and speed measurement (±0.5%)",
            "Auxiliary equipment load accounting during motor power determination",
        ],
        "test_focus": [
            "Dynamometer motor bench testing across entire speed envelope",
            "Thermal saturation test under sustained maximum continuous 30-minute output",
            "Net power rating curve compilation for vehicle registration certification",
        ],
        "revision_history": [
            "AIS-041: 2003 (Measurement of Net Power and 30 Minute Power)",
            "AIS-041 (Rev. 1): 2015 (Harmonization with UN ECE R85)",
            "AIS-041 (Rev. 1) Amendment 1 (08/2024): Updated power measurement for integrated axle-drives (e-Axles)",
        ],
        "amendments": [
            "Amendment 1 (08/2024): Included testing provisions for integrated inverter-motor-gearbox (3-in-1 e-Axle) architectures.",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-039",
            "AIS-040",
            "AIS-003",
        ],
        "comparative_study": {
            "primary_role": "Certified electric motor net power and 30-minute continuous power rating",
            "main_output": "Peak Net Power (kW), 30-minute Sustained Power (kW), and Full Load Torque Curve (Nm)",
            "engineering_domain": "Electric Motor Dyno Testing & Thermal Rating",
            "compliance_criteria": "Power output curve must be repeatable within ±2% across speed test points",
            "test_methodology": "Motor dynamometer test at full throttle from base speed to maximum rotational speed with thermal monitoring",
            "best_compared_with": [
                "AIS-003",
                "AIS-039",
                "AIS-040",
            ],
            "comparison_note": (
                "AIS-041 measures the raw mechanical power and sustained continuous thermal capability of the electric motor, "
                "whereas AIS-003 determines if that power is sufficient to start the vehicle on a steep incline. "
                "AIS-041 output ratings directly determine the vehicle's official registration horsepower."
            ),
        },
        "source": "ARAI AIS-041 (Rev. 1) with Amendment 1 (08/2024)",
    },

    "AIS-048": {
        "code": "AIS-048",
        "title": "Battery Operated Vehicles — Safety Requirements of Traction Batteries",
        "overview": (
            "Specifies electrical, mechanical, and environmental safety requirements and destructive "
            "test procedures for traction batteries used in battery-operated vehicles."
        ),
        "scope": (
            "Applies to traction (driving power) batteries used for battery-operated vehicles of categories L, M, and N "
            "as defined in AIS-053. Covers cell and pack-level safety under severe electrical and environmental stress."
        ),
        "category": "EV Traction Battery Safety",
        "vehicle_type": "Traction Batteries for L, M, N Category Vehicles",
        "purpose": (
            "To ensure that traction batteries do not explode, catch fire, emit toxic fumes, or rupture when exposed "
            "to electrical abuse, mechanical impact, or harsh environmental conditions."
        ),
        "applicability": (
            "Component-level type-approval standard for traction battery packs under CMVR."
        ),
        "ev_related": True,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "External short-circuit test with resistance < 5 mΩ without fire or explosion",
            "Overcharge test at 1C / specified charge rate until safety cutoff operates",
            "Over-discharge abuse test to 0V without catastrophic failure",
            "Mechanical shock (acceleration pulses up to 25g/50g) and vibration endurance",
            "Fire resistance test: Direct flame exposure for 70 seconds followed by 60 seconds indirect flame",
            "C-rate and discharge current formula: Current (A) = Capacity (Ah) * C_rate; Time = 1 / C_rate",
        ],
        "test_focus": [
            "Destructive battery pack abuse testing in explosion-proof test bunkers",
            "Flame immersion and fuel fire simulation testing",
            "Drop test, penetration resistance, and high-current short circuiting",
        ],
        "revision_history": [
            "AIS-048: 2009 (Safety Requirements of Traction Batteries)",
            "Amendment 1 (2014): Revised vibration profiles",
            "Amendment 2 (01/2020): Updated short-circuit and fire resistance test protocols",
        ],
        "amendments": [
            "Amendment 2 (01/2020): Clarified pass/fail criteria for secondary lithium-ion chemistry packs.",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-156",
            "AIS-049",
        ],
        "comparative_study": {
            "primary_role": "Component-level traction battery abuse & safety certification",
            "main_output": "Battery pack safety approval against fire, explosion, and mechanical shock",
            "engineering_domain": "Cell & Pack-Level Battery Safety Engineering",
            "compliance_criteria": "Zero flame, zero explosion, zero toxic leakage during electrical, mechanical, and fire abuse",
            "test_methodology": "Destructive laboratory abuse testing: external short circuit (<5mΩ), fuel fire exposure, 50g mechanical shock",
            "best_compared_with": [
                "AIS-038",
                "AIS-156",
                "AIS-049",
            ],
            "comparison_note": (
                "AIS-048 is an isolated battery pack component abuse standard, whereas AIS-038 and AIS-156 are full "
                "vehicle-level safety frameworks. Many tests historically defined in AIS-048 have been upgraded into the "
                "rigorous thermal runaway and water immersion clauses of AIS-038 (Rev. 2) and AIS-156."
            ),
        },
        "source": "ARAI AIS-048 Publication including Amendment 2 (01/2020)",
    },

    "AIS-049": {
        "code": "AIS-049",
        "title": "Electric Power Train Vehicles — CMVR Type Approval",
        "overview": (
            "Prescribes the statutory type-approval and homologation framework, administrative procedures, "
            "and mandatory CMVR rule compliance roadmap for battery-operated and electric powertrain vehicles."
        ),
        "scope": (
            "Applies to all battery-operated vehicles (BoVs) and electric powertrain vehicles seeking type approval "
            "under the Central Motor Vehicles Rules (CMVR) in India. Connects applicable technical test standards "
            "into a unified certification roadmap."
        ),
        "category": "EV Type Approval & Homologation",
        "vehicle_type": "All Electric and Battery Operated Vehicles (L, M, N Categories)",
        "purpose": (
            "To provide vehicle manufacturers and testing agencies (ARAI, ICAT, GARC) with the standardized "
            "administrative compliance roadmap for granting CMVR type approval certificates."
        ),
        "applicability": (
            "Overarching regulatory homologation document for obtaining commercial roadworthiness certification in India."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Compilation of manufacturer technical specification document (Annexure A to G)",
            "Verification of compliance against AIS-038/AIS-156 (Safety), AIS-039 (Energy), AIS-040 (Range), AIS-041 (Power)",
            "Conformity of Production (COP) audit requirements and test intervals",
            "Verification of safety-critical components (traction motor, controller, BMS, charger, wiring harness)",
            "Identification and stamping of vehicle identification number (VIN) and motor serial number",
        ],
        "test_focus": [
            "Complete vehicle homologation documentation audit",
            "Coordination of physical vehicle testing schedule across testing disciplines",
            "COP surveillance and compliance verification audit",
        ],
        "revision_history": [
            "AIS-049: 2003 (CMVR Type Approval for Battery Operated Vehicles)",
            "AIS-049 Amendment 1 (2010): Updated technical information format",
            "AIS-049 Amendment 2 (2015): Revised COP procedures",
            "AIS-049 (Rev. 1): 2016: Modernized type approval guidelines for electric and hybrid vehicles",
        ],
        "amendments": [
            "Amendment 2: Standardized safety critical part approval pathways.",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-039",
            "AIS-040",
            "AIS-041",
            "AIS-048",
            "AIS-053",
            "AIS-156",
        ],
        "comparative_study": {
            "primary_role": "Master homologation & type approval procedural framework",
            "main_output": "CMVR Type Approval Certificate (TAC) & COP Approval",
            "engineering_domain": "Automotive Certification & Regulatory Homologation",
            "compliance_criteria": "Full documentary and physical test compliance across all referenced AIS safety and performance standards",
            "test_methodology": "Documentary verification, safety-critical component traceability, and physical testing audit",
            "best_compared_with": [
                "AIS-038",
                "AIS-156",
                "AIS-053",
            ],
            "comparison_note": (
                "AIS-049 is the administrative master framework that bundles all specific technical tests "
                "(AIS-038 safety, AIS-039 energy, AIS-040 range, AIS-041 power, AIS-004 EMC) into the legal "
                "CMVR Type Approval Certificate required to sell an electric vehicle in India."
            ),
        },
        "source": "ARAI AIS-049 (Rev. 1) Publication",
    },

    "AIS-053": {
        "code": "AIS-053",
        "title": "Automotive Vehicles — Types — Terminology and Classification",
        "overview": (
            "Provides the foundational legal terminology, dimensional criteria, weight thresholds, and "
            "classification taxonomy for all automotive vehicles and trailers in India."
        ),
        "scope": (
            "Defines vehicle categories including Category M (passenger vehicles M1, M2, M3), Category N (goods vehicles N1, N2, N3), "
            "Category L (2-wheelers and 3-wheelers L1, L2, L3, L4, L5, L7), Category T (trailers), and Category A4 (agricultural tractors)."
        ),
        "category": "Vehicle Classification & Taxonomy",
        "vehicle_type": "All Vehicle Categories (M, N, L, T, A4, Special Purpose Vehicles)",
        "purpose": (
            "To establish legally unambiguous definitions of vehicle categories, gross weights, axle layouts, "
            "and body styles that determine which AIS safety and performance standards apply to a given vehicle."
        ),
        "applicability": (
            "Universal reference standard cited across every single AIS standard and CMVR statutory notification."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Classification of Category M: Power-driven vehicles having at least 4 wheels for carriage of passengers (M1 <= 8 seats, M2 <= 5 tonnes, M3 > 5 tonnes)",
            "Classification of Category N: Power-driven vehicles for carriage of goods (N1 <= 3.5 tonnes, N2 3.5-12 tonnes, N3 > 12 tonnes)",
            "Classification of Category L: 2-wheelers and 3-wheelers (L1/L2 mopeds, L3/L4 motorcycles, L5 3-wheelers, L7 quadricycles)",
            "Classification of Category A4: Special purpose wheeled agricultural tractors (including high-clearance A4.1 tractors)",
            "Definitions of unladen mass, gross vehicle weight (GVW), pay mass, and axle weight ratings",
        ],
        "test_focus": [
            "Physical dimensional measurement (length, width, height, ground clearance)",
            "Weighbridge mass determination (unladen mass, gross vehicle weight, axle loading distribution)",
            "Seating capacity and luggage volume verification",
        ],
        "revision_history": [
            "AIS-053: 2005 (Automotive Vehicles - Types - Terminology)",
            "Amendments 1 through 6: Progressive inclusion of specialized body styles",
            "Amendment No. 7 (08/2018): Added Category A4 agricultural tractors and electric quadricycle L7 definitions",
        ],
        "amendments": [
            "Amendment 7 (08/2018): Integrated high-clearance agricultural tractors and quadricycle classification criteria.",
        ],
        "related_standards": [
            "AIS-003",
            "AIS-038",
            "AIS-049",
            "AIS-071",
            "AIS-156",
        ],
        "comparative_study": {
            "primary_role": "Universal vehicle classification & terminology backbone",
            "main_output": "Statutory Vehicle Category determination (e.g. M1, N1, L5M, L7)",
            "engineering_domain": "Vehicle Classification & Regulatory Architecture",
            "compliance_criteria": "Vehicle dimensions, seating layout, and GVW must match the declared category threshold",
            "test_methodology": "Dimensional metrology, weighbridge axle weight analysis, and seating capacity verification",
            "best_compared_with": [
                "AIS-049",
                "AIS-038",
                "AIS-156",
            ],
            "comparison_note": (
                "AIS-053 is the taxonomy dictionary for all automotive standards. Before determining whether an EV "
                "must comply with AIS-038 (M/N vehicles) or AIS-156 (L category), its category must be strictly "
                "established using the weight and seating definitions of AIS-053."
            ),
        },
        "source": "ARAI AIS-053: 2005 with Amendment 7 (08/2018)",
    },

    "AIS-071": {
        "code": "AIS-071",
        "title": "Automotive Vehicles — Identification of Controls, Tell-Tales and Indicators",
        "overview": (
            "Specifies requirements for the location, identification symbols, illumination, and color coding "
            "of vehicle controls, warning tell-tales, and dashboard indicators."
        ),
        "scope": (
            "Applies to motor vehicles of categories L, M, and N. Part 1 covers L-category vehicles (2W/3W), "
            "and Part 2 covers categories L7 (quadricycles), M, and N. Regulates mandatory symbols (headlamps, "
            "brakes, hazard warning, EV isolation fault, battery charge status)."
        ),
        "category": "Driver Interface / Human Factors Ergonomics",
        "vehicle_type": "L, M, N Category Motor Vehicles",
        "purpose": (
            "To ensure that vehicle controls and warning indicators are intuitively recognizable, accessible from "
            "the driving position, and use standardized symbols and colors to minimize driver distraction and error."
        ),
        "applicability": (
            "Mandatory safety standard for vehicle interior dashboard design and instrument cluster type approval under CMVR."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Mandatory standardized color coding: Red = Danger/Critical Fault; Yellow/Amber = Caution/Abnormal System; Green = Normal Operation; Blue = High Beam",
            "Electric vehicle specific tell-tales: Traction battery fault, charging cable connected/interlock, high-voltage isolation warning",
            "Visibility: Indicators must be clearly visible from the driver's normal seated eye position under day and night conditions",
            "Master electrical disconnect switch identification for hazardous goods vehicles and pure electric commercial vehicles",
            "Tail lamp, parking lamp, and number plate lamp control unit integration rules",
        ],
        "test_focus": [
            "Photometric luminance and contrast measurement of dashboard tell-tales",
            "Ergonomic reach zone evaluation from driver 95th-percentile eyellipse and seating position",
            "Verification of symbol geometry against standard icon templates",
        ],
        "revision_history": [
            "AIS-071: 2009 (Identification of Controls, Tell-Tales and Indicators)",
            "AIS-071 (Part 1): Requirements for L Category (except L7)",
            "AIS-071 (Part 2): Requirements for L7, M, and N Category vehicles",
            "Amendment No. 1 (09/2020): Added high-voltage EV isolation warning symbols",
            "Amendment No. 3 (01/2021 & 09/2024): Updated Pure Electric Vehicle ignition and control integration rules",
        ],
        "amendments": [
            "Amendment 1 (09/2020): Added specific tell-tales for EV charging connection and battery thermal warning.",
            "Amendment 3 (09/2024): Permitted digital instrument cluster screen integration for EV master drive controls.",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-156",
            "AIS-053",
        ],
        "comparative_study": {
            "primary_role": "Driver interface symbol standardization & warning tell-tale ergonomics",
            "main_output": "Instrument cluster & dashboard tell-tale compliance approval",
            "engineering_domain": "Human-Machine Interface (HMI) & Vehicle Ergonomics",
            "compliance_criteria": "Strict adherence to standardized symbol glyphs, color conventions (Red/Yellow/Green/Blue), and driver reach zones",
            "test_methodology": "Day/night photometric contrast inspection, driver reach verification, and symbol geometry template comparison",
            "best_compared_with": [
                "AIS-038",
                "AIS-156",
                "AIS-189",
            ],
            "comparison_note": (
                "While AIS-038 and AIS-156 dictate the safety thresholds for electrical isolation and battery faults, "
                "AIS-071 dictates how those faults MUST be visually communicated to the driver on the dashboard "
                "(e.g. amber caution vs red critical buzzer), ensuring intuitive driver response during an EV fault."
            ),
        },
        "source": "ARAI AIS-071 (Part 1 & 2) including Amendment 3 (09/2024)",
    },

    "AIS-137": {
        "code": "AIS-137",
        "title": "Test Methods, Testing Equipment and Related Procedures for Type Approval and Conformity of Production",
        "overview": (
            "Comprehensive multi-part testing manual prescribing emissions measurement, chassis dynamometer calibration, "
            "portable emissions measurement systems (PEMS), and EV energy test instrumentation."
        ),
        "scope": (
            "Applies to vehicles of categories M, N, and L. Covers Parts 1 through 9 addressing tailpipe emissions, "
            "OBD-II on-board diagnostics, Real Driving Emissions (RDE), and instrument accuracy for electric powertrain certification."
        ),
        "category": "Emissions & Homologation Test Metrology",
        "vehicle_type": "M, N, and L Category Motor Vehicles",
        "purpose": (
            "To provide detailed calibration specifications for dynamometers, gas analyzers, power analyzers, "
            "and metrological instruments used across CMVR type approval testing."
        ),
        "applicability": (
            "Technical reference standard for testing laboratories and OEM homologation testing facilities."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Dynamometer inertia simulation calibration tolerances (±0.5%)",
            "Specifications for high-precision AC/DC power meters (Class 0.5 or better) for EV energy measurement",
            "Chassis dynamometer coastdown calculation protocols for aerodynamic drag and rolling resistance determination",
            "Ambient temperature and humidity control in test cells (25°C ± 5°C)",
            "Calibration and span gas tolerances for exhaust and evaporative emissions measurement benches",
        ],
        "test_focus": [
            "Chassis dynamometer load cell and inertia simulation calibration",
            "Dynamometer coastdown polynomial curve fitting (F = F0 + F2*v^2)",
            "Power analyzer synchronization with vehicle CAN bus telemetry",
        ],
        "revision_history": [
            "AIS-137 (Parts 1 to 7): 2019 (BS-IV and BS-VI Test Procedures)",
            "AIS-137 (Part 8 & 9): RDE and Electric Powertrain Test Instrumentation",
            "Amendments up to 2023: Updated for Phase-II Real Driving Emissions (RDE) and EV data acquisition standards",
        ],
        "amendments": [
            "Amendment 2023: Updated power analyzer calibration procedures for high-voltage DC bus measurement.",
        ],
        "related_standards": [
            "AIS-039",
            "AIS-040",
            "AIS-041",
            "AIS-049",
        ],
        "comparative_study": {
            "primary_role": "Laboratory testing equipment calibration & metrology manual",
            "main_output": "Test facility certification & instrumentation accuracy compliance",
            "engineering_domain": "Testing Instrumentation & Dyno Metrology",
            "compliance_criteria": "Dyno load error < 1%; electrical energy power analyzer accuracy within Class 0.5 limits",
            "test_methodology": "Chassis dynamometer coastdown calibration, electrical meter precision audit, gas analyzer span calibration",
            "best_compared_with": [
                "AIS-039",
                "AIS-040",
                "AIS-049",
            ],
            "comparison_note": (
                "AIS-137 provides the technical laboratory metrology rules (how to calibrate dynos, how to measure road load, "
                "what power meter class to use) that are strictly utilized when executing the energy consumption tests of "
                "AIS-039 and the range tests of AIS-040."
            ),
        },
        "source": "ARAI AIS-137 Multi-Part Publication",
    },

    "AIS-138": {
        "code": "AIS-138",
        "title": "Electric Vehicle Conductive Charging System — Part 1 (AC Charging) and Part 2 (DC Fast Charging)",
        "overview": (
            "Comprehensive standard for electric vehicle conductive charging infrastructure and onboard systems, "
            "covering AC Level 1/2 charging protocols (Part 1) and high-power DC fast charging systems (Part 2)."
        ),
        "scope": (
            "Applies to EV supply equipment (EVSE) and onboard vehicle inlets. Part 1 covers AC conductive charging "
            "up to 250V 1-phase / 480V 3-phase and up to 63A (Modes 2 & 3). Part 2 covers DC off-board fast chargers up to 1000V DC "
            "and 400A (Mode 4 / Bharat DC-001, CCS-2, CHAdeMO)."
        ),
        "category": "EV Charging Infrastructure & Electrical Safety",
        "vehicle_type": "EV Supply Equipment (EVSE) and All Electric Vehicles (L, M, N Categories)",
        "purpose": (
            "To guarantee electrical safety, interoperability, control-pilot communications, and insulation monitoring "
            "during conductive AC and DC fast charging of electric vehicles."
        ),
        "applicability": (
            "Mandatory certification standard for EV charging stations, wallbox chargers, portable charging cables, and vehicle charging inlets."
        ),
        "ev_related": True,
        "formula_available": True,
        "calculator_available": True,
        "key_requirements": [
            "Part 1 Control Pilot PWM duty cycle signaling: Low range (6-51A, Duty = Current / 0.6) and High range (51-80A, Duty = Current / 2.5 + 64)",
            "Part 2 DC fast charging safety: Continuous insulation monitoring of isolated DC bus, body contact current Ih, and earth leakage current Ig",
            "Mechanical interlock: Vehicle drive-away prevention while the charging connector is engaged",
            "Touch current safety: Leakage current to touchable metal parts must remain <= 3.5 mA AC / 10 mA DC",
            "Emergency stop push-button with immediate relay isolation (< 100 ms) upon actuation",
        ],
        "test_focus": [
            "Control pilot PWM voltage (+12V, +9V, +6V state transitions) and duty cycle verification",
            "DC body-contact and earth-leakage current calculation under grounding resistance networks",
            "High-voltage DC contactor weld detection and pre-charge circuit safety validation",
            "IP54/IP55 weatherproofing and cable mechanical pull/drive-over testing",
        ],
        "revision_history": [
            "AIS-138 (Part 1): February 2017 (Electric Vehicle Conductive AC Charging System)",
            "AIS-138 (Part 2): January 2018 (Electric Vehicle Conductive DC Charging System)",
            "Amendments: Harmonized with IEC 61851-1, IEC 61851-23, and Bharat EV specifications",
        ],
        "amendments": [
            "Incorporated Combined Charging System (CCS Type 2) and Bharat DC-001 charging connector protocols.",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-156",
            "AIS-048",
        ],
        "comparative_study": {
            "primary_role": "EV conductive charging infrastructure & vehicle-to-charger interface safety",
            "main_output": "EVSE and charging inlet safety certification, PWM duty cycle & DC insulation compliance",
            "engineering_domain": "EV Charging Architecture, Power Electronics & Grid Interface",
            "compliance_criteria": "Control pilot PWM accuracy ±0.5%; DC isolation resistance monitoring > 100 kΩ; touch current < 3.5 mA",
            "test_methodology": "Oscilloscope pilot pulse-width measurement, insulation resistance fault injection, DC contactor timing validation",
            "best_compared_with": [
                "AIS-038",
                "AIS-156",
                "AIS-048",
            ],
            "comparison_note": (
                "AIS-138 governs the electrical safety and communications between the external electrical grid/charger "
                "and the vehicle, whereas AIS-038/AIS-156 govern the internal vehicle battery and powertrain safety. "
                "AIS-138 Part 1 (AC) and Part 2 (DC) together ensure full interoperability across home wallboxes and highway fast chargers."
            ),
        },
        "source": "ARAI AIS-138 (Part 1: 2017 & Part 2: 2018) Publications",
    },

    "AIS-156": {
        "code": "AIS-156",
        "title": "Specific Requirements for L Category Electric Power Train Vehicles",
        "overview": (
            "The dedicated electrical safety, REESS, and functional safety standard for 2-wheeled and 3-wheeled "
            "electric vehicles (Categories L1, L2, L5, L7), including swappable battery systems."
        ),
        "scope": (
            "Applies to L-category electric powertrain vehicles (electric scooters, motorcycles, 3-wheelers, quadricycles). "
            "Regulates electric shock protection, REESS mechanical and environmental safety, thermal propagation prevention, "
            "swappable battery packs, and battery swapping station interfaces."
        ),
        "category": "2-Wheeler / 3-Wheeler EV Safety",
        "vehicle_type": "L Category Electric Power Train Vehicles (L1, L2, L3, L4, L5, L7)",
        "purpose": (
            "To eliminate battery fire risks in electric 2-wheelers and 3-wheelers, enforce rigorous thermal propagation "
            "safeguards, ensure swappable battery durability, and protect riders from high-voltage hazards."
        ),
        "applicability": (
            "Mandatory type-approval standard for all electric scooters, motorcycles, e-rickshaws, and e-autos in India under CMVR."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Thermal propagation test: Single-cell thermal runaway must NOT propagate to adjacent cells or cause fire/explosion for at least 5 minutes",
            "Audible alarm buzzer (> 75 dBA) inside rider's acoustic field warning of thermal runaway occurrence",
            "Water ingress protection: Minimum IPX7 protection for battery pack (1 meter water immersion for 30 minutes)",
            "Drop test: Battery pack dropped from 1 meter height on all 6 faces without casing crack, short-circuit, or fire",
            "Swappable battery pack requirements: Rated for minimum 1000 connect/disconnect cycles without pin deterioration",
            "Active micro-controller BMS with cell-level voltage, multi-point temperature sensing, and overcharge safety cutoff",
        ],
        "test_focus": [
            "Thermal propagation initiation via heating cartridge / nail trigger inside pack",
            "IPX7 1-meter water immersion and high-pressure water jet IPX5 testing",
            "Mechanical drop, vibration, and crush testing on 2W/3W battery packs",
            "Battery swapping connector cycle endurance and interlock verification",
        ],
        "revision_history": [
            "AIS-156: 2020 (Specific Requirements for L Category Electric Power Train Vehicles)",
            "AIS-156 Amendment 1 (2021): Added BMS data logging requirements",
            "AIS-156 Amendment 2 (2022): Mandated active thermal runaway buzzer and cell spacing",
            "AIS-156 Amendment 3 (2023): Enhanced overcharge protection and fuse coordination",
            "AIS-156 Amendment 4 (12/2023): Comprehensive clauses for Swappable Battery Packs and Battery Swapping Stations",
        ],
        "amendments": [
            "Amendment 2 (2022): Mandated thermal propagation warning and spacing between cylindrical/pouch cells.",
            "Amendment 4 (12/2023): Introduced complete testing framework for Swappable Battery Packs (clause 2.46) and Swapping Stations (clause 2.47).",
        ],
        "related_standards": [
            "AIS-038",
            "AIS-048",
            "AIS-138",
            "AIS-049",
            "AIS-053",
        ],
        "comparative_study": {
            "primary_role": "Dedicated EV electrical, battery & functional safety for 2-wheelers and 3-wheelers (Category L)",
            "main_output": "Type approval certification for 2W/3W EV safety and swappable battery pack compliance",
            "engineering_domain": "Light EV Safety, Swappable Batteries & Thermal Runaway Mitigation",
            "compliance_criteria": "No fire/explosion during 5-minute thermal propagation; IPX7 water immersion pass; 1-meter drop test pass",
            "test_methodology": "Cell heating thermal runaway trigger, 1m water immersion tank, 1000-cycle swapping connector durability test",
            "best_compared_with": [
                "AIS-038",
                "AIS-048",
                "AIS-138",
                "AIS-049",
            ],
            "comparison_note": (
                "AIS-156 is the L-category (2W/3W) counterpart to AIS-038 (4W/commercial M & N vehicles). "
                "AIS-156 includes unique requirements tailored to lightweight vehicles, such as 1-meter drop tests, "
                "IPX7 flood immersion, swappable battery pack connector durability (1000 cycles), and swapping station safety."
            ),
        },
        "source": "ARAI AIS-156: 2020 including Amendment 4 (12/2023)",
    },

    "AIS-189": {
        "code": "AIS-189",
        "title": "Approval of Vehicles with Regard to Cyber Security and Cyber Security Management System (CSMS)",
        "overview": (
            "Establishes regulatory provisions and certification requirements for automotive Cyber Security "
            "and Cyber Security Management Systems (CSMS) across connected vehicle architectures."
        ),
        "scope": (
            "Applies to vehicles of categories M and N. Also applies to Category T (trailers) if fitted with at least "
            "one electronic control unit (ECU), and Category L7 (quadricycles) if equipped with automated driving functionalities "
            "from Level 3 onwards. Harmonized with UNECE Regulation 155 (UN R155)."
        ),
        "category": "Automotive Cybersecurity & Connected Vehicles",
        "vehicle_type": "M, N, L7 (Level 3+), and T Category Vehicles with ECUs",
        "purpose": (
            "To protect connected vehicles from cyber attacks, unauthorized telemetry access, malicious CAN bus injection, "
            "spoofing of navigation/V2X signals, and remote tampering with safety-critical steering, braking, or battery systems."
        ),
        "applicability": (
            "Mandatory compliance requirement under CMVR for type approval of connected and automated vehicles in India."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Establishment of an organization-wide Cyber Security Management System (CSMS) certified by testing agencies",
            "Threat analysis and risk assessment (TARA) covering vehicle communication channels, backend servers, and telematics",
            "Mitigation against message spoofing (V2X cooperative awareness, GNSS spoofing, Sybil attacks)",
            "Protection of vehicle internal network (CAN, Ethernet, LIN) against malicious injection and tampering",
            "Incident response plan and continuous vulnerability monitoring throughout vehicle lifecycle (minimum 10 years)",
        ],
        "test_focus": [
            "CSMS organizational process and governance audit",
            "Penetration testing and vulnerability scanning on vehicle ECUs and telematics control units (TCU)",
            "Verification of cryptographic message authentication (SecOC) on high-speed vehicle networks",
        ],
        "revision_history": [
            "AIS-189: 2023 (Cyber Security and Cyber Security Management System)",
            "AIS-189 Amendment No. 1 (11/2025): Expanded threat catalog and updated V2X message spoofing mitigation clauses",
        ],
        "amendments": [
            "Amendment 1 (11/2025): Aligned Annexure D threat vectors with updated ISO/SAE 21434 and UN R155 revisions.",
        ],
        "related_standards": [
            "AIS-190",
            "AIS-004",
            "AIS-038",
            "AIS-071",
        ],
        "comparative_study": {
            "primary_role": "Automotive cybersecurity governance (CSMS) & vehicle threat mitigation",
            "main_output": "CSMS Certificate of Compliance & Vehicle Type Approval for Cybersecurity",
            "engineering_domain": "Connected Vehicle Cybersecurity & Embedded Network Security",
            "compliance_criteria": "Documented TARA risk mitigation for all known threat vectors; cryptographically secured external communication",
            "test_methodology": "OEM CSMS process audit, ECU penetration testing, fuzz testing, and communication channel vulnerability assessment",
            "best_compared_with": [
                "AIS-190",
                "AIS-004",
                "AIS-038",
            ],
            "comparison_note": (
                "AIS-189 (Cybersecurity / UN R155) and AIS-190 (Software Updates / UN R156) form the digital security twins "
                "of modern connected vehicles. While AIS-189 protects against cyber attacks, intrusions, and spoofing, "
                "AIS-190 ensures that when software patches and updates are transmitted over-the-air (OTA), they are "
                "deployed safely without bricking the vehicle or compromising safety systems."
            ),
        },
        "source": "ARAI AIS-189: 2023 including Amendment 1 (11/2025)",
    },

    "AIS-190": {
        "code": "AIS-190",
        "title": "Approval of Vehicles with Regard to Software Update and Software Updates Management System (SUMS)",
        "overview": (
            "Establishes uniform regulatory provisions for Software Updates and Software Updates Management Systems (SUMS) "
            "governing Over-The-Air (OTA) and wired ECU firmware updates."
        ),
        "scope": (
            "Applies to motor vehicles of categories M, N, T, A, and C that permit software updates. Regulates the software "
            "delivery pipeline, software identification numbers (RxSWIN), Over-The-Air (OTA) safety interlocks, "
            "and update integrity verification. Harmonized with UNECE Regulation 156 (UN R156)."
        ),
        "category": "Software Updates & Over-The-Air (OTA) Management",
        "vehicle_type": "M, N, T, A, C Category Vehicles permitting Software Updates",
        "purpose": (
            "To guarantee that software updates (especially Over-The-Air) do not compromise vehicle roadworthiness, "
            "cannot be applied while the vehicle is in motion, maintain full traceability with type approval authorities, "
            "and provide fail-safe rollback in case of update interruption."
        ),
        "applicability": (
            "Mandatory homologation standard for all vehicles equipped with OTA update capabilities under CMVR."
        ),
        "ev_related": True,
        "formula_available": False,
        "calculator_available": False,
        "key_requirements": [
            "Certified Software Update Management System (SUMS) at the vehicle manufacturer organization",
            "Regulation-specific Software Identification Numbers (RxSWIN) linked to type-approval parameters",
            "OTA Update Safety Interlock: Vehicle must be parked and in a safe condition before update execution begins",
            "Driver notification and explicit consent before critical firmware installation",
            "Fail-safe rollback mechanism: If update fails or is interrupted, vehicle must safely restore previous functional state",
            "Verification that updates do not alter certified power, emissions, range, or braking without regulatory re-approval",
        ],
        "test_focus": [
            "SUMS organizational audit and OTA cryptographic delivery pipeline inspection",
            "Simulation of interrupted updates (battery disconnection, signal loss) to verify fail-safe recovery",
            "RxSWIN software version traceability audit against CMVR Type Approval Certificates",
        ],
        "revision_history": [
            "AIS-190: April 2024 (Uniform provisions for Software Updates Management System)",
            "AIS-190 Interpretation Manual: May 2024 Version (Detailed compliance evidence guidelines for Test Agencies)",
        ],
        "amendments": [
            "Published with May 2024 Interpretation Manual establishing harmonized test agency audit criteria.",
        ],
        "related_standards": [
            "AIS-189",
            "AIS-038",
            "AIS-049",
            "AIS-071",
        ],
        "comparative_study": {
            "primary_role": "Software Update Management System (SUMS) & Over-The-Air (OTA) update safety",
            "main_output": "SUMS Certificate of Compliance & RxSWIN Software Version Type Approval",
            "engineering_domain": "Over-The-Air (OTA) Telematics & Embedded Firmware Architecture",
            "compliance_criteria": "Zero update execution while vehicle is moving; 100% fail-safe rollback capability; valid RxSWIN traceability",
            "test_methodology": "SUMS organizational audit, interrupted OTA update recovery simulation, RxSWIN electronic readout verification",
            "best_compared_with": [
                "AIS-189",
                "AIS-049",
                "AIS-038",
            ],
            "comparison_note": (
                "AIS-190 works in strict synergy with AIS-189 (Cybersecurity). AIS-189 prevents hackers from tampering "
                "with the telematics channel, while AIS-190 governs the legitimate deployment of software updates, "
                "ensuring that when a manufacturer updates the BMS or motor controller firmware via OTA, the update is "
                "cryptographically signed, executed safely only when parked, and maintains CMVR compliance."
            ),
        },
        "source": "ARAI AIS-190 (April 2024) & Interpretation Manual (May 2024)",
    },

}
