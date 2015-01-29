s='azcbobobobobegghakl'

substring = 'bob'
total_bobs = 0
if substring in s:
    start = 0
    while True:
        start = s.find('bob',start)
        if start == -1:
            break
        total_bobs += 1
        start += 1
else:
        total_bobs = 0
print('Number of times bob occurs is:' + str(total_bobs))