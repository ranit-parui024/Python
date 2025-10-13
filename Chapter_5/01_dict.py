# dict are key value pairs
marks = {
    "harry" : 100,
    "Shubham" : 20,
    "Dipan" : 29,
}

print(marks)

#print(marks["harry"])
#print(marks.items())
#print(marks.keys())
#print(marks.values())
#marks.update({"harry" : 78, "rohini": 79})

print(marks.get("harry1")) # prints none
print(marks["harry1"]) # return error
