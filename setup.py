from setuptools import setup, find_packages

setup(
    name = "django-prove",
    version = "0.1",
    author = "Rob Berry",
    author_email = "",
    url = "http://github.com/rob-b/django-prove/",

    packages = find_packages('prove'),
    license = "MIT License",
    keywords = "django testing",
    description = "A few custom asserts for testing",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ]
)
