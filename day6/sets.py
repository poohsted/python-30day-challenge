tools = {"wrench", "screwdriver", "drill"}
tools.add("drone")
tools.add("drone") # Won't add again

print(tools) # Unordered, unique values

#  Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
