def get_zodiac_sign(day, month):
    zodiac_dates = {
        1: (21, 3),
        2: (20, 4),
        3: (21, 5),
        4: (21, 6),
        5: (23, 7),
        6: (23, 8),
        7: (23, 9),
        8: (23, 10),
        9: (22, 11),
        10: (22, 12),
        11: (20, 1),
        12: (19, 2)
    }

    zodiac_signs = {
        1: 'Aries',
        2: 'Tauro',
        3: 'Géminis',
        4: 'Cáncer',
        5: 'Leo',
        6: 'Virgo',
        7: 'Libra',
        8: 'Escorpio',
        9: 'Sagitario',
        10: 'Capricornio',
        11: 'Acuario',
        12: 'Piscis'    
    }

    for sign, (start_day, start_month) in zodiac_dates.items():
        if (month == start_month and day >= start_day) or (month == (start_month % 12) + 1 and day <= start_day):
            return zodiac_signs[sign]

def get_birthday():
    months = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    day = input("Día de nacimiento: ")
    month = input("Mes de nacimiento: ").lower()

    try:
        day = int(day)
        if day <= 0 or day > 31:
            raise ValueError("Día inválido")
    except ValueError:
        raise ValueError("Día inválido")

    try:
        if month.isdigit():
            month = int(month)
            if month <= 0 or month > 12:
                raise ValueError("Mes inválido")
        else:
            month = months[month]
    except KeyError:
        raise ValueError("Mes inválido")

    return {
        'Fecha de nacimiento': {
            'Día': day, 
            'Mes': month
        }
    }