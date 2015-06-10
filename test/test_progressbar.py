'''Progress Bar visual test for `minchin.text`'''

import time
from minchin import text as wmtext

def test_progressbar():
    bar = wmtext.progressbar()
    for i in range(0,101):
        bar.update(i)
        time.sleep(0.05)
    print

    bar2 = wmtext.progressbar(maximum=0)
    print
    bar2.update(0.00001)
    print
        
    bar = wmtext.progressbar(maximum=5326)
    for i in range(0,5327):
        bar.update(i)
        #time.sleep(0.01)

if __name__ == "__main__":
    import colorama
    colorama.init()
    test_progressbar()
