
# creation of array
array1 = [1, 2, 3, "thimphu", 2.5]

# retrieving
element1 = array1[0]
element2 = array1[4]
lastElement = array1[-5]
# print(lastElement)

# modifying elements
# array1[0] = 10

# getting number of elements in an array
no_of_elements = len(array1)

# slicing
elements = array1[0:3]
# print(elements)

arr1 = [1,10]
arr2 = ['thimphu', 'wangdue']

number_to_check = 1
result = number_to_check in arr1
# print('result is', result)

arr3 = arr2 + arr1
# print(arr3)


stackVar = []
# adding to stack
stackVar.append(4) 
stackVar.append(2) 
stackVar.append(9) 
stackVar.append(12387682376487264872364872364) # 4, 2, 9, 1 
print('After appending', stackVar)
element = stackVar.pop()
print('After popping', stackVar)
print('removed element:', element)



