class Circle:
    def __init__(self, radii):
        """
        Constructor to initialize the Circle with a list of radii.

        :param radii: List of radii
        """
        self._radii = radii  # Private member variable for radii
        self.__pi = 3.141  # Private variable for π

    def area(self, radius):
        """
        Calculate the area of the circle with the given radius.

        :param radius: Radius of the circle
        :return: Area of the circle
        """
        return self.__pi * (radius ** 2)

    def perimeter(self, radius):
        """
        Calculate the perimeter (circumference) of the circle with the given radius.

        :param radius: Radius of the circle
        :return: Perimeter of the circle
        """
        return 2 * self.__pi * radius

    def calculate_areas_and_perimeters(self):
        """
        Calculate areas and perimeters for all radii in the list.

        :return: List of tuples containing (radius, area, perimeter)
        """
        results = []
        for radius in self._radii:
            area = self.area(radius)
            perimeter = self.perimeter(radius)
            results.append((radius, area, perimeter))
        return results


# Example usage
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)

# Calculate and print areas and perimeters
results = circle.calculate_areas_and_perimeters()
for radius, area, perimeter in results:
    print(f"Radius: {radius}, Area: {area:.2f}, Perimeter: {perimeter:.2f}")
