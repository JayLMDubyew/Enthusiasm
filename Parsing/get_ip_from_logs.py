## JayLMDubyew (JLMW) - 2022
import re
ipaddrs = {}
with open("auth.log","r") as log:
    line = log.read()
   # print(line)
    match = re.findall(r"((?:\d{1,3}\.){3}\d{1,3})",line)
    for i in match:
        if i in ipaddrs:
            ipaddrs[i] += 1
        else:
            ipaddrs[i] = 1

    print(ipaddrs)

