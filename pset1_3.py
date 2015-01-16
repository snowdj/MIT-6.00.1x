s = 'azcbobobegghakl'
#s = 'abcde'

start = 0
pos = 1
maxLen = 0
maxStart = 0

if len(s) > 1:
    while pos < len(s):
        strLen = 1
        while True and pos < len(s):
            if ord(s[pos]) >= ord(s[pos-1]):
                strLen += 1
                if pos == len(s)-1:
                    if strLen > maxLen:
                        maxLen = strLen
                        maxStart = start
                pos += 1           
            else:
                if strLen > maxLen:
                    maxLen = strLen
                    maxStart = start
                start = pos
                pos += 1
                break
    substring = s[maxStart : maxStart + maxLen]
else:
    substring = s
print('Longest substring in alphabetical order is: '+ substring)