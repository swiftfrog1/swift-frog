from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime, timedelta


class CalcDate(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #self.window.size_hint = (0.4, 0.3)
        self.window.poshint = {"center_x": 0.5, "center_y": 0.5}

        self.banner = Label(
            text="EXIT DATE CALCULATOR",
            font_size=48,
            bold=True
        )
        self.window.add_widget(self.banner)

        # add widgets to window
        self.getdate = Label(
            text="Enter contract expiration date (MM/DD/YYY): ",
            font_size=26,
        )
        self.window.add_widget(self.getdate)

        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5),
            halign="center",
            font_size=26
        )
        self.window.add_widget(self.user)

        self.button = Button(
            text="CALCULATE",
            size_hint=(1, 0.5),
            bold=True,
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        date = self.user.text
        try:
            date = datetime.strptime(date, '%m/%d/%Y')
            exit_date = date - timedelta(days=21)
            exit_date = exit_date.strftime('%m/%d/%Y')
            self.getdate.text = "Exit Date: {}".format(exit_date)
        except ValueError:
            self.getdate.text = "{} is not a valid date! Enter date (MM/DD/YYYY): ".format(
                date)
            self.user.text = ""


if __name__ == "__main__":
    CalcDate().run()
