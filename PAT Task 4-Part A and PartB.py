class TV:
    def __init__(self, brand):
        """
        Initialize the TV with a brand, default channel, volume, and power status.

        :param brand: Brand of the TV
        """
        self.brand = brand
        self.channel = 1  # Default channel is 1
        self.volume = 50  # Default volume is 50
        self.on_off_status = False  # TV is initially off
        self.inches = 0  # Default inches, can be set in subclasses

    def turn_on(self):
        """Turn the TV on."""
        self.on_off_status = True

    def turn_off(self):
        """Turn the TV off."""
        self.on_off_status = False

    def increase_volume(self):
        """Increase the volume by 1, ensuring it doesn't exceed 100."""
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume cannot exceed 100.")

    def decrease_volume(self):
        """Decrease the volume by 1, ensuring it doesn't go below 0."""
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume cannot go below 0.")

    def set_channel(self, channel):
        """
        Set the channel to a specified number if within the range of 1-50.

        :param channel: The channel number to set
        """
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            print(f"Channel {channel} is out of range. Staying at channel {self.channel}.")

    def reset_tv(self):
        """Reset the TV to channel 1 and volume 50."""
        self.channel = 1
        self.volume = 50

    def status(self):
        """Return the current status of the TV."""
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


# Example usage of the TV class
tv = TV("Panasonic")
tv.turn_on()
tv.set_channel(8)
tv.increase_volume()
print(tv.status())  # Output: Panasonic at channel 8, volume 51
tv.reset_tv()
print(tv.status())  # Output: Panasonic at channel 1, volume 50


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        """
        Initialize the LED TV with additional properties.

        :param brand: Brand of the TV
        :param screen_thickness: Thickness of the screen in mm
        :param energy_usage: Energy usage in Watts
        :param lifespan: Lifespan of the TV in hours
        :param refresh_rate: Refresh rate in Hz
        """
        super().__init__(brand)  # Call the constructor of the base class
        self.screen_thickness = screen_thickness  # in mm
        self.energy_usage = energy_usage  # in Watts
        self.lifespan = lifespan  # in hours
        self.refresh_rate = refresh_rate  # in Hz

    def viewing_angle(self):
        """Return the viewing angle of the LED TV."""
        return "Viewing angle for LED TV is 178 degrees."

    def backlight(self):
        """Return information about the backlight feature."""
        return "This LED TV has a dynamic backlight feature."

    def display_details(self):
        """Display detailed features of the LED TV."""
        details = (f"LED TV Details:\n"
                   f"Brand: {self.brand}\n"
                   f"Screen Thickness: {self.screen_thickness} mm\n"
                   f"Energy Usage: {self.energy_usage} Watts\n"
                   f"Lifespan: {self.lifespan} hours\n"
                   f"Refresh Rate: {self.refresh_rate} Hz")
        return details


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        """
        Initialize the Plasma TV with additional properties.

        :param brand: Brand of the TV
        :param screen_thickness: Thickness of the screen in mm
        :param energy_usage: Energy usage in Watts
        :param lifespan: Lifespan of the TV in hours
        :param refresh_rate: Refresh rate in Hz
        """
        super().__init__(brand)  # Call the constructor of the base class
        self.screen_thickness = screen_thickness  # in mm
        self.energy_usage = energy_usage  # in Watts
        self.lifespan = lifespan  # in hours
        self.refresh_rate = refresh_rate  # in Hz

    def viewing_angle(self):
        """Return the viewing angle of the Plasma TV."""
        return "Viewing angle for Plasma TV is 180 degrees."

    def backlight(self):
        """Return information about the backlight feature."""
        return "This Plasma TV uses an ambient light sensing backlight."

    def display_details(self):
        """Display detailed features of the Plasma TV."""
        details = (f"Plasma TV Details:\n"
                   f"Brand: {self.brand}\n"
                   f"Screen Thickness: {self.screen_thickness} mm\n"
                   f"Energy Usage: {self.energy_usage} Watts\n"
                   f"Lifespan: {self.lifespan} hours\n"
                   f"Refresh Rate: {self.refresh_rate} Hz")
        return details


# Example usage of LedTV and PlasmaTV classes
led_tv = LedTV("Samsung", 25, 100, 60000, 120)
plasma_tv = PlasmaTV("LG", 50, 150, 50000, 60)

print(led_tv.display_details())
print(plasma_tv.display_details())
