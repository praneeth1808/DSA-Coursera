# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    # Make diagonal elements non-zero
    for i in range(size):
        if(a[i][i]==0):
            for j in range(size):
                k = (i+j+1)%size
                if(a[k][i]!=0):
                    a[k],a[i] = a[i],a[k]
                    b[k],b[i] = b[i],b[k]
                    break
    return Equation(a, b)

def SelectPivotElement(a, b, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element, n, m):
    # Write your code here
    pivot_value = a[pivot_element.row][pivot_element.column]
    for i in range(m):
        a[pivot_element.row][i] = a[pivot_element.row][i]/pivot_value
    b[pivot_element.row] /=pivot_value
    for i in range(n):
        if i !=pivot_element.row:
            multiplicand = a[i][pivot_element.column]
            for j in range(m):
                a[i][j] -= a[pivot_element.row][j]*multiplicand
            b[i] -= b[pivot_element.row]*multiplicand
    pass

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    n = size
    m = len(a[0])
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        # pivot_element = Position(size,size)
        pivot_element = SelectPivotElement(a, b, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element, n, m)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    try:
        equation = ReadEquation()
        solution = SolveEquation(equation)
        PrintColumn(solution)
        exit(0)
    except:
        exit(0)
    # equation = ReadEquation()
    # solution = SolveEquation(equation)
    # PrintColumn(solution)
    # exit(0)
