import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sapio_DSS",
    version="0.0.0",
    author="Kritik Seth",
    author_email="sethkritik@gmail.com",
    description="Data ETL for Sapio Covid-19 DSS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kritik-seth/CovidDSS.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
