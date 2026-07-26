from datetime import datetime, date


def prepare_excel_value(value):
    if value is None:
        return None

    if isinstance(value, (datetime, date)):
        return value

    if isinstance(value, str):
        value = value.strip()

        try:
            if value.isdigit():
                return int(value)
        except Exception:
            pass

        try:
            return float(value)
        except ValueError:
            pass

    return value


if __name__ == '__main__':
    pass
