# Artistic Mandelbrot Fractal Renderer

A Python script that renders a high-resolution, deep-zoom view of the **Mandelbrot set** with a simulated **3D metallic lighting effect**, producing a striking piece of generative art rather than a plain escape-time plot.

## What It Does

The script zooms into a narrow region of the Mandelbrot set near one of its classic spiral boundaries and computes, for each pixel, how quickly the corresponding complex point escapes to infinity under iteration.

The escape data is then treated as a **height field** and lit like a 3D surface, giving the final image a sense of depth and metallic sheen instead of flat banded coloring.

## How It Works

### 1. Coordinate Grid

A grid of complex numbers `C` is built over a tight window:

```text
x: -0.7452 to -0.7432
y:  0.1122 to  0.1134
```

This region is chosen for its intricate spiral detail.

### 2. Escape-Time Iteration

For up to `max_iter` steps, each point is updated using the Mandelbrot recurrence:

```text
Z = Z² + C
```

Only points that have not yet escaped (`|Z| <= 2.0`) continue iterating. This keeps the computation efficient as more points escape over time.

### 3. Smooth Coloring

Instead of storing a plain integer iteration count, which produces visible color banding, the script computes a continuous smoothed iteration value using the classic potential formula:

```text
i + 1 - log2(log(|Z|))
```

This value is stored in `smooth_iter` and provides a smoother surface for the final rendering.

### 4. Noise Reduction

A light Gaussian blur with `sigma=0.5` is applied to the iteration field to reduce small pixel-level artifacts.

### 5. Bump-Mapped Lighting

The `smooth_iter` field is treated as a height map. Its gradients (`dx`, `dy`) are calculated to derive a surface normal at every pixel, as if the fractal were a physical relief surface.

A fixed light direction is then used to calculate:

* **Diffuse shading** — determines how directly each surface point faces the light.
* **Specular highlight** — creates a sharp, metallic-looking glint using `diffuse^16`.

### 6. Compositing

The final brightness map combines the raw escape potential with the lighting terms using the following weights:

| Component          | Weight |
| ------------------ | -----: |
| Escape potential   | `0.75` |
| Diffuse lighting   | `25.0` |
| Specular highlight | `50.0` |

This produces a rich, high-contrast metallic appearance.

### 7. Rendering

The result is displayed with Matplotlib using the `magma` colormap, which complements the metallic lighting effect.

The rendering uses:

* **200 DPI**
* No axes
* No padding
* Full-frame fractal composition

## Parameters

| Parameter  | Description                              | Default |
| ---------- | ---------------------------------------- | ------: |
| `width`    | Output image width in pixels             |  `1600` |
| `height`   | Output image height in pixels            |  `1000` |
| `max_iter` | Maximum escape-time iterations per point |   `400` |

## Requirements

The project requires:

* Python 3.x
* NumPy
* Matplotlib
* SciPy

Install the required dependencies with:

```bash
pip install numpy matplotlib scipy
```

## Usage

Run the script directly:

```bash
python fractal_render.py
```

A Matplotlib window will display the rendered fractal.

### Save the Image

To save the rendered image instead of only displaying it, add the following before `plt.show()`:

```python
plt.savefig(
    "fractal.png",
    dpi=200,
    bbox_inches="tight",
    pad_inches=0
)
```

## Customization

### Explore a Different Region

Change the coordinate boundaries to explore different areas of the Mandelbrot set:

```python
x_min = -0.7452
x_max = -0.7432
y_min = 0.1122
y_max = 0.1134
```

### Increase the Detail

Increase `max_iter` to reveal more detail, especially when exploring deeper zoom levels:

```python
max_iter = 800
```

Higher iteration counts will increase rendering time.

### Change the Lighting Angle

Adjust the light direction parameters:

```python
lx
ly
lz
```

Changing these values alters the direction of the simulated 3D light source.

### Change the Color Palette

The default colormap is:

```python
cmap="magma"
```

You can experiment with other Matplotlib colormaps:

```python
cmap="inferno"
cmap="plasma"
cmap="cividis"
```

## Example Result

The renderer produces a deep-zoom Mandelbrot visualization with:

* Intricate spiral structures
* Smooth escape-time shading
* Simulated 3D depth
* Metallic highlights
* High-contrast generative-art aesthetics

## Project Structure

```text
.
├── fractal_render.py
├── README.md
└── fractal.png          # Optional generated output
```

## License

This project is provided for educational and generative-art purposes. You are free to modify and experiment with the code.
