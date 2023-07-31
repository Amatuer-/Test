class Solution:
    def gcdOfStrings(str1, str2):
        len1 , len2 = len(str1) , len(str2)
        print(len1 , len2 , len1 % 3)
        def isDivisor(i):
            if len1 % i or  len2 % i:
                print('iam here')
                return False


            f1 , f2 =  len1 // i , len2 //i
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2

        for i in range(min(len1, len2) , 0 , -1):
            print(i)
            if isDivisor(i):
                return str1[:i]
        return ''




if __name__ == '__main__':
    print(Solution.gcdOfStrings('ABABABAB','AB'))