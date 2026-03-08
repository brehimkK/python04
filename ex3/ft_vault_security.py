#!/usr/bin/env python3

def main() -> int:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")

    with open("test.txt", "r") as file:
        data = file.read()
    print(f"{data}")
    print("\nSECURE PRESERVATION:")
    with open("test.txt", "w") as file:
        lista = ["[CLASSIFIED] New security protocols archived",
                 "Vault automatically sealed upon completion"]
        for line in lista:
            file.write(line)
            file.write("\n")

    for line in lista:
        print(line)

    print("\nAll vault operations completed with maximum security.")
    return 0


if __name__ == "__main__":
    main()