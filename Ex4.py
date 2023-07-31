class Solution:
    def canPlaceFlowers(flowerbed, n):
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                print('cur==1')
                if prev == 1:  # violation!
                    print(prev)
                    count -= 1
                prev = 1
            else:
                if prev == 1:  # can't plant
                    print('we are here prev==1')
                    prev = 0
                else:
                    print('we are here else')
                    count += 1
                    prev = 1  # the cur plot gets taken

        return count >= n
        # print(flowerbed)
        # print(n)
        # lenf = len(flowerbed)
        # print(lenf)
        # for i in range(0,lenf-1):
        #     print(i)
        #     if flowerbed[i]==1 & flowerbed[i+1]==1:
        #         print('iam here')
        #         return False
        #     if flowerbed[i-1] == 0 and flowerbed[i]==0:
        #         flowerbed[i] = n
        # print(flowerbed)



if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 1
    res = Solution.canPlaceFlowers(flowerbed, n)
    print(res)
