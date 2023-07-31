def StackEmpty():
    if s.top == 0:
        return True
    else:
        return False


def Push(s,x):
    s.top = s.top+1
    s[s.top] =x


if __name__ == '__main__':
    s = [15,6,2,9]
    if StackEmpty(s):
         print('underflow')
    else:
        s.top = s.top-1
    return s[s[top]+1]