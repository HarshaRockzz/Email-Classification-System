from setuptools import setup, find_packages

setup(
    name="email-classification-system",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open("requirements.txt")
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Advanced email classification system with PII masking",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)