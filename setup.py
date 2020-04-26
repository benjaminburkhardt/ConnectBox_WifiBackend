""" Set up script """
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "README.md"), "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="connectBoxWifi",
    version="1.0",
    author="Benjamin Burkhardt",
    author_email="-",
    description="ConnectBox Wifi Toggler",
    long_description_content_type="text/markdown",
    long_description=long_descr,
    url="https://github.com/benjaminburkhardt/compal_CH7465LG_py",
    entry_points={},
    install_requires=["requests", "lxml"],
    include_package_data=True,
    python_requires=">=3.7",
    license="MIT",
    keywords="unitymedia connectbox wifi connect box cablemodem",
    packages=find_packages(exclude=["examples", "tests", "tests.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
    ],
)
