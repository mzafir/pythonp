dic1 = {"a": 234, "b": 393}
dic2 = {"b": 393, "a": 777}
"""
for key, value in set(dic1) & set(dic2):
    if dic1[key] ==dic2[key]:
        print (key, value)
"""

for key, value in dic1.items():
    if dic2[key] == dic1[key]:
        print("all keys are match")
    else dic2[key] != dic1[key]:
        print("")


