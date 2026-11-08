def main():
    time = input("What time is it? ")
    time_conv = convert(time)

    if 7.00 <= time_conv <= 8.00:
        print("breakfast time")
    elif 12.00 <= time_conv <= 13.00:
        print("lunch time")
    elif 18.00 <= time_conv <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(':')
    convert_time = float(hours) + (float(minutes) / 60)
    return convert_time

if __name__ == "__main__":
    main()
