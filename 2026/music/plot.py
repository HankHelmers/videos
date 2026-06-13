from manim import *

class SineWavePeriodComparison(Scene):
    def construct(self):
        # --- TOP WAVE: 440 Hz ---
        top_axes = Axes(
            x_range=[0, 4 * PI, PI], y_range=[-1.5, 1.5, 1],
            x_length=10, y_length=2.5,
            axis_config={"include_tip": False}
        ).shift(UP * 1.8)

        top_title = Text("440 Hz (Base Period)", font_size=24, color=BLUE)
        top_title.next_to(top_axes, UP, buff=0.3)

        top_wave = top_axes.plot(lambda x: np.sin(2 * x), color=BLUE, x_range=[0, 4 * PI])

        # --- BOTTOM WAVE: 880 Hz ---
        bottom_axes = Axes(
            x_range=[0, 4 * PI, PI], y_range=[-1.5, 1.5, 1],
            x_length=10, y_length=2.5,
            axis_config={"include_tip": False}
        ).shift(DOWN * 1.8)

        bottom_title = Text("880 Hz (Double Frequency / Half Period)", font_size=24, color=RED)
        bottom_title.next_to(bottom_axes, UP, buff=0.3)

        bottom_wave = bottom_axes.plot(lambda x: np.sin(4 * x), color=RED, x_range=[0, 4 * PI])

        # --- PERIOD INDICATORS ---
        # The period of sin(2x) is PI. Let's draw indicators at x = PI.
        # This is where 440Hz completes 1 cycle, and 880Hz completes exactly 2 cycles.
        
        # 1. Vertical alignment line connecting top and bottom graphs
        start_pt = top_axes.c2p(PI, 0)
        end_pt = bottom_axes.c2p(PI, 0)
        alignment_line = DashedLine(start_pt, end_pt, color=YELLOW, stroke_width=4)
        
        # 2. Highlight braces to mark the physical length of the periods
        top_brace = BraceBetweenPoints(top_axes.c2p(0, -1), top_axes.c2p(PI, -1), direction=DOWN, color=BLUE_A)
        top_brace_text = top_brace.get_text("1 Full Period").scale(0.6)
        
        bottom_brace = BraceBetweenPoints(bottom_axes.c2p(0, -1), bottom_axes.c2p(PI, -1), direction=DOWN, color=RED_A)
        bottom_brace_text = bottom_brace.get_text("2 Full Periods").scale(0.6)

        # --- ANIMATION SEQUENCE ---
        # Setup axes
        self.play(Create(top_axes), Create(bottom_axes), Write(top_title), Write(bottom_title))
        self.wait(0.5)

        # Draw waves
        self.play(
            Create(top_wave, run_time=3, rate_func=linear),
        )
        self.wait(0.5)
        self.play(
            Create(bottom_wave, run_time=3, rate_func=linear),
        )

        # Drop the vertical alignment line to show the mathematical intersection
        self.play(Create(alignment_line), run_time=1)
        self.play(FadeOut(bottom_title))  # Remove the line after showing it
        self.play(Flash(alignment_line, color=YELLOW, flash_radius=0.5))
        self.wait(0.5)

        # Show the braces demonstrating how the periods measure out spatially
        self.play(
            GrowFromCenter(top_brace), FadeIn(top_brace_text),
            GrowFromCenter(bottom_brace), FadeIn(bottom_brace_text)
        )
        
        self.wait(3)