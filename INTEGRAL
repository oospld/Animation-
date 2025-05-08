#%%manim -pqh -v WARNING TheMathBossQ

config.media_dir = "/content"
class TheMathBossQ(Scene):
    def construct(self):
        #Creat à title with animation and color
        title = Text("Variations of Integral", font_size=71, gradient=(PURPLE,RED))
        title.to_edge(UP)

        #The bottom text
        bottom_text = Text("INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        bottom_text.next_to(title, DOWN*1.7, buff=0.5)

        # The symbol of Integral
        integral = MathTex(r"\int",font_size = 96, color=RED)
        integral.next_to(bottom_text, DOWN*2, buff=0.5)

        #The Double Integral Texte
        double_intehral_bottom_text = Text("DOUBLE INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        double_intehral_bottom_text.next_to(title, DOWN*1.7, buff=0.5)

        #The double integral symbol
        double_integral = MathTex(r"\int\!\!\int",font_size = 96, color=RED)
        integral.next_to(double_intehral_bottom_text, DOWN*2, buff=0.5)

        #The Triple Integral Text
        triple_integral_bottom_text = Text("TRIPLE INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        triple_integral_bottom_text.next_to(title, DOWN*1.7, buff=0.5)

        #The triple integral symbol
        triple_integral = MathTex(r"\int\!\!\int\!\int",font_size = 96, color=RED)
        integral.next_to(triple_integral_bottom_text, DOWN*2, buff=0.5)

        #The Contour Integral Text
        contour_integral_bottom_text = Text("CONTOUR INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        contour_integral_bottom_text.next_to(title, DOWN*1.7, buff=0.5)

        #The contour integral symbol
        contour_integral = MathTex(r"\oint",font_size = 96, color=RED)
        integral.next_to(contour_integral_bottom_text, DOWN*2, buff=0.5)

        #The Surface Integral Text
        surface_integral_bottom_text = Text("SURFACE INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        surface_integral_bottom_text.next_to(title, DOWN*1.7, buff=0.5)


        #The surface integral symbol
        surface_integral = MathTex(r"\int\!\!\int",font_size = 96, color=RED)
        circle_overlay = Ellipse(width=1.5, height=0.7, color=RED)
        circle_overlay.move_to(double_integral)

        #Add the circle overlay to the surface integral symbol 
        surface_integral_symbol = VGroup(double_integral, circle_overlay)
        surface_integral_symbol.next_to(surface_integral_bottom_text, DOWN*2, buff=0.5)
        
        #The Volume Integral Text 
        volume_integral_bottom_text = Text("VOLUME INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        volume_integral_bottom_text.next_to(title, DOWN*1.7, buff=0.5)

        #The volume integral symbol
        volume_integral = MathTex(r"\int\!\!\int\!\int",font_size = 96, color=RED)
        circle_overlay = Ellipse(width=3, height=0.7, color=RED)
        circle_overlay.move_to(triple_integral)
        
        #Add the circle overlay to the volume integral symbol
        volume_integral_symbol = VGroup(triple_integral, circle_overlay)
        volume_integral_symbol.next_to(volume_integral_bottom_text, DOWN*2, buff=0.5)

        #The surface integral symbol
        #surface_integral = MathTex(r"\oiint_{\Sigma}",font_size = 96, color=RED)
        #integral.next_to(surface_integral_bottom_text,DOWN*2, buff=0.5)

        #The Quadruple Integral Text
        quadruple_integral_bottom_text = Text("QUADRUPLE INTEGRAL", font_size=48, gradient=(PURPLE,RED))
        quadruple_integral_bottom_text.next_to(title, DOWN*1.7, buff=0.5)

        #The quadruple integral symbol
        quadruple_integral = MathTex(r"\int\!\!\int\!\!\int\!\!\int",font_size = 96, color=RED)
        integral.next_to(quadruple_integral_bottom_text, DOWN*2, buff=0.5)

        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(bottom_text, shift = UP))
        self.play(FadeIn(integral))

        self.wait(0.5)
        self.play(
            Transform(integral, double_integral),
            Transform(bottom_text,  double_intehral_bottom_text),                       
        )
        self.wait(0.5)

        self.play(
            Transform(integral, triple_integral),
            Transform(bottom_text,  triple_integral_bottom_text),
        )
        self.wait(0.5)

        self.play(
            Transform(integral,contour_integral),
            Transform(bottom_text,  contour_integral_bottom_text),
        )
        self.wait(0.5)

        self.play(
            Transform(integral, surface_integral_symbol),
            Transform(bottom_text,  surface_integral_bottom_text),
        ) 
        self.wait(0.5)
