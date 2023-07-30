# Creating Car class
class Car:
    # Initializing Car class with input of 1 row of data frame
    def __init__(self, data):
        # Extracting parameters from data frame passed and setting values of Car object parameters
        self.nickname = "none"
        self.aspiration = data['aspiration']
        self.body_style = data['body-style']
        self.bore = data['bore']
        self.city_mpg = data['city-mpg']
        self.compression_ratio = data['compression-ratio']
        self.curb_weight = data['curb-weight']
        self.drive_wheels = data['drive-wheels']
        self.engine_location = data['engine-location']
        self.engine_size = data['engine-size']
        self.engine_type = data['engine-type']
        self.fuel_system = data['fuel-system']
        self.fuel_type = data['fuel-type']
        self.height = data['height']
        self.highway_mpg = data['highway-mpg']
        self.horsepower = data['horsepower']
        self.length = data['length']
        self.make = data['make']
        self.normalized_losses = data['normalized-losses']
        self.num_of_cylinders = data['num-of-cylinders']
        self.num_of_doors = data['num-of-doors']
        self.peak_rpm = data['peak-rpm']
        self.price = data['price']
        self.stroke = data['stroke']
        self.symboling = data['symboling']
        self.wheel_base = data['wheel-base']
        self.width = data['width']