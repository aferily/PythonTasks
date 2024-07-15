# https://edabit.com/challenge/xbjDMxzpFcsAWKp97

from functools import reduce

def can_see_stage(seats):
    return all([
        reduce(
            lambda prev, x: -1 if prev >= x or prev == -1 else x, t
        ) != -1 for t in zip(*seats)
    ])