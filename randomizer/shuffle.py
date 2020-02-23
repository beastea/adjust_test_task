import random


def shuffle():
    shuffle_list = list(range(1, 11, 1))
    return random.sample(shuffle_list, len(shuffle_list))
