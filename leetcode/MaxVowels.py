def maxVowels(s, k):
    vowels = 'aioue'
    cnt = ans = sum(s[i] in vowels for i in range(k))
    # print(cnt)
    # print(ans)
    if ans !=k:
        for i in range(k , len(s)):
            print(f's[i] {(s[i] in vowels)}')
            print(f's[i-k] is {s[i-k] in vowels}')
            # cnt += (s[i] in vowels) - (s[i-k] in vowels)
            ans = max(cnt , ans)
    return ans

if __name__ == '__main__':
    s = 'abciiidef'
    k = 3
    print(maxVowels(s,k))