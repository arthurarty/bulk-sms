from utils import format_phone_number


def test_handle_phone_number():
    assert format_phone_number('780541865') == '+256780541865'
    assert format_phone_number(780541865) is None
