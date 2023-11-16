import math

import numpy as np


def basic_numpy_operation():
    print("=======basic numpy operation========")
    arr = np.array([1, 2, 3, 4, 5])
    arr_view = arr.view()
    arr_copy = arr.copy()
    arr[3] = 6
    print("arr is: ", arr)
    # the view function will be changed according to arr itself
    print("arr_view is: ", arr_view)
    print("arr_copy is: ", arr_copy)
    print("type of arr is", type(arr))
    print("the shape of arr is:", arr.shape)
    print("the dtype of arr is: ", arr.dtype)
    arr = np.append(arr, 7)
    print("arr append 7 result is: ", arr)
    arr_float = np.array([1.1, 2, 3, 4, 5])
    print("the dtype of {} is: {}".format(arr_float, arr_float.dtype))
    arr2 = np.array([6, 7, 8, 9, 10])
    arr_new = np.concatenate((arr, arr2))
    print("the combination of arr and arr2 is", arr_new)
    print("=======basic numpy operation end========")


def block_demo():
    print("=====block part========")
    block_1 = np.array([[1, 1], [1, 1]])
    block_2 = np.array([[2, 2, 2], [2, 2, 2]])
    block_3 = np.array([[3, 3], [3, 3], [3, 3]])
    block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])

    block_new = np.block([[block_1, block_2], [block_3, block_4]])

    print(block_new)
    print("=====block part end========")


def multi_dimension_operations():
    print("=====multiple dimension start========")
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("arr2d is \n", arr2d)
    print("the shape of arr2d is:", arr2d.shape)
    print("the dim of arr2d is", arr2d.ndim)
    arr2dto3d = arr2d[..., np.newaxis]
    print("3d arr2 is \n", arr2dto3d)
    print("shape of arr2dto3d is: ", arr2dto3d.shape)
    arr3d = np.array(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
            [[9, 10], [11, 12]],
        ]
    )
    print("arr3d shape:{}, dim:{}".format(arr3d.shape, arr3d.ndim))
    print("=====multiple dimension end========")


def linear_algebra():
    print(
        "generating arithmetic progression between 10 and 60 with the difference of 5:"
    )
    arr2 = np.arange(10, 60, 5)
    print("arrange (10, 60, 10)", arr2)
    arr2_reshape = arr2.reshape(2, 5)
    print("arr2 after reshaping is \n", arr2_reshape)
    arr2_swap_column_0_2 = arr2_reshape.copy()
    arr2_swap_column_0_2[:, [2, 0]] = arr2_reshape[:, [0, 2]]
    print("arr2 after swaping the column of 0 and 2 is \n", arr2_swap_column_0_2)
    arr2dzero = np.zeros([4, 3], dtype=int)
    print("a 4*3 zero matrix with 4*3 is: \n", arr2dzero)
    arr2done = np.ones([4, 3], dtype=int)
    print("a 4*3 one matrix with 4*3 is: \n", arr2done)
    # the eye function will create a one matrix
    arr2donematrix = np.eye(3, 3, dtype=int)
    print("unit matrix of 3*3 is \n", arr2donematrix)
    axisinterval_5 = np.linspace(0, 3.0, num=6, retstep=True)
    # it create an array with interval of .5 [0, 0.5, 1.0, 1.5, 2.0, 2.5]
    print("axis is ", axisinterval_5[0])
    axisPI = np.linspace(0, 2 * math.pi, num=13)
    print("sin 0, pi/3, ... is", np.sin(axisPI))


def compare_arr():
    arr = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[1, 2], [3, 4]])
    comparison = arr == arr2
    print("comparison result is: \n", comparison)
    print("equal arrays: ", comparison.all())
    arr = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[1, 2], [3, 5]])
    comparison = arr == arr2
    print("comparison result is: \n", comparison)
    print("equal arrays: ", comparison.all())


def main():
    # basic_numpy_operation()
    # multi_dimension_operations()
    # block_demo()
    # linear_algebra()
    compare_arr()


if __name__ == "__main__":
    main()
