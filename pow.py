class Solution(object):
    def myPow(self, x, n):
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        current_product = x
        
        while n > 0:
            # If n is odd, multiply res by the current product
            if n % 2 == 1:
                res *= current_product
            
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2
            
        return res
