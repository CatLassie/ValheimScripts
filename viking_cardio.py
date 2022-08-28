import keyboard
import time
import argparse


def main():

    ######## command line stuff ########

    parser = argparse.ArgumentParser(
        description='your arguments, Jarl, if you please:')
    parser.add_argument(
        '--debug', '-d', help='show debug messages', action='store_true')
    parser.add_argument(
        '--lvl', '-l', help='your current run skill level', type=int, default=0)
    parser.add_argument(
        '--stamina1', '-s1', help='max stamina bonus of first consumed food', type=int, default=0)
    parser.add_argument(
        '--duration1', '-d1', help='max duration of first consumed food (in minutes)', type=int, default=0)
    parser.add_argument(
        '--stamina2', '-s2', help='max stamina bonus of second consumed food', type=int, default=0)
    parser.add_argument(
        '--duration2', '-d2', help='max duration of second consumed food (in minutes)', type=int, default=0)
    parser.add_argument(
        '--stamina3', '-s3', help='max stamina bonus of third consumed food', type=int, default=0)
    parser.add_argument(
        '--duration3', '-d3', help='max duration of third consumed food (in minutes)', type=int, default=0)
    parser.add_argument(
        '--rested', help='presence of rested buff', action='store_const', const=1, default=0)
    parser.add_argument(
        '--resting', help='presence of resting buff', action='store_const', const=3, default=0)

    args = parser.parse_args()
    debug = args.debug
    lvl = args.lvl
    max_s1, max_d1 = args.stamina1, args.duration1
    max_s2, max_d2 = args.stamina2, args.duration2
    max_s3, max_d3 = args.stamina3, args.duration3
    rested, resting = args.rested, args.resting

    print('\nyour supplied arguments:', vars(args))
    if debug:
        print('parsed arguments:', debug, lvl, max_s1,
              max_d1, max_s2, max_d2, max_s3, max_d3, rested, resting)

    longest_foor_duration = max(max_d1, max_d2, max_d3)

    if debug:
        print('\nrunning main(), will terminate in',
              longest_foor_duration, 'minutes')

    ######## constants ########

    base_stamina = 50

    regen_modifier = 1 + rested + resting
    regen_rate = 8.66 * regen_modifier
    regen_lag = 1

    drain_rate = 8 * (1 - (0.005 * lvl))

    if debug:
        print('\nmax stamina bonus of food 1:', max_s1)
        print('max duration of food 1:', max_d1, 'min.')
        print('max stamina bonus of food 2:', max_s2)
        print('max duration of food 2:', max_d2, 'min.')
        print('max stamina bonus of food 3:', max_s3)
        print('max duration of food 3:', max_d3, 'min.')
        print('stamina regeneration rate:', regen_rate, '/sec.')
        print('stamina regeneration lag:', regen_lag, 'sec.')
        print('sprint stamina drain rate:', drain_rate, '/sec.')

    ######## loop vars ########

    s1, s2, s3 = max_s1, max_s2, max_s3
    d1, d2, d3 = max_d1, max_d2, max_d3
    current_stamina = base_stamina + s1 + s2 + s3
    sprint_time = current_stamina / drain_rate
    sprint_time = round(sprint_time, 2)
    rest_time = (current_stamina / regen_rate) + regen_lag
    rest_time = round(rest_time, 2)

    if debug:
        print('\ncurrent stamina is:', current_stamina)
        print('current sprint time is:', sprint_time)
        print('current rest time is:', rest_time)

    cardio_start = time.time()
    one_min_start = time.time()

    ######## main loop ########

    while ((time.time() - cardio_start) / 60) < longest_foor_duration:
        try:
            keyboard.press('shift')
            print('\nsprinting for', sprint_time, 'seconds!')
            time.sleep(sprint_time)
            keyboard.release('shift')
            print('resting for', rest_time, 'seconds...')
            time.sleep(rest_time)
        except:
            if debug:
                print('Exception caught!')

        current_time = time.time()
        one_min_interval = current_time - one_min_start

        if one_min_interval > 60:

            ######## stamina update ########

            if debug:
                print('\nupdating stamina values')

            elapsed_time = (current_time - cardio_start) / 60

            d1, d2, d3 = max(max_d1 - elapsed_time, 0), max(max_d2 -
                                                            elapsed_time, 0), max(max_d3 - elapsed_time, 0)
            d1, d2, d3 = round(d1, 2), round(d2, 2), round(d3, 2)

            s1 = calculate_current_food_stamina_bonus(max_s1, d1, max_d1)
            s2 = calculate_current_food_stamina_bonus(max_s2, d2, max_d2)
            s3 = calculate_current_food_stamina_bonus(max_s3, d3, max_d3)
            s1, s2, s3 = round(s1, 2), round(s2, 2), round(s3, 2)

            current_stamina = base_stamina + s1 + s2 + s3
            sprint_time = current_stamina / drain_rate
            sprint_time = round(sprint_time, 2)
            rest_time = (current_stamina / regen_rate) + regen_lag
            rest_time = round(rest_time, 2)

            if debug:
                print('elapsed time:', round(elapsed_time, 2), 'minutes')
                print('remaining stamina/duration of\nfood 1:',
                      s1, '/', d1, '\nfood 2:', s2, '/', d2, '\nfood 3:', s3, '/', d3)
                print('current stamina is:', current_stamina)
                print('current sprint time is:', sprint_time)
                print('current rest time is:', rest_time)

            one_min_start = time.time()

    if debug:
        print('finished main()')


def calculate_current_food_stamina_bonus(max_stamina, duration, max_duration):
    return max_stamina * ((duration / max_duration) ** 0.3)


if __name__ == '__main__':
    main()
