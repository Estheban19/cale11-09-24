import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([0, 160, 20])
y = np.array([0, 80, 10])

# Create a plot
plt.plot(x, y, 'o-', color='b')  # 'o-' means circle markers with a solid line

# Add title and labels for clarity
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
