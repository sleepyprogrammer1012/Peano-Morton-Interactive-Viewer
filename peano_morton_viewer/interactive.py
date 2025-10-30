# peano_morton_viewer/interactive.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib import animation

# import or define your helper functions here:
# - peano_morton_coords
# - morton_subtract
# - morton_multiply
# - morton_divide
# (make sure they’re either in this file or imported from another module)

def interactive_peano(base: int = 3, max_order: int = 6, interval: int = 10):
    """
    Launch an interactive Peano–Morton viewer with:
      - Order slider
      - Play/Pause animation
      - Arithmetic buttons to manipulate Morton index
    """
    # your full interactive_peano implementation goes here
    # (the version we cleaned up earlier with highlight dot, buttons, etc.)
    ...
# peano_morton_viewer/__init__.py

from .interactive import interactive_peano

__all__ = ["interactive_peano"]



# ==============================================================
#  Peano / Morton coordinate generator
# ==============================================================

def peano_morton_coords(order: int, base: int = 3):
    """
    Generate (x, y) coordinates using base-N Morton (Peano-like) interleaving.
    """
    m = order
    N = base ** m
    total = N * N
    coords = np.zeros((total, 2), dtype=int)

    for d in range(total):
        t = d
        x = 0
        y = 0
        scale = 1
        for _ in range(m):
            rx = t % base
            t //= base
            ry = t % base
            t //= base
            x += rx * scale
            y += ry * scale
            scale *= base
        coords[d] = (x, y)

    return coords, N

# ==============================================================
#  Morton index arithmetic operations
# ==============================================================

def morton_subtract(d: int, k: int) -> int:
    """Subtract k from Morton index d."""
    return d - k

def morton_multiply(d: int, f: int) -> int:
    """Multiply Morton index d by factor f."""
    return d * f

def morton_divide(d: int, f: int) -> int:
    """Divide Morton index d by divisor f (integer division)."""
    return d // f

# ==============================================================
#  Interactive + animated viewer
# ==============================================================

def interactive_peano(base: int = 3, max_order: int = 6, interval: int = 10):
    """
    Interactive Peano–Morton viewer with:
      - Order slider
      - Play/Pause animation
      - Arithmetic buttons (–1, ×3, ÷3) to move a red highlight dot
    """
    order = 3
    coords, N = peano_morton_coords(order, base)
    pts = (coords + 0.5) / N
    colors = np.linspace(0, 1, len(pts))

    fig, ax = plt.subplots(figsize=(7, 7), facecolor="black")
    plt.subplots_adjust(bottom=0.35)  # leave space for buttons
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.axis("off")

    pad = 0.02
    ax.set_xlim(-pad, 1 + pad)
    ax.set_ylim(-pad, 1 + pad)

    line, = ax.plot([], [], lw=0.6, color="white", alpha=0.5)
    scatter = ax.scatter([], [], s=0.8, c=[], cmap="hsv", alpha=0.9)
    title = ax.set_title(
        f"Base-{base} Morton / Peano Interleave (order={order})",
        color="white", pad=12
    )

    # Slider
    ax_slider = plt.axes([0.25, 0.12, 0.5, 0.03])
    slider = Slider(ax_slider, 'Order', 1, max_order, valinit=order, valstep=1)

    # Play button
    ax_play = plt.axes([0.82, 0.12, 0.1, 0.04])
    btn_play = Button(ax_play, "Play", color="#202020", hovercolor="#303030")
    anim_running = [False]
    ani = [None]

    # Highlight dot
    highlight, = ax.plot([], [], 'ro', markersize=6)
    selected_index = [0]

    def update_highlight(d):
        """Move red dot and update curve up to index d."""
        n = int(slider.val)
        coords, N = peano_morton_coords(n, base)
        pts_local = (coords + 0.5) / N
        cols_local = np.linspace(0, 1, len(pts_local))
        total = len(coords)
        d = max(0, min(d, total - 1))
        selected_index[0] = d
        x, y = pts_local[d]
        highlight.set_data([x], [y])
        # show curve up to this index
        line.set_data(pts_local[:d+1, 0], pts_local[:d+1, 1])
        scatter.set_offsets(pts_local[:d+1])
        scatter.set_array(cols_local[:d+1])
        title.set_text(f"Base-{base} Morton / Peano Interleave (order={n}) | d={d}")
        fig.canvas.draw_idle()

    # Arithmetic buttons
    ax_sub = plt.axes([0.1, 0.02, 0.1, 0.05])
    btn_sub = Button(ax_sub, "–1", color="#202020", hovercolor="#303030")
    btn_sub.on_clicked(lambda event: update_highlight(morton_subtract(selected_index[0], 1)))

    ax_mul = plt.axes([0.25, 0.02, 0.1, 0.05])
    btn_mul = Button(ax_mul, "×3", color="#202020", hovercolor="#303030")
    btn_mul.on_clicked(lambda event: update_highlight(morton_multiply(selected_index[0], 3)))

    ax_div = plt.axes([0.40, 0.02, 0.1, 0.05])
    btn_div = Button(ax_div, "÷3", color="#202020", hovercolor="#303030")
    btn_div.on_clicked(lambda event: update_highlight(morton_divide(selected_index[0], 3)))

    # Update when order changes
    def update_order(n):
        coords, N = peano_morton_coords(int(n), base)
        pts_local = (coords + 0.5) / N
        cols_local = np.linspace(0, 1, len(pts_local))
        line.set_data(pts_local[:, 0], pts_local[:, 1])
        scatter.set_offsets(pts_local)
        scatter.set_array(cols_local)
        update_highlight(selected_index[0])
        return pts_local, cols_local

    pts, colors = update_order(order)

    slider.on_changed(lambda val: update_order(val))

    # Animation
    def animate_fill(i):
        segment = pts[:i+1]
        line.set_data(segment[:, 0], segment[:, 1])
        scatter.set_offsets(segment)
        scatter.set_array(colors[:i])
        return line, scatter, highlight

    def toggle(event):
        nonlocal pts, colors
        if anim_running[0]:
            # Pause
            if ani[0] is not None and ani[0].event_source is not None:
                ani[0].event_source.stop()
            ani[0] = None
            btn_play.label.set_text("Play")
            anim_running[0] = False
        else:
            # Play
            n = int(slider.val)
            coords, N = peano_morton_coords(n, base)
            pts = (coords + 0.5) / N
            colors = np.linspace(0, 1, len(pts))
            ani[0] = animation.FuncAnimation(
                fig, animate_fill, frames=len(pts),
                interval=interval, blit=True, repeat=False
            )
            btn_play.label.set_text("Pause")
            anim_running[0] = True
        fig.canvas.draw_idle()

    btn_play.on_clicked(toggle)

    plt.show()


# ==============================================================
#  Run
# ==============================================================

if __name__ == "__main__":
    # --- quick demo of arithmetic helpers ---
    d = 45
    print(morton_subtract(d, 5))   # → 40
    print(morton_multiply(d, 3))   # → 135
    print(morton_divide(d, 4))     # → 11

    # --- launch the interactive viewer ---
    interactive_peano(base=3, max_order=6, interval=2)

