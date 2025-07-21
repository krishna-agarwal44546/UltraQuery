from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="UltraQuery",
    version="0.0.7",  # ⬅️ bump version every time you re-upload
    author="Mayank Chaudhary, Krishna Agarwal, Abhedhya Faujdar",
    author_email="mayankchaudhary92197@gmail.com, krishnaiit7@gmail.com, fabhedhya@gmail.com",
    description="A fast CSV reader and CLI plotter tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krishna-agarwal44546/UltraQuery",  # ⬅️ Update this if you have a GitHub repo
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "matplotlib",
        "typer",
        "prompt_toolkit",
    ],
    entry_points={
        'console_scripts': [
            'ultraquery=ultraquery.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
