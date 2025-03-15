from itertools import permutations 
def solve_cryptarithm(equation): 
    letters = set(filter(str.isalpha, equation)) 
    if len(letters) > 10: 
        return None   
    for perm in permutations(range(10), len(letters)): 
        mapping = dict(zip(letters, perm)) 
        expr = equation 
        for letter, digit in mapping.items(): 
            expr = expr.replace(letter, str(digit)) 
        left, right = expr.split('=') 
        if any(term[0] == '0' for term in left.split('+') + [right]): 
            continue   
        if eval(left) == eval(right): 
            return mapping   
    return None   
def main(): 
    equation = input("Enter cryptarithmetic equation (e.g., 'SEND + MORE = MONEY'): ") 
    solution = solve_cryptarithm(equation) 
    if solution: 
        print("Solution found:") 
        for letter, digit in sorted(solution.items()): 
            print(f"{letter} = {digit}") 
    else: 
        print("No solution found.") 
if __name__ == "__main__": 
    main() 
