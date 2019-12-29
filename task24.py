def myfunc():
    name = input()
    if name == name[::-1]:
        return "YES"
    else:
        return "NO"
print(myfunc())