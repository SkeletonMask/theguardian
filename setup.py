from setuptools import setup, find_packages

setup(
    name="theguardian",  
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
    ],
    python_requires='>=3.9',
)
