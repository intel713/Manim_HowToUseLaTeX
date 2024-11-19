from manim import *

def GenerateImage(self, title_text, input_text, text_scale, tex_scale):
    self.camera.background_color = "#FFFFFF"
    title = Text('<' + title_text + '>', font = "Batang", weight = BOLD).move_to([0, 2.71, 0]).set_color(BLACK)
    down_arr = MathTex("\\Downarrow").move_to([0, -0.4, 0]).set_color(BLACK).scale(2)
    text = Text(input_text, font = "Noto Sans").move_to([0, 1, 0]).scale(text_scale)
    latex = MathTex(input_text).move_to([0, -2, 0]).scale(tex_scale)
    math = VGroup(text, latex).set_color(BLACK)
    self.add(title, down_arr, math)

class HowToUseLaTeX(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        LaTeX = SVGMobject("media/LaTeX_logo.svg").set_color(WHITE).scale(0.5)
        text = MathTex("\\mathrm{How\\ to\\ use}").scale(2)
        title = VGroup(text.shift(3.5*LEFT), LaTeX.shift(0.75*RIGHT + 0.09*DOWN))
        title.move_to(ORIGIN).scale(1.4).set_color(BLACK)

        madeby = MathTex("\\mathrm{Made \\ by}").scale(1.2).set_color(BLACK)
        instagram_id = MathTex("\\mathrm{@shun400hz}").scale(1.2)
        instagram_id.set_color_by_gradient("#FA7E1E", "#D62976", "#962FBF", "#4F5BD5")
        manim = MathTex("\\mathbb{M}\\mathrm{anim}").scale(1.2).set_color_by_gradient(GREEN_D, TEAL_D, BLUE_D)
        wt = MathTex("\\mathrm{with}").scale(1.2).set_color(BLACK)
        author = VGroup(madeby.shift(5*LEFT), instagram_id.shift(2.1*LEFT), wt.shift(0.2*RIGHT), manim.shift(1.88*RIGHT))
        author.move_to(ORIGIN)

        self.add(title.shift(UP), author.shift(2.3*RIGHT + 3.4*DOWN))

class CubicFunction(Scene):
    def construct(self):
        title_txt = "삼차함수"
        input_txt = "f(x) = x^{3} + 3x^{2} - 4x + 2"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)
        

class QuadraticFormula(Scene):
    def construct(self):
        title_txt = "이차방정식의 근의 공식"
        input_txt = "x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class EulersFormula(Scene):
    def construct(self):
        title_txt = "오일러 공식"
        input_txt = "e^{i\\theta} = \\cos \\theta + i\\sin \\theta"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class Calculus(Scene):
    def construct(self):
        title_txt = "미적분학의 기본정리"
        input_txt = "g'(x) = \\frac{\\rm d}{{\\rm d}x} \\int_a^x f(t) \\,{\\rm d}t = f(x)"
        GenerateImage(self, title_txt, input_txt, 0.8, 1.3)

class Operators(Scene):
    def construct(self):
        title_txt = "기본 기호"
        input_txt = "+ - \\times \\div = \\neq < \\le > \\ge \\cdot"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class TrigonometriFcunction(Scene):
    def construct(self):
        title_txt = "삼각함수"
        input_txt = "\\sin 30^\\circ = \\cos \\frac{\\pi}{3}, \\sec^2 x"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class ExpLog(Scene):
    def construct(self):
        title_txt = "지수와 로그"
        input_txt = "\\sqrt[3]{2^4} = 2^{\\frac{4}{3}}, \\log_{3} 81 = 4}"
        GenerateImage(self, title_txt, input_txt, 0.9, 1.5)

class Matrix(Scene):
    def construct(self):
        title_txt = "행렬"
        input_txt = "\\begin{bmatrix} 1 & a \\\\ b & -5 \\end{bmatrix}"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class Set(Scene):
    def construct(self):
        title_txt = "집합"
        input_txt = "\\{3, e, \\pi\\} \\varnothing \\in \\ni \\notin \\cap \\cup"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class AmGmInequality(Scene):
    def construct(self):
        title_txt = "산술평균과 기하평균의 관계"
        input_txt = "\\frac{a + b}{2} \\ge \\sqrt{ab}"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class Factorization(Scene):
    def construct(self):
        title_txt = "인수분해"
        input_txt = "x^3 - 8 = (x - 2)(x^2 + 2x + 4)"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class CaseDiv(Scene):
    def construct(self):
        title_txt = "경우 나누기"
        input_txt = "f(n) = \\begin{cases} 1 & (n = 0) \\\\ -1 & (n \\neq 0) \\end{cases}"
        GenerateImage(self, title_txt, input_txt, 0.75, 1.5)

class SumLim(Scene):
    def construct(self):
        title_txt = "수열의 합과 극한"
        input_txt = "\\lim_{n\\to\\infty}\\sum_{k=1}^{n}{a_k}"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)

class DifferentialCoefficient(Scene):
    def construct(self):
        title_txt = "미분계수"
        input_txt = "f'(x) = \\lim_{h \\to 0}\\frac{f(x + h) - f(x)}{h}"
        GenerateImage(self, title_txt, input_txt, 1, 1.5)