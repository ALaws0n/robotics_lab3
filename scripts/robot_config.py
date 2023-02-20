# Import important modules
import math
import robot_model as rm


def two_link_planar_manipulator():
    """
    Test case for a two link planar manipulator with the following joint conditions:
        Joint 1: Theta = pi/2, a = 1, d = 0, alpha = 0
        Joint 2: Theta = pi/2, a = 1, d = 0, alpha = 0
    :return: None
    """
    # Create a 2D array of Denavit-Hartenberg parameters for each joint
    dh_parameters = [[(math.pi/2), 1, 0, 0], [(math.pi/2), 1, 0, 0]]
    # Get the homogenous transformation matrix from passing the dh_parameters array to the kinematic chain function
    homogenous_transformation = rm.kinematic_chain(dh_parameters)
    # Get the x, y, z components from the homogenous transformation matrix
    x, y, z = rm.get_pos(homogenous_transformation)
    # Get the roll, pitch, yaw angles from the homogenous transformation matrix
    roll, pitch, yaw = rm.get_rot(homogenous_transformation)
    # Display the results from the calculations
    print(f'X: {x:.2f} meters\nY: {y:.2f} meters\nZ: {z:.2f} meters\n'
          f'Roll: {roll:.2f} radians\nPitch: {pitch:.2f} radians\nYaw: {yaw:.2f} radians')


def UR5e_case_1():
    """
    UR5e Test Case 1 using given Denavit-Hartenberg Parameters and a joint angle of 0 for each joint
    :return: None
    """
    # Create 2D array of Denavit-Hartenberg parameters for each joint
    dh_parameters = [[0, 0, 0.1625, math.pi/2],   # Joint 1
                     [0, -0.425, 0, 0],           # Joint 2
                     [0, -0.3922, 0, 0],          # Joint 3
                     [0, 0, 0.1333, math.pi/2],   # Joint 4
                     [0, 0, 0.0998, -math.pi/2],  # Joint 5
                     [0, 0, 0.0996, 0]]           # Joint 6

    # Get the full homogenous transformation matrix of the kinematic chain
    homogenous_transformation = rm.kinematic_chain(dh_parameters)
    # Get the x, y, z components of the homogenous transformation matrix
    x, y, z = rm.get_pos(homogenous_transformation)
    # Get the roll, pitch, yaw angles of the homogenous transformation matrix
    roll, pitch, yaw = rm.get_rot(homogenous_transformation)
    # Display the results from the calculations
    print(f'X: {x:.2f} meters\nY: {y:.2f} meters\nZ: {z:.2f} meters\n'
          f'Roll: {roll:.2f} radians\nPitch: {pitch:.2f} radians\nYaw: {yaw:.2f} radians')


def UR5e_case_2():
    """
    UR5e Test Case 1 using given Denavit-Hartenberg Parameters and a joint angle of 0 all joints except Joint 2.
    Joint 2 will be given an angle of -pi/2
    :return: None
    """
    # Create 2D array of Denavit-Hartenberg parameters for each joint
    dh_parameters = [[0, 0, 0.1625, math.pi/2],   # Joint 1
                     [-math.pi/2, -0.425, 0, 0],  # Joint 2
                     [0, -0.3922, 0, 0],          # Joint 3
                     [0, 0, 0.1333, math.pi/2],   # Joint 4
                     [0, 0, 0.0998, -math.pi/2],  # Joint 5
                     [0, 0, 0.0996, 0]]           # Joint 6
    # Get the full homogenous transformation matrix of the kinematic chain
    homogenous_transformation = rm.kinematic_chain(dh_parameters)
    # Get the x, y, z components of the homogenous transformation matrix
    x, y, z = rm.get_pos(homogenous_transformation)
    # Get the roll, pitch, yaw angles of the homogenous transformation matrix
    roll, pitch, yaw = rm.get_rot(homogenous_transformation)
    # Display the results from the calculations
    print(f'X: {x:.2f} meters\nY: {y:.2f} meters\nZ: {z:.2f} meters\n'
          f'Roll: {roll:.2f} radians\nPitch: {pitch:.2f} radians\nYaw: {yaw:.2f} radians')


if __name__ == '__main__':
    print("Two Link Planar Manipulator")
    two_link_planar_manipulator()
    print("\nUR5e Case 1")
    UR5e_case_1()
    print("\nUR5e Case 2")
    UR5e_case_2()

