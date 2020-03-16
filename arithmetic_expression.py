# python3
import sys

# this function takes in array num that stores all digits
# and array op that stores all operators in the arithmetic expression to be maximized
# this function then returns the max and min values of all possible set of subexpressions
# with subexpressions defined as a chunk of the orignal arithmetic expression separated by an operator
# e.g. expression 1 + 2 * 3 - 4
# num = [0,1,2,3,4] with 0 being a padding value that does not have any real meaning except for filling up the array
# op = [0,+,*,-] with 0 being a padding value
def min_and_max(op,m, M, i,j):
    # create two 2D arrays min and max to store the computed min and max values of all subexpressions
    min_ = float("inf")
    max_ = float("-inf")

    for k in range(i, j):
        if op[k] == "+":
            a = M[i][k] + M[k+1][j]
            b = M[i][k] + m[k+1][j]
            c = m[i][k] + m[k+1][j]
            d = m[i][k] + M[k+1][j]
            min_ = min(min_,a,b,c,d)
            max_ = max(max_,a,b,c,d)
        elif op[k] == "-":
            a = M[i][k] - M[k+1][j]
            b = M[i][k] - m[k+1][j]
            c = m[i][k] - m[k+1][j]
            d = m[i][k] - M[k+1][j]
            min_ = min(min_,a,b,c,d)
            max_ = max(max_,a,b,c,d)
        elif op[k] == "*":
            a = M[i][k] * M[k+1][j]
            b = M[i][k] * m[k+1][j]
            c = m[i][k] * m[k+1][j]
            d = m[i][k] * M[k+1][j]
            min_ = min(min_,a,b,c,d)
            max_ = max(max_,a,b,c,d)
        else:
            print("Unable to read operation k")
            sys.exit()

    return min_, max_

# this function returns the maxium value of the passed in string that represents an arithmetic expression
# string dataset = s0s1...s2n of length at most 29
# each symbol at even position of string dataset is a digit (integer from 0-9)
# each symbol at odd position of string dataset is an operator (either +, -, or *. no division)
# rationale behind this solution:
# assume that the last operations in the original expression is operation k, with k belongs to array op
# in order to find the maximum value of the expression,
# we need to find the max and min value of the subexpressions separated by k
# we need both min and max values because say k is an addition operation
# and the original expression = subexp1 * subexp2
# then in order to obtain max value of the original expression, we would want the max value of subexp1 and subexp2
# whereas, if the k operation is a subtraction, we would want to max value of subexp1 and min value of subexp2
def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    # create array num and array op to hold all numbers and operators in the expression
    # add 0 as a padding value to the two arrays
    num = [0]
    op = ['0']
    for i in range(len(dataset)):
        if i%2 == 0: # write all symbols in even positions to array num
            num.append(int(dataset[i]))
        else: # write all symbols in odd positions to array op
            op.append(dataset[i])

    # create a 2D array m and M to store the min and max value of all possible subexpressions
    m = [[0]*len(num) for _ in range (len(num))]
    M = [[0]*len(num) for _ in range (len(num))]

    # fill in the diagnal of the array m and M
    # when the subexpression only contains 1 digit and no operator,
    # the min and max of that expression is equal to that digit
    for i in range(1, len(num)):
        m[i][i] = int(num[i])
        M[i][i] = int(num[i])
    for s in range(1,len(num)):
        for i in range(1,len(num)-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(op,m,M,i,j)

    return M[1][len(num)-1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
    
