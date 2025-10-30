# Peano–Morton Interactive Viewer

---

An interactive Python tool for exploring ternary (or generalized base‑N) Morton / Peano interleaving.
It lets you visualize space‑filling curves, step through indices, and experiment with arithmetic operations on Morton codes.

---

## ✨ Features

• 	Slider to change recursion order (1–6)

• 	Play/Pause button to animate filling the curve

• 	Auto‑centered + padded viewport

• 	Arithmetic buttons (–1, ×3, ÷3) to manipulate the current Morton index

• 	Red highlight dot that shows the current index on the curve

---

## 🚀 Getting Started

Requirements

• 	Python 3.8+

• 	numpy

• 	matplotlib

---

Install dependencies:

```
pip install numpy matplotlib
```

Run: 

```
python peano_morton_fill_centered.py
```

---
Absolutely 👍 — here’s a clean, copy-paste-ready **CLI usage section** you can drop straight into your `README.md` (right after the “Run” section if you’d like):

---

## 🧭 Command-Line Usage

Once installed (for example via `pip install -e .`), you can run the viewer directly from the terminal:

```bash
peano-viewer
```

or, equivalently:

```bash
python -m peano_morton_viewer
```

### Options

You can adjust curve parameters using flags:

```bash
peano-viewer --order 4 --base 3 --interval 0.5
```

**Arguments:**

| Flag         | Description                                                       | Default |
| ------------ | ----------------------------------------------------------------- | ------- |
| `--order`    | Recursion order (curve detail level)                              | `3`     |
| `--base`     | Numeric base for Morton interleave (e.g. 2 = binary, 3 = ternary) | `3`     |
| `--interval` | Animation frame interval (seconds)                                | `0.2`   |

**Examples**

```bash
# Display a ternary (Peano-style) curve of order 5
peano-viewer --order 5

# Explore a binary (Z-order) variant
peano-viewer --base 2 --order 6

# Watch it fill the grid at half-speed
peano-viewer --interval 0.5
```

---

## 🎮 Controls

• 	Slider: Adjust recursion order

• 	▶ Play / ⏸ Pause: Animate the curve filling

• 	–1 / ×3 / ÷3: Step through Morton indices interactively

• 	Red dot: Shows the currently selected index

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
Commercial use requires a license — reach out if you’re interested.
