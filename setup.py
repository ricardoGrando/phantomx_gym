import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gym_phantomx",
    version="0.1.0",
    author="Ricardo Bedin Grando",
    author_email="ricardo.bedin@utec.edu.uy",
    description="Gym environment for phantomx hexapod",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ricardoGrando/phantomx_gym",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['gym']
)
