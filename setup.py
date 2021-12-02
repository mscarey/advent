import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="advent",
    version="0.0.1",
    author="Matt",
    author_email="matt@authorityspoke.com",
    description="Advent of Code 2021 solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mscarey/advent",
    project_urls={
        "Bug Tracker": "https://github.com/mscarey/advent/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
