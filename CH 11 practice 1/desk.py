from furniture import OfficeFurniture


class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_drawers):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.location_of_drawers = location_of_drawers
        self.number_of_drawers = number_drawers

    def __str__(self):
        temp = super().__str__()
        temp += f"\nLocation of drawers: {self.location_of_drawers}\n" \
                f"Number of drawers: {self.number_of_drawers}"
        return temp
