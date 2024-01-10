def chosen(device, command):
    if device in command or device.replace(" ", "") in command:
        return True
    else:
        return False


device_names = ["heating", "ceiling light", "spotlight", "music player"]
device_ons = [False, False, False]
device_settings = [18, 350, 7]
device_types = ["temperature", "brightness", "brightness", "volume"]

for device in device_names:
    print(f"{device} has been initialised")

name = input("What is your name? ")
print(f"Hello {name}")

while True:
    print()
    command = input(f"What next, {name}? ")
    command = f" {command.lower()} "

    if "system off" in command:
        break

    device_chosen = None
    for device in device_names:
        if chosen(device, command):
            device_chosen = device
            break

    if device_chosen is None:
        print(f"Sorry {name}, I do not understand that")
    else:
        i = device_names.index(device)
        if " on " in command:
            device_ons[i] = True
            print(device + " is on")
        elif " off " in command:
            device_ons[i] = False
            print(device + " is off")
        elif " up " in command:
            device_settings[i] += 1
            print(f" {device} {device_types[i]} is set to {device_settings[i]}")
        elif " down " in command:
            device_settings[i] -= 1
            print(f" {device} {device_types[i]} is set to {device_settings[i]}")
        elif " play " in command and device == "music player":
            print(f" {device} is playing")
        elif " pause " in command and device == "music player":
            print(f" {device} is paused")
        else:
            print(f"Sorry {name}, I do not understand that")

print(f"Bye bye, {name}")
