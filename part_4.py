def rover_angle():
    travel_log = []
    while True:
        s_angle = input("Sensor Reading (Slope Angle):")
        try:
            s_angle = int(s_angle)
        except ValueError:
            print("Sensor Glitch")
            continue
        if s_angle > 45:
            print("CRITICAL TILT! HALTING.")
            break
        travel_log.append(s_angle)
        print("Path Stable. Moving forward.")
    print("Mission Terminated")
    print(f"Total steps taken: {len(travel_log)}")
    print(travel_log)

if __name__ == "__main__":
    rover_angle()