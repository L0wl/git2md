from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="git2md",
    version="1.1.0",
    description="Convert Git repository contents to Markdown format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Michael",
    author_email="x30827pos@gmail.com",
    url="https://github.com/xpos587/git2md",
    packages=find_packages(),
    # install_requires=["pathspec>=0.12.1", "nbconvert>=7.16.4", "pymupdf4llm>=0.0.17"],
    entry_points={
        "console_scripts": [
            "git2md=src.git2md:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
    python_requires=">=3.12",
    include_package_data=True,
    package_data={
        "src": ["*.globalignore"],
    },
)
