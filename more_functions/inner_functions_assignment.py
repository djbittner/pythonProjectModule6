"""
Author:  Derek Bittner
Due Date: 10/6/2020

"""


def measurements(rect_measure):
    a_value = 0.0
    p_value = 0.0

    def area(a_measure):
        return a_measure[0] * a_measure[1]

    def perimeter(p_measure):
        return p_measure[0] * 2 + p_measure[1] * 2

    a_value = area(rect_measure)
    p_value = perimeter(rect_measure)
    return "Perimeter = {} Area = {}".format(p_value, a_value)


if __name__ == '__main__':
    print(measurements([2, 3]))
