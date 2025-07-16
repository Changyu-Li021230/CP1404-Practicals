from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SquaringWidget(BoxLayout):
    """Main widget for the squaring app."""
    pass


class SquaringApp(App):
    """App to square a number entered by the user."""

    def build(self):
        """Build the root widget."""
        return SquaringWidget()

    def handle_calculate(self, input_text):
        """
        Try to convert input to an integer and square it.
        If invalid, display an error message.
        """
        try:
            number = int(input_text.strip())
            squared = number * number
            self.root.ids.result_label.text = f"Result: {squared}"
        except ValueError:
            self.root.ids.result_label.text = "Error: Please enter a valid integer!"


if __name__ == '__main__':
    SquaringApp().run()
