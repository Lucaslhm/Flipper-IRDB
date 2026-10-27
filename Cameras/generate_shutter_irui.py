import sys
import hashlib
import re

# Set this according to the naming scheme
correct_key_name = "Shutter"
# Ignore regex pattern before correct_key_name
ignore_key_name_prefix = r"^(\d+sec_)?"

for i in range(1,len(sys.argv)):
    original_key_name = ""
    desired_key_name = ""
    key_count = False
    with open(sys.argv[i]) as f:
        s = b""
        for e in f.read().split("\n"):
            e = e.split(": ")
            if e[0] in ["type","frequency","duty_cycle","data","protocol","address","command"]:
                s += e[1].encode()
            elif e[0] in ["name"]:
                original_key_name = e[1]
                match = re.search(ignore_key_name_prefix,original_key_name)
                if original_key_name[match.span()[1]::] != correct_key_name:
                    desired_key_name = match.group()+correct_key_name
                    key_count += 1
        s = hashlib.sha256(s).hexdigest()
        with open("".join(sys.argv[i].split(".")[:-1:] + [".irui"]), "w") as g:
            g.write("{\"pages\":[{\"buttons\":[{\"data\":{\"key_id\":{\"key_name\":\"" + correct_key_name + "\",\"sha_256_string\":\"" + s + "\",\"type\":\"SHA_256\"},\"type\":\"SHUTTER\"},\"position\":{\"alignment\":{\"center\":{}},\"containerHeight\":11,\"containerWidth\":5,\"contentHeight\":3,\"contentWidth\":3,\"x\":0,\"y\":0,\"zIndex\":1}}]}]}")
    if 1 < key_count:
        print("Warning: Multiple signals found in file. Check manually!")
    else:
        if desired_key_name:
            data = None
            with open(sys.argv[i]) as f:
                data = f.read().replace(original_key_name,desired_key_name)
            with open(sys.argv[i], "w") as f:
                f.write(data)
            print("Mismatched key name " + original_key_name + " in " + sys.argv[i] + " replaced with " + desired_key_name)

input("Finished, press enter to continue... ")