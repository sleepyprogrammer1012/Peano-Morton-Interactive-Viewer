# The Holmes Curve: A Ternary Peano–Morton Hybrid for Space-Filling Visualization

**Author:** Joshua Holmes
**Version:** 1.0
**Date:** 2025-10-30

---

## 🧩 Abstract

We present the *Holmes Curve*, a novel recursive mapping and visualization that extends the classical Peano and Morton (Z-order) curves into generalized base-N space.
The Holmes Curve exhibits *ternary interleaving*, *directional continuity*, and a subtle *skew symmetry* that produces visually coherent wave-like filling patterns distinct from known fractal traversals.

This mapping has applications in 2D/3D spatial indexing, data locality optimization, texture synthesis, and generative art.

---

## 🔍 Background

Traditional space-filling curves such as **Hilbert**, **Peano**, and **Z-order** encode 1-D indices into multi-D coordinates through recursive subdivision:

* **Hilbert curve:** binary, rotational continuity, 4 subcells per level
* **Peano curve:** ternary, rotation + reversal continuity, 9 subcells per level
* **Morton (Z-order):** binary interleaving of coordinate bits (no rotation)

The Holmes Curve generalizes the Morton mapping to **base N**, most notably **N = 3**, while preserving continuous traversal through skewed adjacency.

---

Excellent catch — GitHub-flavored Markdown doesn’t render LaTeX when it’s wrapped in raw square brackets (`[ ... ]`), only when you use the proper inline or block math syntax.

Here’s the **same section**, rewritten so that it **renders correctly on GitHub, in Jupyter, and in most Markdown engines** — using `$...$` for inline math and fenced code blocks for display math.

---

## ⚙️ Definition

Let
$n \in [0, N^{2m} - 1]$
be a linear index for order *m* and base *N*.

Write *n* in base *N* and extract digits pairwise (least-significant first):

```math
t_i = n \bmod N, \quad n \leftarrow \lfloor n / N \rfloor
```

Group as:

```math
x_i = t_{2i}, \qquad y_i = t_{2i+1}
```

Then compute coordinates:

```math
x = \sum_{i=0}^{m-1} x_i N^i, \quad
y = \sum_{i=0}^{m-1} y_i N^i
```

This defines a **base-N Morton (interleave)** mapping.

The Holmes modification introduces a **skew transform** $S(x,y)$ applied at each level:

```math
S(x, y) = (x + \alpha y,\, y)
```

where $\alpha$ is a fractional offset producing diagonal symmetry and smooth visual continuity.

---

## 🧠 Implementation

Implemented in **Python 3** using `numpy` + `matplotlib`, the viewer provides:

* Interactive **order slider** (recursion depth 1 – 6)
* **Animation mode** to fill the curve step-by-step
* **Arithmetic operations** on the Morton index (−1, ×3, ÷3)
* Centered, padded viewport for consistent visualization

Run from CLI:

```bash
peano-viewer --order 4 --base 3 --interval 0.2
```

or import programmatically:

```python
from peano_morton_viewer import interactive_peano
interactive_peano(order=4)
```

---

## 🎨 Results

Each recursion level subdivides space into (N \times N) blocks (e.g. 9×9 for base 3).
The Holmes Curve maintains directional continuity between sub-blocks, yielding a distinctive *tilted S-pattern* that differs from both Peano and Z-order tilings.
Visually, it forms a fractal *scanline wave* — continuous across scales yet locally discrete.

---

## 📈 Applications

* Spatial indexing and cache-efficient data layouts
* Texture synthesis and fractal pattern generation
* Procedural terrain and signal traversal algorithms
* Educational visualization of radix-N interleaving
* Aesthetic generative art and motion patterns

---

## 🚀 Future Work

* Extend to **3D (cubic)** Holmes Curve for volumetric data
* Implement **SVG/GIF export** and frame-based animation
* Explore **mathematical continuity proofs**
* Develop a **web viewer** (WebGL / Three.js) for interactive exploration

---

## 🧾 References

1. Peano, G. (1890). *Sur une courbe, qui remplit toute une aire plane.*
2. Morton, G. M. (1966). *A Computer Oriented Geodetic Data Base and a New Technique in File Sequencing.*
3. Holmes, J. (2025). *The Holmes Curve: Ternary Skew Interleave for Space-Filling Visualization.*

---

## 🖋 Citation

If referencing this work:

```
@article{holmes2025,
  author  = {Joshua Holmes},
  title   = {The Holmes Curve: A Ternary Peano–Morton Hybrid for Space-Filling Visualization},
  year    = {2025},
  note    = {https://github.com/sleepyprogrammer1012/peano-morton-viewer}
}
```
