def main():
    status = {"Power": 100, "Samples": 0}
    inventory = []
    while True:
        print("a. Dig for Sample \n")
        print("b. Report Status \n")
        print("c. Emergency Stop \n")

        option = input("Please choose menu option:")
        match option:
            case "a":
                sample_name = input("Enter sample name:")
                inventory.append(sample_name)
                status["Power"] -= 10
                status["Samples"] += 1

            case "b":
                print(status)
                print(inventory)
            case "c":
                break
            
            case _:
                print("Invalid option entered")
            
if __name__ == "__main__":
    main()