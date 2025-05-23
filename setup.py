from setuptools import setup, find_packages

setup(
    name="black_scholes",
    version="0.1.0",
    packages=find_packages(),             # automatically finds black_scholes/
    install_requires=[],                  # any runtime deps go here
    extras_require={
        "dev": ["pytest"],                # so pip install -e .[dev] pulls pytest
    },
    entry_points={
        "console_scripts": [
            "bs-repl = black_scholes.cli:main",
        ],
    },
)