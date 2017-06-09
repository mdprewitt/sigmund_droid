#!/usr/bin/env python3

import time, random
import ev3dev.ev3 as ev3

random.seed( time.time() )


class ev3rstorm:
    def __init__(self):

        self.screen = ev3.Screen()

        self.draw_face()


    def draw_face(self):
        w,h = self.screen.shape
        y = h // 2

        eye_xrad = 20
        eye_yrad = 30

        pup_xrad = 10
        pup_yrad = 10

        def draw_eye(x):
            self.screen.draw.ellipse((x-eye_xrad, y-eye_yrad, x+eye_xrad, y+eye_yrad))
            self.screen.draw.ellipse((x-pup_xrad, y-pup_yrad, x+pup_xrad, y+pup_yrad), fill='black')

        draw_eye(w//3)
        draw_eye(2*w//3)

        self.screen.update()


if __name__ == '__main__':
    Droid = ev3rstorm()
    ev3.Sound.speak('Hello, I am sigmund droid, please follow me').wait()
