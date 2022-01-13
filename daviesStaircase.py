
result = dict() #creates empty object
result[1] = 1
result[2] = 2
result[3] = 4 #possible permutation of steps using 1, 2 or 3 steps


def stepPerms(n):
    if n == 0:
        return 0
    if n in result.keys(): #if n exists already return the value of n (memoization), else assign new key with n 
        return result[n] 
    result[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3) #next amt of ways = sum of prev 3
    return result[n]