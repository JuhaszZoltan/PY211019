# 2004 -> IGEN
# 1600 -> IGEN
# 1700 -> 
# 2017 -> NEM

ev = int(input('év: '))

if   ev % 400 == 0: print('szökőév')
elif ev % 100 == 0: print('NEM szökőév')
elif ev %   4 == 0: print('szökőév')
else:               print('NEM szökőév')