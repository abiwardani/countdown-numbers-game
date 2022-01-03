import solution_parser as sp

class Countdown:
    def __init__(self, targetSum, numbers, useAll = False):
        self.targetSum = targetSum
        self.numbers = numbers
        self.useAll = useAll == True
        self.solution = ""
        self.memo = {}

    def search(self, targetSum = None, numbers = None):
        #setup recursive
        if (targetSum is not None):
            self.targetSum = targetSum
        if (numbers is not None):
            self.numbers = numbers
        self.memo = {}
        self.solution = ""

        #start recursive calls
        solution = self.searchRecursive(self.targetSum, self.numbers, 0, "")

        if (solution):
            spObject = sp.SolutionParser()
            return spObject.toClassicFormat(solution)
        else:
            return None
    
    def searchRecursive(self, targetSum, numbers, repeat, path):
        #if target sum is 0, either initial target was 0 or result of addition or subtraction; and solution does not have to use all
        if (targetSum == 0 and not(self.useAll)): #then found
            self.memo[str(targetSum)+"|"+str(numbers)] = path[1::] #memoize
            return self.memo[str(targetSum)+"|"+str(numbers)]

        #if partial solution already memoized
        if (str(targetSum)+"|"+str(numbers) in self.memo):
            return self.memo[str(targetSum)+"|"+str(numbers)]
        
        #base case; only one useable number
        if (len(numbers) == 1):
            #check if useable number is target sum
            if (targetSum == numbers[0]):
                self.memo[str(targetSum)+"|"+str(numbers)] = str(numbers[0])+path #memoize
                self.solution = self.memo[str(targetSum)+"|"+str(numbers)]
            else:
                self.memo[str(targetSum)+"|"+str(numbers)] = False #memoize
            
            return self.memo[str(targetSum)+"|"+str(numbers)]
        
        #solution within subtract left branch?
        minus = self.searchRecursive(targetSum-numbers[0], numbers[1::], 0, "+"+str(numbers[0])+path)
        self.memo[str(targetSum-numbers[0])+"|"+str(numbers[1::])] = minus #memoize
        dim = minus
        if (dim == False): #solution not within subtract left branch; solution within subtract right branch?
            minus = self.searchRecursive(numbers[0]-targetSum, numbers[1::], 0, "*(-1)+"+str(numbers[0])+path)
            self.memo[str(targetSum-numbers[0])+"|"+str(numbers[1::])] = minus #memoize
            dim = dim or minus
            if (dim == False): #solution not within subtract right branch; solution within addition branch?
                plus = self.searchRecursive(targetSum+numbers[0], numbers[1::], 0, "-"+str(numbers[0])+path)
                self.memo[str(targetSum+numbers[0])+"|"+str(numbers[1::])] = plus #memoize
                dim = dim or plus
                if (dim == False and numbers[0] != 0): #solution not within addition branch and current number not 0; solution within multiplication branch?
                    multiply = self.searchRecursive(targetSum*numbers[0], numbers[1::], 0, "/"+str(numbers[0])+path)
                    self.memo[str(targetSum*numbers[0])+"|"+str(numbers[1::])] = multiply #memoize
                    dim = dim or multiply
                    if (dim == False and numbers[0] != 0): #solution not within multiplication branch and current number not 0; solution within division left branch?
                        divide = self.searchRecursive(targetSum/numbers[0], numbers[1::], 0, "*"+str(numbers[0])+path)
                        self.memo[str(targetSum/numbers[0])+"|"+str(numbers[1::])] = divide #memoize
                        dim = dim or divide
                        if (dim == False and numbers[0] != 0): #solution not within multiplication branch and current number not 0; solution within division left branch?
                            divide = self.searchRecursive(numbers[0]/targetSum, numbers[1::], 0, "^(-1)*"+str(numbers[0])+path)
                            self.memo[str(numbers[0]/targetSum)+"|"+str(numbers[1::])] = divide #memoize
                            dim = dim or divide

        #repeat denotes number of times recursion has been called without eliminating a number
        #if program has iterated throughout the whole list of numbers
        if (repeat == len(numbers)):
            maintain = False #solution does not exist
        else: #else, move the first number to the back of the list and repeat search, while iterating variable:repeat by 1
            maintain = self.searchRecursive(targetSum, numbers[1::]+[numbers[0]], repeat+1, path)
        
        return dim or maintain #if solution found through diminishing search or maintaining search, return solution path; else return false