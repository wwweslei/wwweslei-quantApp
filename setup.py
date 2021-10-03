from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantAPP",
    version="1.0.0",
    description="Financial asset management application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="www.weslei@gmail.com",
    url="https://github.com/wwweslei/wwweslei-quantApp",
    license="MIT License",
    platforms="Windows/Linux",
    packages=find_packages(exclude=[".venv", "test", "test\\", "test_*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Windows/Linux",
    ],
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)
