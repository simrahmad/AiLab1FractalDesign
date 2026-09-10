import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


def generate_artistic_fractal(width=1600, height=1000, max_iter=400):
    # High-detail zoom coordinates into a classic spiral boundary
    x_min, x_max = -0.7452, -0.7432
    y_min, y_max = 0.1122, 0.1134

    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C)
    smooth_iter = np.zeros(C.shape, dtype=np.float64)

    # Escape-time algorithm with smooth color potential
    for i in range(max_iter):
        mask = np.abs(Z) <= 2.0
        Z[mask] = Z[mask]**2 + C[mask]

        abs_z = np.abs(Z)
        smooth_mask = mask & (abs_z > 1.0)
        smooth_iter[smooth_mask] = (
            i + 1 - np.log2(np.log(abs_z[smooth_mask]))
        )

    # Normalize iteration depth for shading
    smooth_iter = gaussian_filter(smooth_iter, sigma=0.5)

    # Generate 3D Surface Normals (Bump-mapping effect)
    dy, dx = np.gradient(smooth_iter)
    normal_x = -dx
    normal_y = -dy
    normal_z = 0.15

    # Normalize normal vector
    norm = np.sqrt(normal_x**2 + normal_y**2 + normal_z**2)
    nx = normal_x / norm
    ny = normal_y / norm
    nz = normal_z / norm

    # Light direction vector
    lx, ly, lz = -0.577, 0.577, 0.577

    # Calculate Diffuse Shading & Specular Metallic Highlight
    diffuse = np.maximum(0, nx * lx + ny * ly + nz * lz)
    specular = np.power(diffuse, 16)

    # Combine escape potential with light intensity
    final_image = smooth_iter * 0.75 + diffuse * 25.0 + specular * 50.0

    return final_image


# Render high-resolution fractal
data = generate_artistic_fractal(
    width=1600,
    height=1000,
    max_iter=400
)

# Display with a vibrant, metallic color map
plt.figure(figsize=(16, 10), dpi=200)
plt.imshow(data, cmap="magma", origin="lower")
plt.axis("off")
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.show()