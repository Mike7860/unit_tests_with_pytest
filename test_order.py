import pytest
import math


def select_single_box(x):
    if x == 0:
        return [0, 0, 0]
    if x <= 3:
        return [1, 0, 0]
    if x <= 6:
        return [0, 1, 0]
    if x <= 9:
        return [0, 0, 1]


def single_box_and_overflow(x, m, s, d):
    overflow = [m, s, d]
    result = select_single_box(x)

    # sum 2 arrays [a, b, c] and [d, e, f] into [a+d, b+e, c+f]
    for i in range(len(result)):
        result[i] = result[i] + overflow[i]
    return result


def goal(x):
    if x > 100:
        raise Exception("Wrong value, should be equal or less than 100")
    if x <= 9:
        return single_box_and_overflow(x, 0, 0, 0)
    if x >= 16:
        big_boxes_temp = 1 + (x - 9) // 9
        x = x - big_boxes_temp * 9
        return single_box_and_overflow(x, 0, 0, big_boxes_temp)

    # for x in [10, 15] below scheme doesn't work, so treat it specially
    if x <= 12:
        return [0, 2, 0]
    if x <= 15:
        return [0, 0, 2]


def result(x):
    boxes = goal(x)
    wrap_up_box = sum(boxes)
    if wrap_up_box == 1:
        wrap_up_box = 0
    wrap_up_box = math.ceil(wrap_up_box / 3)
    print("test case: {}, small: {}, medium: {}, big: {}, wrap-up: {}".format(x, boxes[0], boxes[1], boxes[2], wrap_up_box))


if __name__ == "__main__":
    # invoking function which return details for all test cases
    for i in range(1, 101):
        result(i)


def test_select_single_box():
    """function for unit tests"""
    # assert(goal(55) == [1, 0, 6])
    # assert(goal(5) == [0, 1, 0])
    # assert(goal(15) == [0, 0, 2])

# invoking function with parameter x - order quantity, which return details about boxes
# result(x=55)