#JayLMDubyew 2022
import re as r
import collections

ipattempts = collections.defaultdict(int)
userattempts = collections.defaultdict(int)
combined = collections.defaultdict(set)

with open("auth.log") as file:
    blob = file.read()

    fails = r.findall(r'Invalid user (\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',blob)
    for i in fails:
        #print(f"failed: {i[0]} from {i[1]}")
        userattempts[i[0]] += 1
        ipattempts[i[1]] += 1
        combined[i[0]].add(i[1])
    #print(userattempts)
    #print(ipattempts)

for k,v in ipattempts.items():
    print(f"Address {k} attempted {v} times")
for k,v in userattempts.items():
    print(f"User {k} attempted {v} times")
for k,v in combined.items():
    print(f"User {k} attempted logins from {len(v)} address(es): {v}")