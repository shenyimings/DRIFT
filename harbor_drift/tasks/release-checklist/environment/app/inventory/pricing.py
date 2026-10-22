def apply_discount(price, percent):
    """Return price reduced by `percent` (0-100), rounded to cents."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def line_total(price, qty, percent=0):
    return round(apply_discount(price, percent) * qty, 2)
