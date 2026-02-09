
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

def main():
    print(sample_bay[0])

    print(sample_bay[-1])

    print(len(sample_bay))

    for i in sample_bay:
        print(f"Transmitting data for: [{i}]")
    
    new_findings = []
    for i in range(3):
        new_sample = input("Please input a rock:")
        new_findings.append(new_sample)

    print(new_findings)
    try:
        index = sample_bay.index("Dust")
        sample_bay.remove(index)
    except:
        print("Dust was not found in the sample bay")
    print(sample_bay)


if __name__ == "__main__":
    main()