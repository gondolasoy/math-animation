from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        #self.play(Transform(square, circle))  # interpolate the square into the circle
        #self.play(FadeOut(square))  # fade out animation

class ThreeCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        #circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        circle2 = Circle()  # create a square
        #circle2.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        circle3 = Circle()  # create a square
        #circle3.set_fill(GREEN, opacity=0.5)  # set the color and transparency

        circle2.next_to(circle, RIGHT, buff=0.5)  # set the position
        circle3.next_to(circle, LEFT, buff=0.5)

        self.play(circle.animate.set_fill(PINK, opacity=0.5))
        self.play(circle2.animate.set_fill(BLUE, opacity=0.5))  
        self.play(circle3.animate.set_fill(GREEN, opacity=0.5))  # set the color and transparency
        
        # show the shapes on screen