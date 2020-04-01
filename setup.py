import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'pronounce',
    version = '1.0.0',
    author="Vishal Kumar",
    author_email="vtkumar022@gmail.com",
    description = 'Generate the pronunciation code for the string',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vish0709/pronounce/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
