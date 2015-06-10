'''Progress Bar visual test for `wmtext`'''

import time
import colorama
colorama.init()

from minchin import text as wmtext

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

