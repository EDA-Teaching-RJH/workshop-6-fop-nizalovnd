def main():
    rover_status = {
        "Battery":100,
        "Heater":"Off",
        "Camera":"Standby"
    }
    print(rover_status["Battery"])

    rover_status["Battery"] = 85
    rover_status["Heater"] = "On"
    rover_status["Speed"] = 5

    print(rover_status)

    mission_log = []
    mission_log.append({"Site": "Crater A", "Radiation": "Low", "Water": False})
    mission_log.append({"Site": "Dune B", "Radiation": "High", "Water": True})
    for item in mission_log:
        print(f"Site [{item["Site"]}] has [{item["Radiation"]} radiation]")

if __name__ == "__main__":
    main()