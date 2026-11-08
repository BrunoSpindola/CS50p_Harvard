from datetime import date
import pytest

from seasons import check_date, minutes_convert, minutes_to_words


# minutes_convert
def test_minutes_one_year():
    assert minutes_convert(date(2025, 10, 26), date(2026, 10, 26)) == 525600


def test_minutes_two_years():
    assert minutes_convert(date(2024, 10, 26), date(2026, 10, 26)) == 1051200


def test_minutes_one_day():
    assert minutes_convert(date(2026, 10, 25), date(2026, 10, 26)) == 1440


def test_minutes_same_day():
    assert minutes_convert(date(2026, 10, 26), date(2026, 10, 26)) == 0


def test_minutes_leap_year():
    assert minutes_convert(date(2024, 2, 28), date(2024, 3, 1)) == 2 * 1440
    assert minutes_convert(date(2023, 2, 28), date(2023, 3, 1)) == 1 * 1440


# minutes_to_words
def test_words_one_year():
    assert minutes_to_words(525600) == "five hundred twenty-five thousand, six hundred"


def test_words_one_day():
    assert minutes_to_words(1440) == "one thousand, four hundred forty"


def test_words_zero():
    assert minutes_to_words(0) == "zero"


def test_words_no_and():
    assert " and " not in minutes_to_words(1051200)


# check_date
def test_check_date_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2000-01-01")
    assert check_date() == date(2000, 1, 1)


@pytest.mark.parametrize("entrada", [
    "January 1, 2000",
    "01/01/2000",
    "2026-02-30",
    "2026-13-01",
    "",
    "cat",
])

def test_check_date_invalid(monkeypatch, entrada):
    monkeypatch.setattr("builtins.input", lambda _: entrada)
    with pytest.raises(SystemExit):
        check_date()
