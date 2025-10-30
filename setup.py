from setuptools import setup, find_packages

setup(
    name="peano-morton-viewer",
    version="0.1.0",
    description="Interactive viewer for ternary (or generalized base-N) Morton / Peano interleaving",
    author="Your Name",
    author_email="your.email@example.com",
    license="Proprietary (non-commercial use only, see LICENSE.md)",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.8",
)
