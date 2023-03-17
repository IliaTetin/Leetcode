# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        min = salary[0]
        max = salary[1]
        for i, val in enumerate(salary):
            if val < min:
                min = val
            elif val > max:
                max = val
            
            sum += val
        return (sum - min - max) / (len(salary) - 2)
