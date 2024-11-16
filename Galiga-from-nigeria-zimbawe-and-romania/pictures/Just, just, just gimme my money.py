'''


Date done: 8/29/2024 Problem 1-5

 def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return (a_smile==b_smile)
  
def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

def diff21(n):
  if (n >21):
    return (n-21)*2
  else:
    return 21-n

def makes10(a, b):
  if(a==10):
    return True
  if(b==10):
    return True
  if(a+b==10):
    return True
  return False  

'''


def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return (a_smile==b_smile)

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

def diff21(n):
  if (n >21):
    return (n-21)*2
  else:
    return 21-n

def makes10(a, b):
  if(a==10):
    return True
  if(b==10):
    return True
  if(a+b==10):
    return True
  return False  



# I finsihed problems 1-5, the rest of the problems I had trouble with. I would like to you to help me with the rest if you can.





'''
9/11/2024: Date the assignment was done

def make_bricks(small, big, goal):
  return goal % 5 <= small and goal - big * 5 <= small


  def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
  def fix_teen(n):
    if n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
      return 0
    return n


def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(num):
  if num % 10 >= 5:
    return num + 10 - (num % 10)
  return num - (num % 10)


Any problmems that I did not give an awnser was too hard for me to solve


'''


def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(num):
  if num % 10 >= 5:
    return num + 10 - (num % 10)
  return num - (num % 10)
































