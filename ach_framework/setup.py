from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ach-framework",
    version="1.0.0",
    author="Simone Souza dos Reis",
    author_email="simone.souzareis@email.com",
    description="A Python package for detecting Anomalous Cosmic Homogeneity in cosmological datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simonereis/ach-framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.5.0",
        "matplotlib>=3.3.0",
    ],
)
