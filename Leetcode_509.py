# memoization

class solution:
    def fib(self, n: int) -> int:
        memo = {0:0 , 1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
            
        return f(n)
    
# time : O(n)
# space : O(n)


# tabulation

class solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
# time : O(n)
# space : O(n)

# space optimized

class solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        prev = 0
        cur = 1

        for i in range(2, n + 1):
            prev, cur = cur, prev + cur

        return cur

# time : O(n)
# space : O(1)

# log approach

class solution:
    def fib(self, n:int) -> int:
        golden_ratio = (1+(5**0.5)) / 2
        return int(round(golden_ratio**n / (5**0.5)))