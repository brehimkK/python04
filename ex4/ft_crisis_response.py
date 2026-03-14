#!/usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as file:
            data = file.read()
            print(f"{data}")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as file:
            file.write("45")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            file.read()
        print("SUCCESS: Archive recovered -"
              "``Knowledge preserved for humanity''")
        print("STATUS: Normal operations resumed")

        print("\nAll crisis scenarios handled successfully. Archives secure.")
    except Exception:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    main()
