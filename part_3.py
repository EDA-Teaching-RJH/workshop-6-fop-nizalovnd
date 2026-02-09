def main():
    try:
        motor_speed = int(input("Enter Motor Speed:"))
    except ValueError as e:
        print("Error: Corrupted Signal. Maintaining current speed.")

    x_coordinate = get_coordinate()


def get_coordinate():
    while True:
        try:
            x = int(input("Enter the X coordinate:"))
        except ValueError:
            print("Invalid Coordinate")
            continue
        if x > 100 or x < -100:
            print("Coordinate out of range")
            continue
        break
    return x

if __name__ == "__main__":
    main()
