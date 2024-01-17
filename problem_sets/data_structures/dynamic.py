def fibs(n):
  """"fib with memoisation"""
  memo = {}
  def helper(n):
    if memo.get(n):
      return(memo[n])
  
    if n <= 2:
      return 1
    res = helper(n-1) + helper(n-2)
    memo[n] = res
    return res
    
  
  return helper(n)
  
  
  
  
print(fibs(100))