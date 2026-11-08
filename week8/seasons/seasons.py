from datetime import date
import inflect
import operator
import sys

def check_date():
    try:
        date_birth = input("Date birth: ")
        return date.fromisoformat(date_birth)
    except ValueError:
        sys.exit("Invalid date")

def minutes_convert(date_birth, today):
    difference = operator.sub(today, date_birth)
    return difference.days * 24 * 60

def minutes_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="")


def main():
    valid_date_birth = check_date()
    minutes = minutes_convert(valid_date_birth, date.today())
    minutes_words = minutes_to_words(minutes)
    print(f"{minutes_words.capitalize()} minutes")

if __name__ == "__main__":
    main()
