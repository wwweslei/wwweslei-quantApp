from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantAPP",
    version="0.1.0",
    description="Financial asset management application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author_email="www.weslei@gmail.com",
    url="https://github.com/wwweslei/wwweslei-quantApp",
    include_package_data=True,
    license="MIT License",
    platforms="Windows/Linux",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Windows/Linux",
    ],
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)
