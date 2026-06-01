from manim import *

class AnimatedSquareToCricle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )

class CreateCircleSquare(Scene):
    def construct(self):
        circle = Circle()  
        circle.set_fill(PINK, opacity=0.4)
        
        square=Square()
        square.set_fill(BLUE, opacity=0.5)
        
        square.next_to(circle, RIGHT, buff=0.5)
        
        self.play(Create(circle), Create(square))
        