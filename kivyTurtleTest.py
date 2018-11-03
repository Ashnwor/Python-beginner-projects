# @Author: ashnwor
# @Date:   03-Nov-2018
# @Email:  ashnwor@gmail.com
# @Last modified by:   ashnwor
# @Last modified time: 03-Nov-2018
import turtle
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello motherfucker!')

TestApp().run()
