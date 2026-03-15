length_units = {
    "mm": 10,
    "cm": 1,
    "m": 0.01,
    "km": 0.00001,
    "in": 0.393701,
    "ft": 0.0328084,
    "yd": 0.0109361,
    "mi": 0.0000062137,
}


def convert_length(value, from_unit, to_unit):
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid length unit")

    # Convert the value to centimeters
    value_in_cm = value / length_units[from_unit]

    # Convert the value from centimeters to the target unit
    converted_value = value_in_cm * length_units[to_unit]

    return converted_value


weight_units = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "oz": 0.035274,
    "lb": 0.00220462,
}


def convert_weight(value, from_unit, to_unit):
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid weight unit")

    # Convert the value to grams
    value_in_g = value / weight_units[from_unit]

    # Convert the value from grams to the target unit
    converted_value = value_in_g * weight_units[to_unit]

    return converted_value


temperature_to_c = {
    "C": lambda x: x,
    "F": lambda x: (x - 32) * 5.0 / 9.0,
    "K": lambda x: x - 273.15,
}

temperature_from_c = {
    "C": lambda x: x,
    "F": lambda x: (x * 9.0 / 5.0) + 32,
    "K": lambda x: x + 273.15,
}


def convert_temperature(value, from_unit, to_unit):
    if from_unit not in temperature_to_c or to_unit not in temperature_from_c:
        raise ValueError("Invalid temperature unit")

    # Convert the value to the target unit
    value_in_c = temperature_to_c[from_unit](value)
    converted_value = temperature_from_c[to_unit](value_in_c)

    return converted_value
