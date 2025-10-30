<!-- ============================================================
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
-->
# Peano–Morton Interactive Viewer (Holmes Curve)

![Hits](https://hits.sh/github.com/sleepyprogrammer1012/Peano-Morton-Interactive-Viewer-Holmes-Curve.svg?style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/sleepyprogrammer1012/Peano-Morton-Interactive-Viewer-Holmes-Curve?style=social)
[![Star History Chart](https://api.star-history.com/svg?repos=sleepyprogrammer1012/Peano-Morton-Interactive-Viewer-Holmes-Curve)](https://star-history.com/#sleepyprogrammer1012/Peano-Morton-Interactive-Viewer-Holmes-Curve)
---

# 🚀 Project Announcement

What started as an idea this morning (10-29-2025) is now live: an interactive Python package for exploring Peano–Morton (Z‑order) curves.
In just a few hours, it went from concept → working code → polished package with CLI support and documentation.

This project brings abstract math into an interactive, visual form — useful for anyone in data visualization, GIS, graphics, or scientific computing.

Check out the repo, try the viewer, and if you find it interesting, ⭐ the project to help others discover it!

---

## ✨ Features

• 	Slider to change recursion order (1–6)

• 	Play/Pause button to animate filling the curve

• 	Auto‑centered + padded viewport

• 	Arithmetic buttons (–1, ×3, ÷3) to manipulate the current Morton index

• 	Red highlight dot that shows the current index on the curve

---

### 🚀 Getting Started

Requirements

- Python 3.8+
  
- numpy
  
- matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

Run the viewer:

```bash
# Option 1: via the CLI entry point
peano-viewer

# Option 2: as a module
python -m peano_morton_viewer
```

---

### 🧭 Command-Line Usage

Once installed (for example via `pip install -e .`), you can run the viewer directly from the terminal:

```bash
peano-viewer
```

or equivalently:

```bash
python -m peano_morton_viewer
```

#### Options

| Flag         | Description                                                       | Default |
| ------------ | ----------------------------------------------------------------- | ------- |
| `--order`    | Recursion order (curve detail level)                              | `3`     |
| `--base`     | Numeric base for Morton interleave (e.g. 2 = binary, 3 = ternary) | `3`     |
| `--interval` | Animation frame interval in **milliseconds**                      | `10`    |

#### Examples

```bash
# Display a ternary (Peano-style) curve of order 5
peano-viewer --order 5

# Explore a binary (Z-order) variant
peano-viewer --base 2 --order 6

# Slow down the animation (larger interval = slower)
peano-viewer --interval 50
```

---

## 🎮 Controls

- Slider: Adjust recursion order
   
- ▶ Play / ⏸ Pause: Animate the curve filling
  
- –1 / ×3 / ÷3: Step through Morton indices interactively
   
- Red dot: Shows the currently selected index  

---

### 📸 .gif / Demo

![demo](https://github.com/user-attachments/assets/b5077018-ada9-49bc-8e1b-e2ac2465e6b4)


---

## 📚 Why it matters
Morton (Z‑order) codes are widely used in:

• 	Spatial indexing (databases, GIS)

• 	Graphics and texture mapping

• 	Cache‑friendly data layouts

• 	Scientific computing

This viewer makes the abstract math visible and interactive.

---

## 💼 Pro / Commercial Use
This repository is a free educational demo.

For commercial licensing, advanced features, or consulting (e.g. 3D extensions, export to CAD/GIS, performance analysis), please contact me.

---

## 🛠 Roadmap

• 	[ ] 3D Peano/Morton viewer

• 	[ ] Export animations/images

• 	[ ] Highlight neighborhoods (3×3 blocks)

• 	[ ] Web‑based version

---

## 📜 License
Free for personal and educational use.
Commercial use requires a license — reach out if you’re interested. [License and Email HERE](https://github.com/sleepyprogrammer1012/Peano-Morton-Interactive-Viewer/blob/main/LICENSE.md)
