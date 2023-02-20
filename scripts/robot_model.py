# import important modules
import numpy as np
import math


def dh_transformation(theta, a, d, alpha):
    """
    Receives Denavit-Hartenberg parameters and returns a combined homogenous transformation matrix

    :param theta: Joint Angle
    :param a: Link Length
    :param d: Link Offset
    :param alpha: Link Twist
    :return: Homogenous transformation matrix
    """

    # Create a transformation matrix using the provided Denavit-Hartenberg parameters
    transformation_matrix = np.array(
        [[math.cos(theta), -math.sin(theta) * math.cos(alpha), math.sin(theta) * math.sin(alpha), a * math.cos(theta)],
         [math.sin(theta), math.cos(theta) * math.cos(alpha), -math.cos(theta) * math.sin(alpha), a * math.sin(theta)],
         [0, math.sin(alpha), math.cos(alpha), d],
         [0, 0, 0, 1]])
    # Return transformation matrix
    return transformation_matrix


def kinematic_chain(joint_chain):
    """
    Receives a 2D array containing the Denavit-Hartenberg parameters for each joint
    Returns a homogenous transformation matrix for the entire kinematic chain
    :param joint_chain: 2D array of Denavit-Hartenberg parameters
    :return: Homogenous Transformation Matrix
    """
    # Initialize running total with an Identity Matrix
    homogenous_transformation = np.array([[1, 0, 0, 0],
                                          [0, 1, 0, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 1]])
    # Loop through each set of joint parameters in the chain
    for joint in joint_chain:
        # Pass the Denavit-Hartenberg Parameters to the dh_transformation function
        dh_trans_result = dh_transformation(joint[0], joint[1], joint[2], joint[3])
        # Multiply the resulting Matrix by the running total
        homogenous_transformation = np.matmul(homogenous_transformation, dh_trans_result)
    # Return homogenous transformation matrix for the entire kinematic chain
    return homogenous_transformation


def get_pos(transformation_matrix):
    """
    Receives a homogenous transformation matrix and returns the x, y, z components
    :param transformation_matrix: Homogenous Transformation Matrix
    :return: x, y, z components
    """
    # receives a homogenous transformation and returns x,y,z components
    x = transformation_matrix[0][3]
    y = transformation_matrix[1][3]
    z = transformation_matrix[2][3]

    return x, y, z


def get_rot(transformation_matrix):
    """
    Receives a homogenous transformation matrix and returns the roll-pitch-yaw angles
    :param transformation_matrix: Homogenous transformation matrix
    :return: Roll-Pitch-Yaw angles
    """
    # Get Roll angle using given formula
    roll = (math.atan2((transformation_matrix[2][1]), (transformation_matrix[2][2])))
    # Get Pitch angle using given formula
    pitch = (math.atan2(-(transformation_matrix[2][0]),
                        math.sqrt((transformation_matrix[2][1]) ** 2 + (transformation_matrix[2][2]) ** 2)))
    # Get Yaw angle using given formula
    yaw = (math.atan2((transformation_matrix[1][0]), (transformation_matrix[0][0])))

    # Return roll, pitch, yaw angles
    return roll, pitch, yaw
