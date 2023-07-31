class Solution:
    def compress(self, chars):
        length = len(chars)
        if length <2:
            return length
        cidx = 0  #current idx
        widx = 0 # write indx

        for pos,char in enumerate(chars):
            print(f'in pos {pos} and the character is  - {char}')
            if (pos+1) == len(chars) or char != chars[pos+1]:
                print(f'inside if loop {pos+1}  and {len(chars)}')
                # print(f'inside if loop {char}  and {chars[pos+1]}')

                chars[widx] = char
                widx +=1

                if pos > cidx:
                    repeated_times = pos-cidx+1
                    for num in str(repeated_times):
                        chars[widx] = num
                        widx +=1
                cidx +=1
        return chars





    def countInc(self, count):
        a = []
        count +=1
        return a.append(count)



        # 0    1    2    3    4    5    6
chars = ["a", "a", "b", "b", "c", "c", "c"]
s = Solution()
print(s.compress(chars))