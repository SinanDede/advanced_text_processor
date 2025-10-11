from setuptools import setup, find_packages

setup(
    name="advanced_text_processor",
    version="0.2.0",
    author="Sinan Dede",
    author_email="",
    description="A built-in-only Python library for text processing and dataset manipulation.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SinanDede/advanced_text_processor",
    license="MIT",
    packages=find_packages(where="advanced_text_processor"),
    package_dir={"": "advanced_text_processor"},
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Intended Audience :: Developers",
    ],
    include_package_data=True,
    install_requires=[],  # built-in only
)
