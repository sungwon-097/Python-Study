#중복 없이 1등 3명과 2등 3명을 추첨

from random import *

lst=range(1,21)
lst=list(lst)
shuffle(lst)
winners=sample(lst,4)
print("-- 당첨자발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다! --")