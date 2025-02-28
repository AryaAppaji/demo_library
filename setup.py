from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    author="Arya Appaji",
    author_email="your.email@example.com",
    description="A package containing basic math and string operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AryaAppaji/demo_library",  # Update with your actual repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
