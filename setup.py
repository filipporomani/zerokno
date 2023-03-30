from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='zerokno',
    version='1.0.0',
    description='ZeroKno is a lightweight zero-knowledge password storage library for Python 3.7+',
    py_modules=["zerokno"],
    package_dir={'': 'zerokno'},
    extras_require={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Filippo Romani",
    author_email="mail@filipporomani.it",
    url="https://github.com/filipporomani/zerokno"
)