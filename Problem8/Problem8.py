class Solution:
    def kthDigit(self, A, B, K):

        n = A ** B
        temp = n
        
        num_dig = 0
        
        while num_dig < K:
            dig = temp % 10
            temp = temp//10
            num_dig += 1
            
        return dig
        
        
FindDig = Solution()

Dig = FindDig.kthDigit(3,7,2)
print("3**7 = ", 3**7)
print("Kth Digit= ",Dig)