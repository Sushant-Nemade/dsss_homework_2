from setuptools import setup, find_packages

setup (
    name="dsss_homework_2",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.math_quiz:math_quiz',
        ]
    }
)