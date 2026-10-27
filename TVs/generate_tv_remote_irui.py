import json
import sys
import hashlib
import os

button_aliases = {
    "input": ["src", "source","sources"],
    "prev": ["previous", "back", "return"],
    "rwd": ["rewind"],
    "fwd": ["forward", "fast_forward", "fast_fwd"],
    "play": ["play_pause"],
    "info": ["help"],
    "settings": ["options"]
}


for k in range(1,len(sys.argv)):
    irui = None
    with open("template.irui") as f:
        irui = json.load(f)
    sys.argv[k] = sys.argv[k].replace("\\","/")
    ir = []
    lines = None
    with open(sys.argv[k]) as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.split(": ")
        if line[0] == "name":
            ir.append({"name": line[1]})
        elif line[0] in ["type","frequency","duty_cycle","data","protocol","address","command"]:
            ir[-1][line[0]] = line[1]
    for i in range(len(ir)):
        if ir[i]["type"] == "raw":
            ir[i]["sha_256_string"] = ir[i]["type"] + ir[i]["frequency"] + ir[i]["duty_cycle"] + ir[i]["data"]
        elif ir[i]["type"] == "parsed":
            ir[i]["sha_256_string"] = ir[i]["type"] + ir[i]["protocol"] + ir[i]["address"] + ir[i]["command"]

    buttons = irui["pages"][0]["buttons"]
    navigation_index = -1
    matches = {}
    for i in range(len(ir)):
        for j in range(len(buttons)):
            if buttons[j]["data"]["type"] in ["NAVIGATION", "OK_NAVIGATION"]:
                navigation_index = j
                if buttons[j]["data"]["up_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["up_key_id"]["key_name"].lower()] if buttons[j]["data"]["up_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["up_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["up_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
                elif buttons[j]["data"]["down_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["down_key_id"]["key_name"].lower()] if buttons[j]["data"]["down_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["down_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["down_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
                elif buttons[j]["data"]["left_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["left_key_id"]["key_name"].lower()] if buttons[j]["data"]["left_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["left_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["left_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
                elif buttons[j]["data"]["right_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["right_key_id"]["key_name"].lower()] if buttons[j]["data"]["right_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["right_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["right_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
                elif buttons[j]["data"]["type"] in ["OK_NAVIGATION"] and buttons[j]["data"]["ok_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["ok_key_id"]["key_name"].lower()] if buttons[j]["data"]["ok_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["ok_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["ok_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
            elif buttons[j]["data"]["type"] in ["VOLUME", "CHANNEL"]:
                if buttons[j]["data"]["add_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["add_key_id"]["key_name"].lower()] if buttons[j]["data"]["add_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["add_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["add_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
                elif buttons[j]["data"]["reduce_key_id"]["key_name"].lower() in [ir[i]["name"].lower()] + [button_aliases[buttons[j]["data"]["reduce_key_id"]["key_name"].lower()] if buttons[j]["data"]["reduce_key_id"]["key_name"].lower() in button_aliases else []][0]:
                    buttons[j]["data"]["reduce_key_id"]["key_name"] = ir[i]["name"]
                    matches[ir[i]["name"]] = True
                    buttons[j]["data"]["reduce_key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()
            elif ir[i]["name"].lower() in [buttons[j]["data"]["key_id"]["key_name"].lower()] + [button_aliases[buttons[j]["data"]["key_id"]["key_name"].lower()] if buttons[j]["data"]["key_id"]["key_name"].lower() in button_aliases else []][0]:
                buttons[j]["data"]["key_id"]["key_name"] = ir[i]["name"]
                matches[ir[i]["name"]] = True
                buttons[j]["data"]["key_id"]["sha_256_string"] = hashlib.sha256(ir[i]["sha_256_string"].encode()).hexdigest()

            if ir[i]["name"] in matches:
                break          

    signalless_buttons = []
    i = 0
    while i < len(buttons):
        if buttons[i]["data"]["type"] in ["NAVIGATION", "OK_NAVIGATION"]:
            if buttons[i]["data"]["up_key_id"]["sha_256_string"] == "":
                signalless_buttons.append(buttons[i]["data"]["up_key_id"]["key_name"])
                buttons[i]["data"].pop("up_key_id")
            if buttons[i]["data"]["down_key_id"]["sha_256_string"] == "":
                signalless_buttons.append(buttons[i]["data"]["down_key_id"]["key_name"])
                buttons[i]["data"].pop("down_key_id")
            if buttons[i]["data"]["left_key_id"]["sha_256_string"] == "":
                signalless_buttons.append(buttons[i]["data"]["left_key_id"]["key_name"])
                buttons[i]["data"].pop("left_key_id")
            if buttons[i]["data"]["right_key_id"]["sha_256_string"] == "":
                signalless_buttons.append(buttons[i]["data"]["right_key_id"]["key_name"])
                buttons[i]["data"].pop("right_key_id")
            if buttons[i]["data"]["type"] in ["OK_NAVIGATION"] and buttons[i]["data"]["ok_key_id"]["sha_256_string"] == "":
                    signalless_buttons.append(buttons[i]["data"]["ok_key_id"]["key_name"])
                    buttons[i]["data"].pop("ok_key_id")
            if buttons[i]["data"].keys() == ["type"]:
                buttons.pop(i)
                navigation_index -= 1 if i < navigation_index else 0
                i -= 1
        elif buttons[i]["data"]["type"] in ["VOLUME", "CHANNEL"]:
            if buttons[i]["data"]["add_key_id"]["sha_256_string"] == "":
                signalless_buttons.append(buttons[i]["data"]["add_key_id"]["key_name"])
                buttons[i]["data"].pop("add_key_id")
            if buttons[i]["data"]["reduce_key_id"]["sha_256_string"] == "":
                signalless_buttons.append(buttons[i]["data"]["reduce_key_id"]["key_name"])
                buttons[i]["data"].pop("reduce_key_id")
            if buttons[i]["data"].keys() == ["type"]:
                buttons.pop(i)
                navigation_index -= 1 if i < navigation_index else 0
                i -= 1
        elif buttons[i]["data"]["key_id"]["sha_256_string"] == "":
            signalless_buttons.append(buttons[i]["data"]["key_id"]["key_name"])
            buttons.pop(i)
            navigation_index -= 1 if i < navigation_index else 0
            i -= 1
        i += 1


    buttonless_signals = []
    for i in range(len(ir)):
        if ir[i]["name"] not in matches:
            buttonless_signals.append(ir[i]["name"])

    if signalless_buttons != []:
        print("Signal not found for these buttons in " + sys.argv[k] + ":", ", ".join(signalless_buttons))

    if buttonless_signals != []:
        print("Button not found for these signals in " + sys.argv[k] + ":", ", ".join(buttonless_signals))
        print("Warning: These signals will not be sendable from the app!")
    
    navigation_wheel_incomplete = False
    if "Up" not in signalless_buttons or "Down" not in signalless_buttons or "Left" not in signalless_buttons or "Right" not in signalless_buttons:
        if "Up" in signalless_buttons or "Down" in signalless_buttons or "Left" in signalless_buttons or "Right" in signalless_buttons:
            print("Warning: Navigation wheel incomplete! Investigate issue manually in " + sys.argv[k] + "!")
            navigation_wheel_incomplete = True
        elif "Ok" in signalless_buttons:
            print("Warning: Ok button not found in " + sys.argv[k] + "!")
            buttons[navigation_index]["data"]["type"] = "NAVIGATION"
            buttons[navigation_index]["position"]["x"] += 0.33333
    
    if buttonless_signals != [] and not navigation_wheel_incomplete:
        if not os.path.exists("/".join(sys.argv[k].split("/")[:-1:]+["README.md"])):
            with open("/".join(sys.argv[k].split("/")[:-1:]+["README.md"]), "a") as f:
                f.write("# IRUI will hide some functions on mobile for these files\n\n")
        with open("/".join(sys.argv[k].split("/")[:-1:]+["README.md"]), "a") as f:
            f.write(f"* **{sys.argv[k].split("/")[-1].replace("_", "\\_")}**: {", ".join(buttonless_signals).replace("_", "\\_")}\n")

    if not navigation_wheel_incomplete:
        with open(os.path.splitext(sys.argv[k])[0] + ".irui", "w") as f:
            json.dump(irui, f)
    
    if buttonless_signals != [] or signalless_buttons != [] or "Ok" in signalless_buttons:
        input("Press enter to continue... ")
    else:
        print("Finished " + sys.argv[k] + " without issues.")
    print("---")