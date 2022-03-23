def add_function(a,b):
	return a+b
def sub_function(a,b):
	return a-b

a = 3
b = 5
myhtmlcode = "<h1>This is site header</h1>"
myhtmlcode += "<p> The sum of " + str(a) + " and " + str(b) + " equals " + str(add_function(a,b)) + "</p>"
myhtmlcode += "<p> The sub of " + str(a) + " and " + str(b) + " equals " + str(sub_function(a,b)) + "</p>"
with open('index.html', 'w') as file:
	file.write(myhtmlcode)
