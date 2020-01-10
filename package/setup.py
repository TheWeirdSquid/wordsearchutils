import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordsearchutils-TheWeirdSquid", # Replace with your own username
    version="1.1",
    author="David Bootle",
    author_email="davidtbootle@gmail.com",
    description="A library to solve word searches.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheWeirdSquid/wordsearchutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)