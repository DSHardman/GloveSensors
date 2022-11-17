import numpy as np
import matplotlib.pyplot as plt
from HandStrain import get_hand_field


def relu(relu_var):
    """We only model positive strains (tensions) as affecting the resistance - ReLU removes negative components"""
    for i in range(len(relu_var)):
        for j in range(len(relu_var[i])):
            relu_var[i][j] = max(0.0, relu_var[i][j])
    return relu_var


def strain_model(sensor_path, u, v, GF=1.4):
    # Sensor path is array of [x y t] points, assumed in mm
    # u & v are strains at the points in the strain field in x & y directions
    # GF is material gauge factor

    # Only consider tensile strains: assume compressions have no effect
    u = relu(u)
    v = relu(v)

    num_sum = 0  # Initialise numerator sum
    den_sum = 0  # Initialise denominator sum

    # Perform discrete summation in lieu of integration
    for i in range(1, len(sensor_path)):
        path_vec = [sensor_path[i][0]-sensor_path[i-1][0], sensor_path[i][1]-sensor_path[i-1][1]]

        # Coordinate of mid-point
        p_x = 0.5 * (sensor_path[i][0] + sensor_path[i - 1][0])
        p_y = 0.5 * (sensor_path[i][1] + sensor_path[i - 1][1])

        # Get strain of nearest neighbour
        strain = [u[round(p_x) - 1][round(p_y) - 1], v[round(p_x) - 1][round(p_y) - 1]]

        # Increment numerator: sign of direction should not matter, so np.abs function
        # Dimensionless: unaffected by unit
        num_sum += np.abs((strain[0]*path_vec[0] + strain[1]*path_vec[1])/sensor_path[i][2])

        # Increment denominator
        # Dimensionless: unaffected by unit
        den_sum += np.sqrt(path_vec[0]**2 + path_vec[1]**2)/sensor_path[i][2]

        # Plot sensor element line
        plt.plot([sensor_path[i - 1][0], sensor_path[i][0]], [sensor_path[i - 1][1], sensor_path[i][1]],
                 color='k', linewidth=sensor_path[i][2])

    return GF*num_sum/den_sum


# Read sensor shape from file exported from inkscape
file = open("TestXY.xyz", 'r')
lines = file.readlines()
example_sensor_path = []
for line in lines:
    line = line.split()
    assert(len(line) == 3)
    extracted_data = []
    for i in range(3):
        extracted_data.append(float(line[i]))
    example_sensor_path.append(extracted_data)
file.close()

x, y = np.meshgrid(np.linspace(1, 200, 200), np.linspace(1, 200, 200))

# This function crudely defines a strain field for different regions of the hand
strain_field = get_hand_field(palm=(0, 3),
                              thumb1=(1, 1), thumb2=(0.7, 1),
                              index1=(1.2, 0.9), index2=(0.1, 1),
                              middle1=(1, 0), middle2=(1, 0),
                              ring1=(0, 1), ring2=(0.5, 0),
                              pinky1=(1, 0), pinky2=(0.3, 0.7))

u = strain_field[0]
v = strain_field[1]

# Plot strain field
plt.quiver(x, y, relu(u), relu(v), headwidth=0, headlength=0, headaxislength=0)
plt.xlim([0, 200])
plt.ylim([0, 200])

# Calculate sensitivity and draw sensor path
print(strain_model(example_sensor_path, u, v))
plt.show()
