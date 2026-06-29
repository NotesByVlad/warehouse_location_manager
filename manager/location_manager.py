import json


class LocationManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.warehouse = self.load_warehouse()

    def load_warehouse(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_warehouse(self):
        with open(self.file_path, "w") as file:
            json.dump(self.warehouse, file, indent=4)

    def find_location(self, location_code):
        aisle, column, row, slot = location_code.split("-")

        try:
            return self.warehouse["aisles"][aisle]["columns"][column]["rows"][row]["locations"][slot]
        except KeyError:
            return None

    def change_status(self, location_code, new_status):
        location = self.find_location(location_code)

        if location is None:
            return False

        location["status"] = new_status
        return True

    # Options

    def block_location(self, location_code):
        return self.change_status(location_code, "blocked")

    def unblock_location(self, location_code):
        return self.change_status(location_code, "available")
    
    def occupy_location(self, location_code):
        return self.change_status(location_code, "occupied")
    
    def free_location(self, location_code):
        return self.change_status(location_code, "available")
    
    def reserve_location(self, location_code):
        return self.change_status(location_code, "reserved")
    
    def set_maintenance(self, location_code):
        return self.change_status(location_code, "maintenance")
    