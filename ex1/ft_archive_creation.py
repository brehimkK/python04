#!/usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    file = open("new_discovery.txt", "w")

    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    data = ["[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"]

    for line in data:
        file.write(line + "\n")
        print(f"{line}")

    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
