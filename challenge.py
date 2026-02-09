command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",    # Corrupted: 'five' is text, not a number
    "DIG",
    "MOVE 20",
    "XÆA-12",       # Corrupted: Unknown command
    "RETURN",
    "MOVE 15"
]

def main():
    rover_state = {"x": 0, "y": 0, "samples": 0}
    for item in command_batch:
        parts = item.split(" ")
        if parts[0] == "MOVE":
            try:
                new_y = int(parts[1])
            except ValueError:
                print("Error: Invalid distance ignored")
                continue
            rover_state["y"] += new_y

        elif parts[0] == "DIG":
            rover_state["samples"] += 1
        
        elif parts[0] == "TURN":
            print("Turning...")
        else:
            print("Error: Unknown command sequence")
            continue
    print(rover_state)

if __name__ == "__main__":
    main()