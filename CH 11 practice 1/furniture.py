class OfficeFurniture:

    def __init__(self, category, material, length, width, height, price):
        self.category = category
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = price

    def __str__(self):
        return f"Category: {self.category}\n" \
               f"Material: {self.material}\n" \
               f"Length: {self.length} feet\n" \
               f"Width: {self.width} feet\n" \
               f"Height: {self.height} feet\n" \
               f"Price: ${self.price}"
