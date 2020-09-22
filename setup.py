import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="img-renamer",
    version="0.0.1",
    author="Charles Samuel R",
    author_email="rcharles.samuel99@gmail.com",
    description="A package to convert and rename different images to the same format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charlescsr/img-renamer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
