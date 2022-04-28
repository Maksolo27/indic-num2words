import setuptools

with open("README.rst", "r") as fh:

    long_description = fh.read()

def find_version(fname):
    """Parse file & return version number matching 0.0.1 regex
    Returns str or raises RuntimeError
    """
    version = ''
    with open(fname, 'r', encoding="utf-8") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

setuptools.setup(

    name="<indic-num2words>",

    version="0.1",

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
