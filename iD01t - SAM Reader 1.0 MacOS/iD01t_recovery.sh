#!/bin/bash

echo "iD01t FRP TOOL 1.0"
echo ""

# Check if ADB is installed
if ! command -v adb &> /dev/null; then
    echo "ADB not found, installing Android Platform Tools..."
    brew install android-platform-tools
fi

# Check for connected ADB devices
echo "Checking for connected devices..."
adb_devices=$(adb devices | awk 'NR>1 {print $1}' | grep -v '^$')

if [ -z "$adb_devices" ]; then
    echo "No devices/emulators found. Please check if:"
    echo "  - Your device is connected via USB."
    echo "  - USB Debugging is enabled on the device."
    echo "  - Device drivers are properly installed."
    exit 1
else
    echo "Connected device found: $adb_devices"
fi

# Reboot to recovery mode
echo ""
echo "Rebooting the device into Recovery Mode..."
adb reboot recovery
sleep 10  # Wait for the device to reboot into recovery


echo ""
echo "Process complete."
