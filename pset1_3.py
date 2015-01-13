s = 'azcbobobegghakl'

start = 0
pos = 0
maxLen = 0
maxStart = 0

while pos < len(s):
    strLen = 1
    start = pos
    while True:
        if ord(s[pos+1]) < ord(s[pos]):
            if strLen > maxLen:
                maxLen = strLen
                maxStart = start
            pos += 1
            break
        else:
            strLen += 1
            pos += 1
substring = s[maxStart : maxStart + strLen + 1]
print('Longest substring in alphabetical order is: '+ substring)