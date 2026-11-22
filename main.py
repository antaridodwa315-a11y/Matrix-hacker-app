
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp

class MatrixHacker(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 1)
        self.cols = 0
        self.rows = 0
        self.screen = []

        self.display = Label(
            text="",
            markup=True,
            font_size=dp(14),
            font_name="Roboto",
            halign="center",
            valign="middle"
        )
        self.add_widget(self.display)
        self.bind(size=self.resize, pos=self.resize)
        Clock.schedule_interval(self.update, 0.05)

    def resize(self, *args):
        self.display.size = self.size
        self.display.pos = self.pos
        self.display.text_size = self.size
        self.cols = max(20, int(self.width / dp(9)))
        self.rows = max(10, int(self.height / dp(19)))
        self.screen = [
            [random.choice(["0", "1", " "])
             for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def update(self, dt):
        if not self.cols or not self.rows:
            return

        self.screen.pop(0)
        self.screen.append([
            random.choice(["0", "1", " "])
            for _ in range(self.cols)
        ])

        mid = self.rows // 2
        message = "YOU ARE NOW HACKED"
        lines = []

        for r, row in enumerate(self.screen):
            line = "".join(row)

            if r == mid:
                left = max(0, (self.cols - len(message)) // 2)
                right = max(0, self.cols - left - len(message))
                line = (
                    " " * left +
                    "[color=ffffff][b]" + message +
                    "[/b][/color]" +
                    " " * right
                )
            elif r in (mid - 1, mid + 1):
                line = " " * self.cols

            lines.append(line)

        self.display.text = (
            "[color=00ff00]" +
            "\n".join(lines) +
            "[/color]"
        )

class MatrixApp(App):
    def build(self):
        self.title = "Matrix Hacker Simulator"
        return MatrixHacker()

if __name__ == "__main__":
    MatrixApp().run()
  
