# ============================================================
#  Peano–Morton Interactive Viewer (Holmes Curve Visualization)
#  Copyright (c) 2025 Joshua Holmes
#  All rights reserved.
#
#  License:
#    - Free for personal, educational, and research use.
#    - Commercial use requires an explicit license agreement.
#
#  Description:
#    Interactive Python tool for exploring Peano–Morton interleaving
#    and the Holmes Curve, a ternary skewed space-filling traversal.
#
#  Author: Joshua Holmes
#  Repository: https://github.com/<your-github-handle>/peano-morton-viewer
# ============================================================

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
