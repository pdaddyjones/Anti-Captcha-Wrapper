"""captcha_solver - An opinionated, minimal cookiecutter template for Python packages"""

__version__ = '0.1.0'
__author__ = 'captcha_solver <pdaddyjonesthethird@gmail.com>'
__all__ = []


from anticaptchaofficial.imagecaptcha import *

class CaptchaSolver:
    def __init__(self, api_key: str):
        self.solver = imagecaptcha()
        self.solver.set_verbose(1)
        self.solver.set_key(api_key)

    def resolve(self, image: str) -> str:
        result = self.solver.solve_and_return_solution(image)
        return result if result != 0 else f"{self.solver.error_code} - {self.solver.err_string}"
