from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.bubble import Button
from kivy.uix.textinput import TextInput


class KivySum(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # label
        self.window.add_widget(
            Label(text="Calculator", font_size=40, color="#ffcc00")
        )

        # inputs
        self.x = TextInput(
            multiline=False, padding_y=(2, 2), size_hint=(1, 0.5), font_size=30
        )
        self.window.add_widget(self.x)
        self.y = TextInput(
            multiline=False, padding_y=(2, 2), size_hint=(1, 0.5), font_size=30
        )
        self.window.add_widget(self.y)

        # result label
        self.result = Label(text="", font_size=40, color="ffcc00")
        self.window.add_widget(self.result)

        # Buttons
        calcula = Button(
            text="Calcula",
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00FFCE"
        )
        calcula.bind(on_press=self.calcula)
        self.window.add_widget(calcula)

        sair = Button(
            text="Sair",
            size_hint=(0.5, 0.5)
        )
        sair.bind(on_press=self.stop)
        self.window.add_widget(sair)

        return self.window

    def calcula(self, instance):
        self.result.text = str(int(self.x.text) + int(self.y.text))


if __name__ == "__main__":
    KivySum().run()
