class Solution:
    def kidsWithCandies(candies, extraCandies):
        maximum = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result



if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    res =  Solution.kidsWithCandies(candies, extraCandies)
    print(res)