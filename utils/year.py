import datetime


def current_year():
    return datetime.date.today().year


""" year choices """


def year_choices():
    return [(r, r) for r in range(1950, datetime.date.today().year + 1)]

year_choices_value = year_choices()
current_year_value = current_year()