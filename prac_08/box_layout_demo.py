from kivy.app import App
from kivy.lang import Builder

# CONSTANTS
DEFAULT_GREETING = "Hello"
EMPTY_TEXT = ""

class BoxLayoutDemo(App):
    def build(self):
        """Build the root widget for the application."""
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet user by name."""
        name = self.root.ids.input_name.text.strip()
        greeting = f"{DEFAULT_GREETING} {name}" if name else DEFAULT_GREETING
        self.root.ids.output_label.text = greeting

    def handle_clear(self):
        """Clear both input and output fields."""
        self.clear_inputs()

    def clear_inputs(self):
        """Set input and label to empty strings."""
        self.root.ids.input_name.text = EMPTY_TEXT
        self.root.ids.output_label.text = EMPTY_TEXT


if __name__ == '__main__':
    BoxLayoutDemo().run()
