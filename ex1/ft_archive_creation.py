#!/usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        file = open("ew_discovery.txt", "w+")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.\n")
        return None
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    data = ["[ENTRY 001] New quantum algorithm discovered\n",
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainee\n"]
    for line in data:
        file.write(line)

    print("Storage unit created successfully...")
    file.seek(0)
    das = file.read()
    print(f"{das}")
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
