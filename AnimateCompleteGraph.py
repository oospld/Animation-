from manim import *
%%manim -qh -v WARNING AnimateCompleteGraph
class AnimateCompleteGraph(Scene):
    def construct(self):
        max_n = 30 #The value of n.
        radius = 2.5

        for n in range(3, max_n + 1):
            self.clear()

            # Title
            title = MathTex(f"n = {n}").to_edge(UP)
            self.play(Write(title))

            # Create dots
            dots = []
            for i in range(n):
                angle = 2 * PI * i / n
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                dot = Dot(point=[x, y, 0], color=GREEN) 
                dots.append(dot)
                self.add(dot)

            # Draw edges (complete graph)
            edges = []
            for i in range(n):
                for j in range(i + 1, n):
                    edge = Line(dots[i].get_center(), dots[j].get_center(), stroke_color=WHITE, stroke_opacity=0.3)
                    edges.append(edge)

            self.play(*[Create(edge) for edge in edges], run_time=1)
            self.wait(1)
