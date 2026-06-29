from manager.location_manager import LocationManager


DATA_FILE = "data/warehouse_locations.json"


def main():
    manager = LocationManager(DATA_FILE)

    while True:
        print("\nWarehouse Location Manager")
        print("1. Find location")
        print("2. Block location")
        print("3. Unblock location")
        print("4. Occupy location")
        print("5. Free location")
        print("6. Reserve location")
        print("7. Set maintenance")
        print("8. Save")
        print("9. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            location_code = input("Location code: ")
            location = manager.find_location(location_code)
            print(location if location else "Location not found.")

        elif choice == "2":
            location_code = input("Location code: ")
            print("Blocked." if manager.block_location(location_code) else "Location not found.")

        elif choice == "3":
            location_code = input("Location code: ")
            print("Unblocked." if manager.unblock_location(location_code) else "Location not found.")

        elif choice == "4":
            location_code = input("Location code: ")
            print("Occupied." if manager.occupy_location(location_code) else "Location not found.")

        elif choice == "5":
            location_code = input("Location code: ")
            print("Freed." if manager.free_location(location_code) else "Location not found.")

        elif choice == "6":
            location_code = input("Location code: ")
            print("Reserved." if manager.reserve_location(location_code) else "Location not found.")

        elif choice == "7":
            location_code = input("Location code: ")
            print("Set to maintenance." if manager.set_maintenance(location_code) else "Location not found.")

        elif choice == "8":
            manager.save_warehouse()
            print("Saved.")

        elif choice == "9":
            manager.save_warehouse()
            print("Saved. Exiting.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()