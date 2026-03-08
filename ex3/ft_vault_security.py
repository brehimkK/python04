#!/usr/bin/env python3

def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\nSECURE EXTRACTION:\n")
    with open("test.txt", "r+") as file:
        data = file.read()
        print(f"{data}")
        list = ["[CLASSIFIED] New security protocols archived",
                "Vault automatically sealed upon completion"]
        for line in list:
            file.write(line)
            file.write("\n")
        dataa = file.read()
        print(f"{dataa}")


main()