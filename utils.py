def format_phone_number(phone_number):
    if not isinstance(phone_number, str):
        return None
    if len(phone_number) < 9:
        return None
    if len(phone_number) == 9:
        return f'+256{phone_number}'
    return phone_number
