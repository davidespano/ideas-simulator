def template_input():
    return {
        'demand': {
            'electric': template_consumption(),
            'heating': template_consumption(),
            'dhw': template_consumption(),
            'cooling': template_consumption(),
        },
        'system': {
            'general': {
                'time': {
                    '_optional': True,
                    'year': {'type': 'int', '_optional': True},
                },

                'location': {
                    'lat': {'type': 'float', 'range': '[0,360]'},
                    'lon': {'type': 'float', 'range': '[0,360]'},
                    'elev': {'type': 'float'},
                    'albedo': {'type': 'float'},
                    'surface_tilt': {'type': 'float', 'range': '[0,360]'},
                    'surface_azimuth': {'type': 'float', 'range': '[0,360]'},
                    'country': {'type': 'string', 'constr': 'ISO 3166'},
                    'tz': {'type': 'string', 'constr': 'timezone'},
                }
            },
            'pv': {
                'mount_type': {'_optional': True, 'type': 'enum', 'values': ['open_rack_glass_glass', 'close_mount_glass_glass', 'open_rack_glass_polymer', 'insulated_back_glass_polymer']},
                'module_name': {'type': 'string', '_optional': True},
                'cost_per_unit': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
                'model_params': template_pv_params(True),
            },
            'inverter': {
                'model_name': {'type': 'string', '_optional': True},
                'cost_per_unit': {'type': 'float'},
                'estimated_lifetime': {'type': 'int', '_optional': True},
                'model_params': template_inverter_params(True),
            },
            'stc': {
                'cost_per_unit': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
                'model_params': template_stc_params(True),
            },
            'bf': {
                'cost_per_liter': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
            },
            'ahx': {
                'cost_per_kW_th': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
            },
            'ghx': {
                'cost_per_kW_th': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
            },
            'hp': {
                'cost_per_kW_el': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
            },
            'pcm': {
                'cost_per_kg': {'type': 'float'},
                'estimated_lifetime': {'_optional': True, 'type': 'int'},
            },


        },
        'misc_params': {
            'financial': {
                'hourly_energy_import_tariff': {'type': 'array(float)', 'length': 24},
                'hourly_energy_generation_tariff': {'type': 'array(float)', 'length': 24},
                'hourly_energy_export_tariff': {'type': 'array(float)', 'length': 24},
                'daily_standing_charge': {'type': 'float'},
                'discount_rate': {'type': 'float'},
            },
            'carbon_intensity': {'type': 'float'},
            'criteria_weights': {
                '_optional': True,
                'op_cost': {'type': 'float', 'range': '[0,1]'},
                'co2': {'type': 'float', 'range': '[0,1]'},
                'res_share': {'type': 'float', 'range': '[0,1]'},
            }
        },
        'configurations': {
            '_optional': True,
            'type': 'array(dict)',
            'element': template_configuration(False),
            'min-length': 1
        }
    }


def template_configuration(optional):
    return {
        'id': {'type': 'int'},
        'num_pv_panels': {'type': 'float'},
        'num_inverters': {'type': 'float'},
        'num_stc_panels': {'type': 'float'},
        'yearly_maintenance_cost_ratio': {'type': 'float', 'range': '[0,1]'},
        'additional_yearly_costs': {'type': 'float'},
        'cost_reduction': {
            '_optional': True,
            'pv': {'type': 'float', 'range': '[0,1]'},
            'inverter': {'type': 'float', 'range': '[0,1]'},
            'stc': {'type': 'float', 'range': '[0,1]'},
            'bf': {'type': 'float', 'range': '[0,1]'},
            'ahx': {'type': 'float', 'range': '[0,1]'},
            'ghx': {'type': 'float', 'range': '[0,1]'},
            'hp': {'type': 'float', 'range': '[0,1]'},
        }
    }


def template_stc_params(optional):
    return {
        '_optional': optional,
        'A': {'type': 'float'},
        'lkf_lin': {'type': 'float'},
        'lkf_quad': {'type': 'float'},
        'eta_opt': {'type': 'float'},
    }


def template_inverter_params(optional):
    return {
        '_optional': optional,
        'Vac': {'type': 'float'},
        'Pso': {'type': 'float'},
        'Paco': {'type': 'float'},
        'Pdco': {'type': 'float'},
        'Vdco': {'type': 'float'},
        'C0': {'type': 'float'},
        'C1': {'type': 'float'},
        'C2': {'type': 'float'},
        'C3': {'type': 'float'},
        'Pnt': {'type': 'float'},
        'Vdcmax': {'type': 'float'},
        'Idcmax': {'type': 'float'},
        'Mppt_low': {'type': 'float'},
        'Mppt_high': {'type': 'float'},
        'CEC_Date': {'type': 'float'},
        'CEC_Type': {'type': 'float'},
    }


def template_consumption():
    return {
        'total_consumptions': {
            'yearly': {'type': 'float'},
            'monthly': {'type': 'array(float)', 'length': 12, '_optional': True},
            'daily': {'type': 'array(float)', 'length': 365, '_optional': True},
            'hourly': {'type': 'array(float)', 'length': 8760, '_optional': True},
        },

        'profiles': {
            '_optional': True,
            'monthly': {'type': 'array(float)', 'length': 12},
            'hourly': {
                'winter': {
                    'working': {'type': 'array(float)', 'length': 24},
                    'nonworking': {'type': 'array(float)', 'length': 24},
                },
                'spring': {
                    'working': {'type': 'array(float)', 'length': 24},
                    'nonworking': {'type': 'array(float)', 'length': 24},
                },
                'summer': {
                    'working': {'type': 'array(float)', 'length': 24},
                    'nonworking': {'type': 'array(float)', 'length': 24},
                },
                'fall': {
                    'working': {'type': 'array(float)', 'length': 24},
                    'nonworking': {'type': 'array(float)', 'length': 24},
                },
                'noise': {
                    '_optional': True,
                    'daily': {'type': 'float', 'range': '[0:2]'},
                    'hourly': {'type': 'float', 'range': '[0:2]'},
                }
            }
        }
    }


def template_pv_params(optional):
    return {
        '_optional': optional,
        'Vintage': {'type': 'float'},
        'Area': {'type': 'float'},
        'Material': {'type': 'float'},
        'Cells_in_Series': {'type': 'float'},
        'Parallel_Strings': {'type': 'float'},
        'Isco': {'type': 'float'},
        'Voco': {'type': 'float'},
        'Impo': {'type': 'float'},
        'Vmpo': {'type': 'float'},
        'Aisc': {'type': 'float'},
        'Aimp': {'type': 'float'},
        'C0': {'type': 'float'},
        'C1': {'type': 'float'},
        'Bvoco': {'type': 'float'},
        'Mbvoc': {'type': 'float'},
        'Bvmpo': {'type': 'float'},
        'Mbvmp': {'type': 'float'},
        'N': {'type': 'float'},
        'C2': {'type': 'float'},
        'C3': {'type': 'float'},
        'A0': {'type': 'float'},
        'A1': {'type': 'float'},
        'A2': {'type': 'float'},
        'A3': {'type': 'float'},
        'A4': {'type': 'float'},
        'B0': {'type': 'float'},
        'B1': {'type': 'float'},
        'B2': {'type': 'float'},
        'B3': {'type': 'float'},
        'B4': {'type': 'float'},
        'B5': {'type': 'float'},
        'DTC': {'type': 'float'},
        'FD': {'type': 'float'},
        'A': {'type': 'float'},
        'B': {'type': 'float'},
        'C4': {'type': 'float'},
        'C5': {'type': 'float'},
        'IXO': {'type': 'float'},
        'IXXO': {'type': 'float'},
        'C6': {'type': 'float'},
        'C7': {'type': 'float'},
        'Notes': {'type': 'string'},
    }

