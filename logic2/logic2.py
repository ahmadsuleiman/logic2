def make_bricks(small, big, goal):
  x=goal/5
  if big>x:
    big=x
  goal = goal-big*5
  if goal>small:
    return False
  if goal<=small:
    return True
	
def lone_sum(a, b, c):
  s=0
  if a!=b and a!=c:
    s=s+a
  if b!=a and b!=c:
    s=s+b
  if c!=a and c!=b:
    s=s+c
  return s
  
def lucky_sum(a, b, c):
  sum=0
  if a==13:
    return sum
  else: sum+=a
  if b==13:
    return sum
  else: sum+=b
  if c==13:
    return sum
  else: sum+=c
  return sum
  
def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
def fix_teen(n):
  if n>=13 and n<=19 and n!=15 and n!=16:
    return 0
  return n
  
def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c)
def round10(num):
  if num%10>=5:
    return num+abs(num%10-10)
  else:
    return num-num%10
	
def close_far(a, b, c):
  return abs(a-b)<=1 and abs(a-c)>=2 and abs(c-b)>=2 or abs(b-c)<=1 and abs(a-c)>=2 and abs(a-b)>=2 or abs(a-c)<=1 and abs(a-b)>=2 and abs(c-b)>=2
  
def make_chocolate(small, big, goal):
  x=goal/5
  if big>x:
    big=x
  goal = goal-big*5
  if goal<=small:
    return goal
  return -1