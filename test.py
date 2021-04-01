def minimum_input():
    return {
        'demand': {
            'electric': {
                'total_consumptions': {
                    'yearly': 456.5,
                },
            },
            'heating': {
                'total_consumptions': {
                    'yearly': 456.5,
                },
            },
            'dhw': {
                'total_consumptions': {
                    'yearly': 456.5,
                },
            },
            'cooling': {
                'total_consumptions': {
                    'yearly': 456.5,
                },
            },
        },
        'system': {
            'general': {
                'location': {
                    'lat': 0.2849424798,
                    'lon': 0.3759827350,
                    'elev': 400.24,
                    'albedo': 212,
                    'surface_tilt': 60.4,
                    'surface_azimuth': 50,
                    'country': 'IT',
                    'tz': 'CET',
                },
            },
            'pv': {
                'cost_per_unit': 200,
            },
            'inverter': {
                'cost_per_unit': 300,
            },
            'stc': {
                'cost_per_unit': 400,
            },
            'bf': {
                'cost_per_liter': 5,
            },
            'ahx': {
                'cost_per_kW_th': 7,
            },
            'ghx': {
                'cost_per_kW_th': 7,
            },
            'hp': {
                'cost_per_kW_el': 7,
            },
            'pcm': {
                'cost_per_kg': 1,
            }
        },
        'misc_params': {
            'financial': {
                'hourly _energy_import_tariff': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                'hourly_energy_generation_tariff': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                'hourly_energy_export_tariff': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                'daily_standing_charge': 4.5,
                'discount_rate': 0.0,
            },
            'carbon_intensity': 0.5,
        }
    }


def array_test():
    return {
        'demand': {
            'electric': {
                'total_consumptions': {
                    'yearly': 456.5,
                    'monthly': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
                },
            },
            'heating': {
                'consumptions': {
                    'yearly': 456.5,
                },
            },
            'dhw': {
                'consumptions': {
                    'yearly': 456.5,
                },
            },
            'cooling': {
                'consumptions': {
                    'yearly': 456.5,
                },
            },
        },
        'system': {
            'general': {
                'location': {
                    'lat': 0.2849424798,
                    'lon': 0.3759827350,
                    'elev': 400.24,
                    'albedo': 212,
                    'surface_tilt': 60.4,
                    'surface_azimuth': 50,
                    'country': 'IT',
                    'tz': 'CET',
                },
            },
            'pv': {
                'cost_per_unit': 200,
            },
            'inverter': {
                'cost_per_unit': 300,
            },
            'stc': {
                'cost_per_unit': 400,
            },
            'bf': {
                'cost_per_liter': 5,
            },
            'ahx': {
                'cost_per_kW_th': 7,
            },
            'ghx': {
                'cost_per_kW_th': 7,
            },
            'hp': {
                'cost_per_kW_el': 7,
            },
            'pcm': {
                'cost_per_kg': 1,
            }
        },
        'misc_params': {
            'financial': {
                'hourly _energy_import_tariff': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                'hourly_energy_generation_tariff': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                'hourly_energy_export_tariff': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                'daily_standing_charge': 4.5,
                'discount_rate': 0.0,
            },
            'carbon_intensity': 0.5,
        }
    }


def pupin_input():
    return {
        "demand": {"electric": {"total_consumptions": {"yearly": 1000, "monthly": None, "daily": None, "hourly": None},
                                "profiles": {
                                    "monthly": [0.0996, 0.0859, 0.0668, 0.09, 0.0799, 0.0704, 0.0847, 0.071, 0.0722,
                                                0.0853, 0.0906, 0.1038], "hourly": {"winter": {
                                        "working": [0.0297, 0.0248, 0.0208, 0.0198, 0.0193, 0.0198, 0.0243, 0.0387,
                                                    0.0416, 0.0401, 0.0362, 0.0352, 0.0357, 0.0391, 0.0377, 0.0456,
                                                    0.058, 0.0684, 0.0743, 0.0733, 0.0664, 0.0614, 0.05, 0.0396],
                                        "nonworking": [0.0299, 0.0261, 0.0212, 0.0198, 0.0193, 0.0193, 0.0203, 0.029,
                                                       0.0367, 0.0405, 0.0434, 0.0483, 0.0478, 0.0492, 0.0492, 0.0463,
                                                       0.0531, 0.0618, 0.0676, 0.0714, 0.0598, 0.055, 0.0483, 0.0367]},
                                                                                    "spring": {
                                                                                        "working": [0.0371, 0.032,
                                                                                                    0.0256, 0.0249,
                                                                                                    0.0256, 0.0243,
                                                                                                    0.0256, 0.0281,
                                                                                                    0.0377, 0.039,
                                                                                                    0.0428, 0.0448,
                                                                                                    0.0448, 0.0448,
                                                                                                    0.0441, 0.0454,
                                                                                                    0.0486, 0.0563,
                                                                                                    0.0556, 0.0563,
                                                                                                    0.0537, 0.0595,
                                                                                                    0.0563, 0.0473],
                                                                                        "nonworking": [0.0377, 0.034,
                                                                                                       0.0264, 0.0252,
                                                                                                       0.0245, 0.0239,
                                                                                                       0.0252, 0.0264,
                                                                                                       0.0358, 0.039,
                                                                                                       0.0434, 0.0516,
                                                                                                       0.056, 0.0572,
                                                                                                       0.0497, 0.0459,
                                                                                                       0.0465, 0.0497,
                                                                                                       0.0503, 0.0516,
                                                                                                       0.0516, 0.0528,
                                                                                                       0.0516, 0.044]},
                                                                                    "summer": {
                                                                                        "working": [0.0371, 0.032,
                                                                                                    0.0256, 0.0249,
                                                                                                    0.0256, 0.0243,
                                                                                                    0.0256, 0.0281,
                                                                                                    0.0377, 0.039,
                                                                                                    0.0428, 0.0448,
                                                                                                    0.0448, 0.0448,
                                                                                                    0.0441, 0.0454,
                                                                                                    0.0486, 0.0563,
                                                                                                    0.0556, 0.0563,
                                                                                                    0.0537, 0.0595,
                                                                                                    0.0563, 0.0473],
                                                                                        "nonworking": [0.0377, 0.034,
                                                                                                       0.0264, 0.0252,
                                                                                                       0.0245, 0.0239,
                                                                                                       0.0252, 0.0264,
                                                                                                       0.0358, 0.039,
                                                                                                       0.0434, 0.0516,
                                                                                                       0.056, 0.0572,
                                                                                                       0.0497, 0.0459,
                                                                                                       0.0465, 0.0497,
                                                                                                       0.0503, 0.0516,
                                                                                                       0.0516, 0.0528,
                                                                                                       0.0516, 0.044]},
                                                                                    "fall": {"working": [0.0297, 0.0248,
                                                                                                         0.0208, 0.0198,
                                                                                                         0.0193, 0.0198,
                                                                                                         0.0243, 0.0387,
                                                                                                         0.0416, 0.0401,
                                                                                                         0.0362, 0.0352,
                                                                                                         0.0357, 0.0391,
                                                                                                         0.0377, 0.0456,
                                                                                                         0.058, 0.0684,
                                                                                                         0.0743, 0.0733,
                                                                                                         0.0664, 0.0614,
                                                                                                         0.05, 0.0396],
                                                                                             "nonworking": [0.0299,
                                                                                                            0.0261,
                                                                                                            0.0212,
                                                                                                            0.0198,
                                                                                                            0.0193,
                                                                                                            0.0193,
                                                                                                            0.0203,
                                                                                                            0.029,
                                                                                                            0.0367,
                                                                                                            0.0405,
                                                                                                            0.0434,
                                                                                                            0.0483,
                                                                                                            0.0478,
                                                                                                            0.0492,
                                                                                                            0.0492,
                                                                                                            0.0463,
                                                                                                            0.0531,
                                                                                                            0.0618,
                                                                                                            0.0676,
                                                                                                            0.0714,
                                                                                                            0.0598,
                                                                                                            0.055,
                                                                                                            0.0483,
                                                                                                            0.0367]}}},
                                "noise": {"daily": 0.1, "hourly": 0.1}},
                   "heating": {"total_consumptions": {"yearly": 1000, "monthly": None, "daily": None, "hourly": None},
                               "profiles": {
                                   "monthly": [0.2102, 0.1639, 0.1206, 0.0826, 0.0627, 0, 0, 0, 0, 0.0765, 0.1051,
                                               0.1783], "hourly": {"winter": {
                                       "working": [0.0541, 0.0542, 0.0597, 0.06, 0.071, 0.0819, 0.0926, 0.0868, 0.0599,
                                                   0.0493, 0.0438, 0.0275, 0.0217, 0.0217, 0.016, 0.016, 0.0159, 0.0218,
                                                   0.027, 0.027, 0.0217, 0.0217, 0.0218, 0.027],
                                       "nonworking": [0.0541, 0.0542, 0.0597, 0.06, 0.071, 0.0819, 0.0926, 0.0868,
                                                      0.0599, 0.0493, 0.0438, 0.0275, 0.0217, 0.0217, 0.016, 0.016,
                                                      0.0159, 0.0218, 0.027, 0.027, 0.0217, 0.0217, 0.0218, 0.027]},
                                                                   "spring": {
                                                                       "working": [0.0541, 0.0542, 0.0597, 0.06, 0.071,
                                                                                   0.0819, 0.0926, 0.0868, 0.0599,
                                                                                   0.0493, 0.0438, 0.0275, 0.0217,
                                                                                   0.0217, 0.016, 0.016, 0.0159, 0.0218,
                                                                                   0.027, 0.027, 0.0217, 0.0217, 0.0218,
                                                                                   0.027],
                                                                       "nonworking": [0.0541, 0.0542, 0.0597, 0.06,
                                                                                      0.071, 0.0819, 0.0926, 0.0868,
                                                                                      0.0599, 0.0493, 0.0438, 0.0275,
                                                                                      0.0217, 0.0217, 0.016, 0.016,
                                                                                      0.0159, 0.0218, 0.027, 0.027,
                                                                                      0.0217, 0.0217, 0.0218, 0.027]},
                                                                   "summer": {
                                                                       "working": [0.0541, 0.0542, 0.0597, 0.06, 0.071,
                                                                                   0.0819, 0.0926, 0.0868, 0.0599,
                                                                                   0.0493, 0.0438, 0.0275, 0.0217,
                                                                                   0.0217, 0.016, 0.016, 0.0159, 0.0218,
                                                                                   0.027, 0.027, 0.0217, 0.0217, 0.0218,
                                                                                   0.027],
                                                                       "nonworking": [0.0541, 0.0542, 0.0597, 0.06,
                                                                                      0.071, 0.0819, 0.0926, 0.0868,
                                                                                      0.0599, 0.0493, 0.0438, 0.0275,
                                                                                      0.0217, 0.0217, 0.016, 0.016,
                                                                                      0.0159, 0.0218, 0.027, 0.027,
                                                                                      0.0217, 0.0217, 0.0218, 0.027]},
                                                                   "fall": {
                                                                       "working": [0.0541, 0.0542, 0.0597, 0.06, 0.071,
                                                                                   0.0819, 0.0926, 0.0868, 0.0599,
                                                                                   0.0493, 0.0438, 0.0275, 0.0217,
                                                                                   0.0217, 0.016, 0.016, 0.0159, 0.0218,
                                                                                   0.027, 0.027, 0.0217, 0.0217, 0.0218,
                                                                                   0.027],
                                                                       "nonworking": [0.0541, 0.0542, 0.0597, 0.06,
                                                                                      0.071, 0.0819, 0.0926, 0.0868,
                                                                                      0.0599, 0.0493, 0.0438, 0.0275,
                                                                                      0.0217, 0.0217, 0.016, 0.016,
                                                                                      0.0159, 0.0218, 0.027, 0.027,
                                                                                      0.0217, 0.0217, 0.0218, 0.027]}}},
                               "noise": {"daily": 0.1, "hourly": 0.1}},
                   "dhw": {"total_consumptions": {"yearly": 1000, "monthly": None, "daily": None, "hourly": None},
                           "profiles": {
                               "monthly": [0.0937, 0.0937, 0.0886, 0.0937, 0.0835, 0.0734, 0.0734, 0.0709, 0.0684,
                                           0.081, 0.081, 0.0987], "hourly": {"winter": {
                                   "working": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594, 0.0716,
                                               0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324, 0.0394,
                                               0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455],
                                   "nonworking": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594,
                                                  0.0716, 0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324,
                                                  0.0394, 0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455]}, "spring": {
                                   "working": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594, 0.0716,
                                               0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324, 0.0394,
                                               0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455],
                                   "nonworking": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594,
                                                  0.0716, 0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324,
                                                  0.0394, 0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455]}, "summer": {
                                   "working": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594, 0.0716,
                                               0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324, 0.0394,
                                               0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455],
                                   "nonworking": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594,
                                                  0.0716, 0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324,
                                                  0.0394, 0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455]}, "fall": {
                                   "working": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594, 0.0716,
                                               0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324, 0.0394,
                                               0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455],
                                   "nonworking": [0.0128, 0.0131, 0.0193, 0.0193, 0.0193, 0.0193, 0.0157, 0.0594,
                                                  0.0716, 0.0655, 0.0554, 0.0524, 0.0394, 0.036, 0.0261, 0.0259, 0.0324,
                                                  0.0394, 0.0517, 0.0718, 0.0783, 0.0783, 0.052, 0.0455]}}},
                           "noise": {"daily": 0.1, "hourly": 0.1}},
                   "cooling": {"total_consumptions": {"yearly": 1000, "monthly": None, "daily": None, "hourly": None},
                               "profiles": {"monthly": [0, 0, 0, 0, 0, 0.2382, 0.343, 0.2952, 0.1236, 0, 0, 0],
                                            "hourly": {"winter": {
                                                "working": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                            0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                            0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                            0.0449, 0.0425, 0.0425],
                                                "nonworking": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                               0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                               0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                               0.0449, 0.0425, 0.0425]}, "spring": {
                                                "working": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                            0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                            0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                            0.0449, 0.0425, 0.0425],
                                                "nonworking": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                               0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                               0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                               0.0449, 0.0425, 0.0425]}, "summer": {
                                                "working": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                            0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                            0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                            0.0449, 0.0425, 0.0425],
                                                "nonworking": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                               0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                               0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                               0.0449, 0.0425, 0.0425]}, "fall": {
                                                "working": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                            0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                            0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                            0.0449, 0.0425, 0.0425],
                                                "nonworking": [0.0292, 0.0236, 0.021, 0.0181, 0.0183, 0.0184, 0.0186,
                                                               0.0184, 0.0186, 0.0242, 0.0319, 0.0476, 0.0558, 0.0661,
                                                               0.069, 0.0688, 0.0739, 0.0739, 0.0688, 0.0584, 0.0476,
                                                               0.0449, 0.0425, 0.0425]}}},
                               "noise": {"daily": 0.1, "hourly": 0.1}}}, "system": {"general": {"time": {"year": 2021},
                                                                                                "location": {
                                                                                                    "lat": 44.787197,
                                                                                                    "lon": 20.457273,
                                                                                                    "elev": 140.0,
                                                                                                    "albedo": 0.2,
                                                                                                    "surface_tilt": 30.0,
                                                                                                    "surface_azimuth": 180.0,
                                                                                                    "country": "SRB",
                                                                                                    "tz": "Europe/Belgrade"}},
                                                                                    "pv": {
                                                                                        "mount_type": "open_rack_glass_glass",
                                                                                        "module_type": "Canadian_Solar_CS5P_220M___2009_",
                                                                                        "cost_per_unit": 200.0,
                                                                                        "estimated_lifetime": 25,
                                                                                        "model_params": None},
                                                                                    "inverter": {
                                                                                        "model_name": "ABB__MICRO_0_25_I_OUTD_US_208__208V_",
                                                                                        "cost_per_unit": 240.0,
                                                                                        "estimated_lifetime": 10,
                                                                                        "model_params": None},
                                                                                    "stc": {"cost_per_unit": 1200.0,
                                                                                            "A": 2.02, "lkf_lin": 3.75,
                                                                                            "lkf_quad": 0.015,
                                                                                            "eta_opt": 0.9},
                                                                                    "bf": {"cost_per_liter": 100.0,
                                                                                           "estimated_lifetime": 10},
                                                                                    "ahx": {"cost_per_kW_th": 200.0,
                                                                                            "estimated_lifetime": 20},
                                                                                    "ghx": {"cost_per_kW_th": 175.0,
                                                                                            "estimated_lifetime": 50},
                                                                                    "hp": {"cost_per_kW_el": 125.0,
                                                                                           "estimated_lifetime": 25},
                                                                                    "pcm": {"cost_per_kg": 50.0,
                                                                                            "estimated_lifetime": 50}},
        "misc_params": {"financial": {
            "hourly_energy_import_tariff": [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.015, 0.015, 0.015, 0.015,
                                            0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015,
                                            0.015],
            "hourly_energy_generation_tariff": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "hourly_energy_export_tariff": [0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008,
                                            0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008,
                                            0.008, 0.008], "daily_standing_charge": 0.04, "discount_rate": 0.005},
                        "carbon_intensity": 1.54, "criteria_weights": {"op_cost": 0.8, "co2": 0.1, "res_share": 0.1}},
        "configurations": [{"id": 1, "num_pv_panels": 4, "num_inverters": 1, "num_stc_panels": 2,
                            "yearly_maintenance_cost_ratio": 0.02, "additional_yearly_costs": 0.0,
                            "cost_reduction": None},
                           {"id": 2, "num_pv_panels": 6, "num_inverters": 1, "num_stc_panels": 3,
                            "yearly_maintenance_cost_ratio": 0.02, "additional_yearly_costs": 0.0,
                            "cost_reduction": None},
                           {"id": 3, "num_pv_panels": 10, "num_inverters": 2, "num_stc_panels": 4,
                            "yearly_maintenance_cost_ratio": 0.02, "additional_yearly_costs": 0.0,
                            "cost_reduction": None}]
    }


def pupin_output():
    return {
        "id": 1614248880980072,
        "configurations": [
            {
                "input": {
                    "id": 1,
                    "num_pv_panels": 4,
                    "num_inverters": 1,
                    "num_stc_panels": 2,
                    "yearly_maintenance_cost_ratio": 0.02,
                    "additional_yearly_costs": 0.0,
                    "cost_reduction": None
                },
                "output": {
                    "note": "MOCK_RESULT_OBJECT",
                    "rank": 3,
                    "net_preference_flow": 0.47272733788037513,
                    "criteria": {
                        "op_cost": 375.59080496071823,
                        "co2": 355.4703039486395,
                        "res_share": 0.9707178160937351
                    },
                    "system_sizing": {
                        "pv_power_el": 8.91246199071993,
                        "stc_power_th": 1.698618098685175,
                        "ahx_power_th": 3.5709592084512867,
                        "ghx_power_th": 7.854834340972456,
                        "bf1_capacity": 6.046393697096622,
                        "bf2_capacity": 1.6739636892417464,
                        "bf3_capacity": 3.5510721504532183
                    },
                    "output_variables": None
                }
            },
            {
                "input": {
                    "id": 2,
                    "num_pv_panels": 6,
                    "num_inverters": 1,
                    "num_stc_panels": 3,
                    "yearly_maintenance_cost_ratio": 0.02,
                    "additional_yearly_costs": 0.0,
                    "cost_reduction": None
                },
                "output": {
                    "note": "MOCK_RESULT_OBJECT",
                    "rank": 2,
                    "net_preference_flow": 0.5528986983082608,
                    "criteria": {
                        "op_cost": 220.44697883642073,
                        "co2": 419.1418217709819,
                        "res_share": 0.9053671537964653
                    },
                    "system_sizing": {
                        "pv_power_el": 0.43778186471644553,
                        "stc_power_th": 8.327858668078326,
                        "ahx_power_th": 2.4327961036551593,
                        "ghx_power_th": 0.9578221158962053,
                        "bf1_capacity": 9.341478946895567,
                        "bf2_capacity": 9.160613636822518,
                        "bf3_capacity": 5.133105963467503
                    },
                    "output_variables": None
                }
            },
            {
                "input": {
                    "id": 3,
                    "num_pv_panels": 10,
                    "num_inverters": 2,
                    "num_stc_panels": 4,
                    "yearly_maintenance_cost_ratio": 0.02,
                    "additional_yearly_costs": 0.0,
                    "cost_reduction": None
                },
                "output": {
                    "note": "MOCK_RESULT_OBJECT",
                    "rank": 1,
                    "net_preference_flow": 0.9469356324911006,
                    "criteria": {
                        "op_cost": 319.07268186926893,
                        "co2": 486.3278015357672,
                        "res_share": 0.4454151438437046
                    },
                    "system_sizing": {
                        "pv_power_el": 1.2202461317928692,
                        "stc_power_th": 8.799773197706834,
                        "ahx_power_th": 0.6466319898645168,
                        "ghx_power_th": 9.341510489010101,
                        "bf1_capacity": 0.890818260841798,
                        "bf2_capacity": 6.585093531313246,
                        "bf3_capacity": 1.1346592809762046
                    },
                    "output_variables": None
                }
            }
        ]
    }
