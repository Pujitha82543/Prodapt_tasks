print("Welcome to Day 5 Python Core !")
x=1
print(x+1)
print(eval("x+1"))

a=5
b=5
print(a==b)
print(a is b)
print(id(a))
print(id(b))

expression = "10 * 20"
print(expression) #10 * 20
print(eval(expression)) #200

#eval example
expression = input("Enter an expression to evaluate: ")
#"15 * 7" => 105

result = eval(expression)
print("Answer:", result)