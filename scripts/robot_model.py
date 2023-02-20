# import important modules
import numpy as np
import math


def dh_transformation(theta, a, d, alpha):
    # Receives denvait-hartenburg parameters
    # returns a combined homogenous transformation matrix according to dh convention
    Ai = np.array(
        [[math.cos(theta), -math.sin(theta) * math.cos(alpha), math.sin(theta) * math.sin(alpha), a * math.cos(theta)],
         [math.sin(theta), math.cos(theta) * math.cos(alpha), -math.cos(theta) * math.sin(alpha), a * math.sin(theta)],
         [0, math.sin(alpha), math.cos(alpha), d],
         [0, 0, 0, 1]])

    return Ai


def kinematic_chain(link_chain):
    # receives a 2D array containing dh parameters
    # return a homogenous transformation
    # loop that scans the rows and multiplies the transformation
    # init with an identity matrix
    homogenous_transformation = np.array([[1, 0, 0, 0],
                                          [0, 1, 0, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 1]])
    for link in link_chain:
        dh_trans_result = dh_transformation(link[0], link[1], link[2], link[3])
        homogenous_transformation = np.matmul(homogenous_transformation, dh_trans_result)

    return homogenous_transformation


def get_pos(transformation_matrix):
    # receives a homogenous transformation and returns x,y,z components
    x = transformation_matrix[0][3]
    y = transformation_matrix[1][3]
    z = transformation_matrix[2][3]

    return x, y, z


def get_rot(transformation_matrix):
    # receives homogenous transformation matrix
    # returns roll-pitch-yaw angles
    # TODO - look at the Pitch formula some more if this doesnt work
    roll = (math.atan2((transformation_matrix[2][1]), (transformation_matrix[2][2])))
    pitch = (math.atan2(-(transformation_matrix[2][0]),
                        math.sqrt((transformation_matrix[2][1]) ** 2 + (transformation_matrix[2][2]) ** 2)))
    yaw = (math.atan2((transformation_matrix[1][0]), (transformation_matrix[0][0])))

    return roll, pitch, yaw
