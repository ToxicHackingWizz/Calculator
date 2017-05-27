# Date: 5/27/17
# Author: ToxicProgrammer
# Description: basic Calculator
#
class Calculator(object):
 def __init__(self, num, num2):
  self.alpha = max(num,num2)
  self.omega = min(num,num2)

 def Addition(self):
  return self.alpha+self.omega

 def subtraction(self):
  return self.alpha-self.omega

 def Multiplication(self):
  return self.alpha*self.omega

 def Division(self):
  return self.alpha/self.omega

def clear():
 for n in range(200):print('\n')

def main():
 x = input('\n\nEnter first number: ')
 y = input('Enter second number: ')
 s = raw_input('\n\na = +\ns = -\nm = x\nd = /\nEnter sign: ').lower()
 clear()
 calc=Calculator(x, y)
 ans=calc.Addition() if s=='a' else calc.subtraction() if s=='s' else calc.Multiplication() if s=='m' else calc.Division() if s=='d' else 'unknown sign'
 print '{} {} {} = {}'.format(calc.alpha,'+' if s=='a' else '-' if s=='s' else 'x' if s=='m' else '/' if s=='d' else None,calc.omega,ans)

if __name__ == '__main__':
 while 1:
  try:main()
  except:
   clear()
   exit('[-] Exiting ...')
