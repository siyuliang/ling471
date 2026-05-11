# Programming activity: load experiment_data.txt and run three regressions
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

filename = "experiment_data.txt"
path = Path(filename)

if path.exists():
    print(f"Loading data from {path.resolve()}")
    d = np.loadtxt(path)
else:
    print(f"{filename!r} was not found, so I am creating small fake data for demo purposes.")
    print("In class, replace this with the real experiment_data.txt file.")
    rng = np.random.default_rng(471)
    characters = rng.integers(3, 13, size=30)
    latency_ms = 500 + 25 * characters + rng.normal(0, 80, size=characters.shape[0])
    d = np.column_stack([characters, latency_ms])

# First column = number of characters; second column = response latency.
X_raw = d[:, 0]
y_raw = d[:, 1]

print("First five rows of data:")
print(d[:5])

# Method 1: pseudoinverse.
X_with_ones = np.vstack((np.ones(X_raw.shape[0]), X_raw)).T
y_col = y_raw.reshape(-1, 1)
b_pinv = np.linalg.pinv(X_with_ones) @ y_col

print("\nMethod 1: np.linalg.pinv")
print("intercept =", b_pinv[0, 0])
print("slope =", b_pinv[1, 0])

# Method 2: least squares.
b_lstsq, residual_sum, rank, singular_values = np.linalg.lstsq(
    X_with_ones, y_col, rcond=None
)

print("\nMethod 2: np.linalg.lstsq")
print("intercept =", b_lstsq[0, 0])
print("slope =", b_lstsq[1, 0])
print("residual_sum =", residual_sum)

# Method 3: scikit-learn.
try:
    from sklearn.linear_model import LinearRegression
except ImportError:
    print("\nMethod 3 skipped: scikit-learn is not installed.")
    print("Install it with: pip install scikit-learn")
    reg = None
else:
    X_sklearn = X_raw.reshape(-1, 1)
    reg = LinearRegression().fit(X_sklearn, y_raw)
    print("\nMethod 3: sklearn.linear_model.LinearRegression")
    print("intercept =", reg.intercept_)
    print("slope =", reg.coef_[0])
    print("R^2 score =", reg.score(X_sklearn, y_raw))

# Plot result from pseudoinverse.
x_line = np.linspace(X_raw.min(), X_raw.max(), 100)
y_line = b_pinv[0, 0] + b_pinv[1, 0] * x_line

plt.figure()
plt.scatter(X_raw, y_raw)
plt.plot(x_line, y_line)
plt.xlabel("Number of characters")
plt.ylabel("Response latency, ms")
plt.title("Experiment data: characters vs. response latency")
plt.tight_layout()
plt.show()