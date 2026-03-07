#!/usr/bin/env python3
def main() -> int:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt\n")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        data = file.read()
        print("RECOVERED DATA:")
        print(f"{data}")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")
    return 0


if __name__ == "__main__":
    main()
