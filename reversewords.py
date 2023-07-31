def reverseWords(s):
    temp = ''
    res = []
    for i in s:
        if i != ' ':
            temp += i
        elif temp!='':
            res.append(temp)
            temp=''
    if temp !='':
        res.append(temp)
    print(temp)
    print(res)
    return ' '.join(res[::-1])

if __name__ == '__main__':
    print(reverseWords('the sky is blue'))
    print(reverseWords(' hello world  '))