class Solution(object):
    def plusOne(self, digits):
        for x in range(len(digits)):
            if digits[-x-1] != 9:
                digits[-x-1] += 1
                return digits
            digits[-x-1] = 0
        digits.insert(0,1)
        return digits
