from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        """
        Build the root widget for the application.
        """
        self.names = ['Alice', 'Bob', 'Charlie', 'David']
        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):
        """
        Called automatically when the app starts.
        Add a Label for each name in the list.
        """
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
