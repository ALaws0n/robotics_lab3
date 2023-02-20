# import these incase I need 'em
import math
import robot_model as rm


def two_link_planar_manipulator():
    dh_parameters = [[(math.pi/2), 1, 0, 0], [(math.pi/2), 1, 0, 0]]
    homogenous_transformation = rm.kinematic_chain(dh_parameters)
    x, y, z = rm.get_pos(homogenous_transformation)
    roll, pitch, yaw = rm.get_rot(homogenous_transformation)

    print('x: ', x, '\nY: ', y, '\nZ: ', z)
    print("Roll: ", roll)
    print("Pitch: ", pitch)
    print("Yaw: ", yaw)


def UR5e_case_1():
    dh_parameters = [[0, 0, 0.1625, math.pi/2],   # Joint 1
                     [0, -0.425, 0, 0],           # Joint 2
                     [0, -0.3922, 0, 0],          # Joint 3
                     [0, 0, 0.1333, math.pi/2],   # Joint 4
                     [0, 0, 0.0998, -math.pi/2],  # Joint 5
                     [0, 0, 0.0996, 0]]           # Joint 6
    homogenous_transformation = rm.kinematic_chain(dh_parameters)
    x, y, z = rm.get_pos(homogenous_transformation)
    roll, pitch, yaw = rm.get_rot(homogenous_transformation)
    print('x: ', x, '\nY: ', y, '\nZ: ', z)
    print("Roll: ", roll)
    print("Pitch: ", pitch)
    print("Yaw: ", yaw)


def UR5e_case_2():
    dh_parameters = [[0, 0, 0.1625, math.pi/2],   # Joint 1
                     [-math.pi/2, -0.425, 0, 0],           # Joint 2
                     [0, -0.3922, 0, 0],          # Joint 3
                     [0, 0, 0.1333, math.pi/2],   # Joint 4
                     [0, 0, 0.0998, -math.pi/2],  # Joint 5
                     [0, 0, 0.0996, 0]]           # Joint 6
    homogenous_transformation = rm.kinematic_chain(dh_parameters)
    x, y, z = rm.get_pos(homogenous_transformation)
    roll, pitch, yaw = rm.get_rot(homogenous_transformation)
    print('x: ', x, '\nY: ', y, '\nZ: ', z)
    print("Roll: ", roll)
    print("Pitch: ", pitch)
    print("Yaw: ", yaw)


if __name__ == '__main__':
    print("Two Link Planar Manipulator")
    two_link_planar_manipulator()
    print("\n UR5e Case 1")
    UR5e_case_1()
    print("\n UR5e Case 2")
    UR5e_case_2()

