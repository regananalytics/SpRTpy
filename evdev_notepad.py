import evdev

# Scan Devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

# Identify Keybaord
potential_keyboards = [d for d in devices if 'keyboard' in d.name.lower()]

# Use first
keyboard = potential_keyboards[0]
device = evdev.InputDevice(keyboard.path)
print(device)

# Collect keys in loop
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
