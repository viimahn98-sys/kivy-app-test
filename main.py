from kivy.app import App
from kivy.uix.button import Button

class HelloWorldApp(App):
    def build(self):
        # Displays a full-screen button that says Hello World
        return Button(text="Hello World from my Phone!")

if __name__ == "__main__":
    HelloWorldApp().run()
