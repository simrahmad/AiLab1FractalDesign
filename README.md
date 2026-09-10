\# Artistic Mandelbrot Fractal Renderer



A Python script that renders a high-resolution, deep-zoom view of the Mandelbrot set with a simulated 3D metallic lighting effect, producing a striking piece of generative art rather than a plain escape-time plot.



\## What It Does



The script zooms into a narrow region of the Mandelbrot set near one of its classic spiral boundaries and computes, for each pixel, how quickly the corresponding complex point escapes to infinity under iteration. That escape data is then treated as a height field and lit like a 3D surface, giving the final image a sense of depth and sheen instead of flat banded coloring.



\## How It Works



1\. \*\*Coordinate grid\*\*: A grid of complex numbers `C` is built over a tight window (`x: -0.7452 to -0.7432`, `y: 0.1122 to 0.1134`), a region chosen for its intricate spiral detail.



2\. \*\*Escape-time iteration\*\*: For up to `max\_iter` steps, each point is updated with the Mandelbrot recurrence `Z = Z^2 + C`. Only points that have not yet escaped (`|Z| <= 2.0`) continue iterating, which keeps the computation efficient as more of the grid escapes over time.



3\. \*\*Smooth coloring\*\*: Instead of storing a plain integer iteration count (which produces visible banding), the script computes a continuous, smoothed iteration value using the classic `i + 1 - log2(log(|Z|))` potential formula. This is stored in `smooth\_iter`.



4\. \*\*Noise reduction\*\*: A light Gaussian blur (`sigma=0.5`) smooths out pixel-level artifacts in the iteration field.



5\. \*\*Bump-mapped lighting\*\*: The script treats `smooth\_iter` as a height map and computes its gradient (`dx`, `dy`) to derive a surface normal at every pixel, as if the fractal were a physical relief surface. A fixed light direction is then used to calculate:

&#x20;  - \*\*Diffuse shading\*\*: how directly each surface point faces the light.

&#x20;  - \*\*Specular highlight\*\*: a sharp, metallic-looking glint (`diffuse^16`) where the surface normal aligns closely with the light direction.



6\. \*\*Compositing\*\*: The final image blends the raw escape potential with the diffuse and specular lighting terms (weighted `0.75`, `25.0`, and `50.0` respectively) to produce a rich, high-contrast brightness map.



7\. \*\*Rendering\*\*: The result is displayed with Matplotlib using the `magma` colormap, which pairs well with the metallic lighting effect, at 200 DPI with all axes and padding removed for a clean image.



\## Parameters



| Parameter | Description | Default |

|---|---|---|

| `width` | Output image width in pixels | 1600 |

| `height` | Output image height in pixels | 1000 |

| `max\_iter` | Maximum escape-time iterations per point | 400 |



\## Requirements



\- `numpy`

\- `matplotlib`

\- `scipy`



Install with:

```bash

pip install numpy matplotlib scipy

```



\## Usage



Run the script directly, or execute the notebook cell. A Matplotlib window will display the rendered fractal:



```bash

python fractal\_render.py

```



To save the image instead of only displaying it, add before `plt.show()`:



```python

plt.savefig("fractal.png", dpi=200, bbox\_inches="tight", pad\_inches=0)

```



\## Customization Tips



\- \*\*Different region\*\*: Change `x\_min, x\_max, y\_min, y\_max` to explore other areas of the Mandelbrot set.

\- \*\*More detail\*\*: Increase `max\_iter` for deeper zooms (at the cost of longer render times).

\- \*\*Lighting angle\*\*: Adjust `lx, ly, lz` to change the simulated light source direction.

\- \*\*Color palette\*\*: Swap `cmap="magma"` for other Matplotlib colormaps such as `"inferno"`, `"plasma"`, or `"cividis"`.

