try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Run: pip install numpy")
else:
    # Create an array of pipeline metrics
    row_counts = np.array([1200, 1500, 1100, 1600])

    # Vectorized calculations apply to the full array at once
    adjusted_counts = row_counts + 100
    high_volume_mask = row_counts >= 1400

    print("Original counts:", row_counts)
    print("Adjusted counts:", adjusted_counts)
    print("High volume flags:", high_volume_mask)
    print("Average rows processed:", np.mean(row_counts))
