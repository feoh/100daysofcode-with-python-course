import itertools
from time import sleep

import random


def sleep_cycle_timne():
    random.seed()
    sleep((random.random() * 10) + 3)


def cycle_lights():
    traffic_lights = {'red': 'stop', 'yellow': 'caution', 'green': 'go'}

    light_cycle = itertools.cycle(traffic_lights.keys())

    for color in light_cycle:
        sleep_cycle_timne()
        print(f'Light is {color}: {traffic_lights[color]}')


if __name__ == "__main__":
    cycle_lights()
