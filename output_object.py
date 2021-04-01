def template_output():
    return {
        'id': {'type': 'int'},
        'configurations': {
            '_optional': True,
            'type': 'array(dict)',
            'element': template_configuration(),
            'min-length': 1
        }
    }


def template_configuration():
    return {
        'input': {
            'id': {'type': 'int'},
            'num_pv_panels': {'type': 'float'},
            'num_inverters': {'type': 'float'},
            'num_stc_panels': {'type': 'float'},
            'yearly_maintenance_cost_ratio': {'type': 'float'},
            'cost_reduction': {
                '_optional': None,
                'pv': {'type': 'float'},
                'inverter': {'type': 'float'},
                'stc': {'type': 'float'},
                'bf': {'type': 'float'},
                'ahx': {'type': 'float'},
                'ghx': {'type': 'float'},
                'hp': {'type': 'float'},
            }
        },
        'output': {
            'note': {'type': 'string'},
            'rank': {'type': 'int'},
            'net_preference_flow': {'type': 'float'},
            'criteria': {
                'op_cost': {'type': 'float'},
                'co2': {'type': 'float'},
                'res_share': {'type': 'float'},
            },
            'system_sizing': {
                'pv_power_el': {'type': 'float'},
                'stc_power_th': {'type': 'float'},
                'ahx_power_th': {'type': 'float'},
                'ghx_power_th': {'type': 'float'},
                'bf1_capacity': {'type': 'float'},
                'bf2_capacity': {'type': 'float'},
                'bf3_capacity': {'type': 'float'},
            }
        }
    }

