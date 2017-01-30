'''Progress Bar visual test for `minchin.text`'''

import time
from minchin import text as wmtext


def test_progressbar():
    print('Progress Bar test, minchin.text v{}'.format(wmtext.__version__))

    bar1 = wmtext.progressbar()
    for i in range(0, 101):
        bar1.update(i)
        time.sleep(0.05)
    print()

    bar2 = wmtext.progressbar(maximum=0)
    print()
    bar2.update(0.00001)
    print()

    bar3 = wmtext.progressbar(maximum=5326)
    for i in range(0, 5327):
        bar3.update(i)
        #time.sleep(0.01)
    print()

    bar4 = wmtext.progressbar(maximum=2534, time_interval=1)
    for i in range(0, 2535):
        bar4.update(i)
        time.sleep(0.01)
    print()


if __name__ == "__main__":
    import colorama
    colorama.init()
    test_progressbar()
