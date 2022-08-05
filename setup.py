import os

from setuptools import find_packages, setup

# get setup.py file path.
__here__ = os.path.abspath(os.path.dirname(__file__))


# get the long description from the README file
with open(os.path.join(__here__, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='inplus',
    version='0.0.1',
    description='efficient input methods.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='kedarr',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords='inplus, input, input methods, input methods for python',
    url='https://github.com/kedarrio/inplus',
    license='MIT',
    packages=["inplus"],
    package_dir={"": "src"},
    python_requires = '>=3.10'
)
