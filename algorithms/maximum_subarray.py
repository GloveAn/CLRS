#!/usr/bin/python


# exercises 4.1-2, exercises 4.1-3
def maximum_subarray_brute_force(A):
    INFINITY = 0x7FFFFFFF

    left_sum = [0] * (len(A) + 1)
    max_record = (0, 0, -INFINITY)

    for i in range(0, len(A)):
        left_sum[i + 1] = left_sum[i] + A[i]
    for i in range(len(A)):
        for j in range(i, len(A)):
            if left_sum[j + 1] - left_sum[i] > max_record[2]:
                max_record = (i, j, left_sum[j + 1] - left_sum[i])

    return max_record


# chapter 4.1, exercises 4.1-3
def maximum_subarray_divide_conquer(A):
    INFINITY = 0x7FFFFFFF


    def find_max_crossing_sunarray(A, low, mid, high):
        left_sum = -INFINITY
        cross_sum = 0
        max_left = mid
        for i in reversed(range(low, mid)):
            cross_sum = cross_sum + A[i]
            if cross_sum > left_sum:
                left_sum = cross_sum
                max_left = i

        right_sum = -INFINITY
        cross_sum = 0
        max_right = mid + 1
        for j in range(mid, high):
            cross_sum = cross_sum + A[j]
            if cross_sum > right_sum:
                right_sum = cross_sum
                max_right = j

        return (max_left, max_right, left_sum + right_sum)


    def find_max_subarray(A, low, high):
        if high == low + 1:
            return (low, high, A[low])
        else:
            mid = (low + high) // 2
            left_low, left_high, left_sum = \
                find_max_subarray(A, low, mid)
            right_low, right_high, right_sum = \
                find_max_subarray(A, mid, high)
            cross_low, cross_high, cross_sum = \
                find_max_crossing_sunarray(A, low, mid, high)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)


    return find_max_subarray(A, 0, len(A))


# exercises 4.1-5
def maximum_subarray(A):  # linear time
    """proof
    http://blog.eitanadler.com/2015/06/clrs-chapter-41-exercises.html
    """
    max_left = 0
    max_right = 0
    max_sum = A[0]
    cur_left = 0
    cur_sum = 0

    for i in range(len(A)):
        cur_sum = max(cur_sum + A[i], A[i])
        if cur_sum >= max_sum:
            max_left = cur_left
            max_right = i
            max_sum = cur_sum
        if cur_sum == A[i]:
            cur_left = i

    return (max_left, max_right, max_sum)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(maximum_subarray_brute_force(A))
    print(maximum_subarray_divide_conquer(A))
    print(maximum_subarray(A))
