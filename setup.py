import setuptools

with open("README.rst", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="<indic-num2words>", # Replace with your username

    version="1.0.0",

    author="<authorname>",

    author_email="<authorname@indic-num2words.com>",

    description="<Template Setup.py package>",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="<https://github.com/Maksolo27/indic-num2words>",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)