from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934  # Conversion factor from miles to kilometers


class MilesConverterApp(App):
    def build(self):
        """
        Build the root widget for the application.
        """
        Window.size = (700, 350)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """
        Handle the conversion from miles to kilometers.
        """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = f"{result:.2f}"

    def handle_increment(self, change):
        """
        Adjust the miles input by a given increment and update the result.
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        Get the validated float value from the miles input field.
        If invalid input is given, return 0.
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesConverterApp().run()
