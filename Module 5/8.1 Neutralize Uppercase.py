def upper1(str):
    uppervar=0
    for i in str[:4]:
        if i.upper()==i:
            uppervar+=1
    if uppervar>=2:
        return str.upper()
    return str

print(upper1("PyThon"))

var2="Python code"
print(var2.capitalize())
name="Python"
name2="code"
print(name.capitalize())
print(name2.capitalize())