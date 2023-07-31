class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            print(f'area is {area} , {(r-l)}  and {min(height[l],height[r])}')
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
                print('iam here')
            else:
                r -= 1
                print('No iam here')
        return area

if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))