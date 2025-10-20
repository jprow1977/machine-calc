import math


def calc_sfm_inches(tool_diameter, spindle_speed):
    sfm = (math.pi * tool_diameter * spindle_speed) / 12
    return sfm


def calc_rpm_inches(tool_diameter, feed_rate):
    rpm = (12 * feed_rate) / (math.pi * tool_diameter)
    return rpm


def calc_feed_rate_inches(feed_per_tooth, spindle_speed, num_of_teeth):
    feed_rate = (feed_per_tooth * spindle_speed * num_of_teeth)
    return feed_rate


def calc_material_removal_rate(width_of_cut, depth_of_cut, feed_rate):
    mmr = (width_of_cut * depth_of_cut * feed_rate)
    return mmr


if __name__ == '__main__':
    print(f'Surface Feet Per Minute: {round(calc_sfm_inches(2, 500), 2)}')
    print(f'Spindle Speed: {round(calc_rpm_inches(1.5, 300))} inches per minute.')
    print(f'Feed Rate: {round(calc_feed_rate_inches(.005, 1000, 4))} inches per minute.')
    print(f'Material Removal Rate: {round(calc_material_removal_rate(1, .2, 20))} inches\u00B3')
