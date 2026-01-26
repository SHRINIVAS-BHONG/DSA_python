# Recursive Backtracking:-
# Recursive Backtracking is an exhaustive problem-solving technique that explores all possible choices to find solutions.


# Key Steps:

# Make Decisions
# Choose one option among all available possibilities at the current step.

# Recursion
# Recursively solve the remaining subproblem after making a decision.

# Base Case
# Stop the recursion when a valid solution is found or when no further decisions are possible.

# Undo Decisions (Backtracking)
# Revert the last decision to explore alternative choices.


# Important Notes:
# Backtracking follows an exhaustive approach, meaning it systematically explores all possible paths.
# Whenever a problem asks for all solutions, all possible ways, or all combinations, backtracking is typically the preferred approach.

class Solution:
    def subsets(self, nums):
        n = len(nums)
        res, sol = [], []

        def backtrack(index):
            if index == n:
                res.append(sol.copy())
                return
            
            # dont pick nums[i]
            backtrack(index + 1)

            # picks nums[i]
            sol.append(nums[index])
            backtrack(index + 1)
            sol.pop()

        backtrack(0)
        return res
    
# time : O(2^n)
# space : O(n)