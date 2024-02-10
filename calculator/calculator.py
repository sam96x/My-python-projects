import os

def sum(num1, num2):
  return num1 + num2
def substract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2

operations = {
  "+": sum,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calc_function(num1, num2, operator):
  if operator == "+":
    return num1+num2
  elif operator == "-":
    return num1-num2
  elif operator == "*":
    return num1*num2
  elif operator == "/":
    return num1/num2


def calculator():
  lets_continue = "ano"
  result = 0

  num1 = float(input("Zadajte prvé číslo: "))

  while lets_continue == "ano":
    num2 = float(input("Zadajte druhé číslo: "))
    
    for operator in operations:
      print(operator)
    
    operator = input("Zadajte operáciu: ")

    calc_function = operations[operator]
    result = calc_function(num1, num2)
    print(f"{int(num1)} {operator} {int(num2)} = {result}")
    
    lets_continue = input("Chcete pokračovať? Ak áno, napíšte ano, ak nie, tak nie: ")
    
    num1 = result
    
    if lets_continue == "nie":
      os.system("clear")
      calculator()

calculator()