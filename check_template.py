def check_field(input_object, field, path):
    res = ok()

    if input_object is None:
        if '_optional' not in field or field['_optional'] is False:
            return error("The mandatory field '{}' is missing".format(path.removesuffix('.')))
        else:
            return ok()

    if 'type' in field:
        res = check_type(input_object, field, path)
    else:
        for k, v in enumerate(field):
            if not (type(input_object) is dict):
                return error("The field '{}' must be an object".format(path.removesuffix('.')))
            if v is not '_optional':
                res = check_field(input_object.get(v), field[v], path+v+'.')

            if res['valid'] is not True:
                return res
    return res


def check_type(input_object, field, path):

    switcher = {
        'int': check_int,
        'string': check_string,
        'float': check_float,
        'array(int)': check_array_int,
        'array(float)': check_array_float,
        'array(string)': check_array_string,
        'array(dict)': check_array_dict,
        'enum': check_enum,
    }
    if not(field['type'] in switcher):
        return error("Field {}. Undefined type: {}".format(path, field.type))
    else:
        return switcher[field['type']](input_object, field, path.removesuffix('.'))


def check_range(v, r, path):
    lim = r.split(',')
    if len(lim) == 2:
        lim[0] = lim[0].replace('[', '')
        lim[1] = lim[1].replace(']', '')
        try:
            up = float(lim[0])
            dn = float(lim[1])
            if up <= v <= dn:
                return ok()
            else:
                return error('The value {} of the field {} is not in the {} range'.format(
                    v, path, r
                ))
        except ValueError:
            return error("Invalid range definition in template for field {}: {}".format(path, r))
    return error("Invalid range definition in template for field {}: {}".format(path, r))


def check_int(input_object, field, path):
    if not(type(input_object) is int):
        return error("The field {} must be an integer".format(path))
    if 'range' in field:
        res = check_range(input_object, field['range'], path)
        if res['valid'] is False:
            return res
    return ok()


def check_float(input_object, field, path):
    if not(type(input_object) is float) and not(type(input_object) is int):
        return error("The field {} must be a float".format(path))
    if 'range' in field:
        res = check_range(input_object, field['range'], path)
        if res['valid'] is False:
            return res
    return ok()


def check_string(input_object, field, path):
    if not(type(input_object) is str):
        return error("The field {} must be a string".format(path))
    # TODO: iso3166, timezone
    return ok()


def check_array_int(input_object, field, path):
    return check_array(input_object, field, path, int)


def check_array_float(input_object, field, path):
    return check_array(input_object, field, path, float)


def check_array_string(input_object, field, path):
    return check_array(input_object, field, path, str)


def check_array_dict(input_object, field, path):
    if not isinstance(input_object, list):
        return error('The field {} is not an {}'.format(path, field['type']))
    if 'min-length' in field and field['min-length'] > len(input_object):
        return error('The {} array length is {}, expected more than {} '.format(path, len(input_object), field['min-length']))
    for i in range(0, len(input_object)):
        res = check_field(input_object[i], field['element'], path + '[{}].'.format(str(i)))
        if not res['valid']:
            return res

    return ok()


def check_array(input_object, field, path, t):
    if not isinstance(input_object, list):
        return error('The field {} is not an {}'.format(path, field['type']))
    fl = t is float
    for i in range(0, len(input_object)):
        if (not isinstance(input_object[i], t)) and (fl and not isinstance(input_object[i], int)):
            return error('The element at index {} in the {} array is not a {}'.format(str(i), path, str(t)))
    if 'length' in field and field['length'] is not len(input_object):
        return error('The {} array length is {}, expected {} '.format(path, len(input_object), field['length']))
    if 'min-length' in field and field['min-length'] > len(input_object):
        return error('The {} array length is {}, expected more than {} '.format(path, len(input_object), field['min-length']))
    return ok()


def check_enum(input_object, field, path):
    # TODO: to be implemented
    return ok()


def error(descr):
    return {
        'valid': False,
        'description': descr
    }


def ok():
    return {
        'valid': True,
        'description': 'Ok'
    }


