class WarehouseStatistics:
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def count_total_aisles(self):
        return len(self.warehouse["aisles"])

    def count_total_columns(self):
        total = 0

        for aisle_data in self.warehouse["aisles"].values():
            total += len(aisle_data["columns"])

        return total

    def count_total_rows(self):
        total = 0

        for aisle_data in self.warehouse["aisles"].values():
            for column_data in aisle_data["columns"].values():
                total += len(column_data["rows"])

        return total

    def count_total_locations(self):
        total = 0

        for aisle_data in self.warehouse["aisles"].values():
            for column_data in aisle_data["columns"].values():
                for row_data in column_data["rows"].values():
                    total += len(row_data["locations"])

        return total

    def count_locations_by_status(self):
        status_counts = {}

        for aisle_data in self.warehouse["aisles"].values():
            for column_data in aisle_data["columns"].values():
                for row_data in column_data["rows"].values():
                    for location_data in row_data["locations"].values():
                        status = location_data["status"]

                        if status not in status_counts:
                            status_counts[status] = 0

                        status_counts[status] += 1

        return status_counts

    def count_locations_by_aisle(self):
        aisle_counts = {}

        for aisle, aisle_data in self.warehouse["aisles"].items():
            total = 0

            for column_data in aisle_data["columns"].values():
                for row_data in column_data["rows"].values():
                    total += len(row_data["locations"])

            aisle_counts[aisle] = total

        return aisle_counts

    def print_summary(self):
        total_locations = self.count_total_locations()
        status_counts = self.count_locations_by_status()
        aisle_counts = self.count_locations_by_aisle()

        print("\n========= Warehouse Statistics =========")
        print(f"Total aisles:     {self.count_total_aisles()}")
        print(f"Total columns:    {self.count_total_columns()}")
        print(f"Total rows:       {self.count_total_rows()}")
        print(f"Total locations:  {total_locations}")

        print("\nLocations by status")
        print("-------------------")

        for status, count in status_counts.items():
            percentage = (count / total_locations) * 100 if total_locations > 0 else 0
            print(f"{status.capitalize():<12}: {count} ({percentage:.2f}%)")

        print("\nLocations by aisle")
        print("------------------")

        for aisle, count in aisle_counts.items():
            print(f"Aisle {aisle}: {count}")

        print("========================================\n")