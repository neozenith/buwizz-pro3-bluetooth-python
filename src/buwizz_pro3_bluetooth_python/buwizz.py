# Standard Library
from dataclasses import dataclass

# Discovering BuWizz3 device
#
# When active, BuWizz3 device advertises main advertisement data and optional scan response data
# (shown in Figure 1). Main advertisement data contains device name (‘BuWizz3’ by default, but can be
# customized) and short manufacturer information (sequence of 8 bytes - 05:4E:’B’:’W’:’B’:’L’:00:00 in
# bootloader and 05:4E:’B’:’W’:’x’:’y’:<serialLSB>:<serialMSB> in the application, where x and y are
# replaced with firmware version and serial number contains lower 16 bits of device’s serial number).
# Scan response data contains the 128-bit UUID of the device’s main (BuWizz application) service.
#
# Service UUID
# BuWizz 93:6E:67:B1:19:99:B3:88:81:44:FB:74:D1:92:05:50
# The below is the same as above but read in reverse order.
BUWIZZ_SERVICE_UUID = "500592d1-74fb-4481-88b3-9919b1676e93"
#
# There are 6 characteristics in this service, shown in the table below. These have a data exchange
# characteristic with a data exchange descriptor and a Client Characteristic Configuration Descriptor
# (CCCD) controlling the characteristic behavior.
# Characteristic UUID Type
# Application 0x2901 Write + Notify
BUWIZZ_CHAR_UUID_APPLICATION = "50052901-74fb-4481-88b3-9919b1676e93"
# Bootloader 0x8000 Write + Notify
BUWIZZ_CHAR_UUID_BOOTLOADER = "50058000-74fb-4481-88b3-9919b1676e93"
#
# UART ch. 1 0x3901 Write + Notify
# UART ch. 2 0x3902 Write + Notify
# UART ch. 3 0x3903 Write + Notify
# UART ch. 4 0x3904 Write + Notify
BUWIZZ_CHAR_UUID_UART_CH1 = "50053901-74fb-4481-88b3-9919b1676e93"
BUWIZZ_CHAR_UUID_UART_CH2 = "50053902-74fb-4481-88b3-9919b1676e93"
BUWIZZ_CHAR_UUID_UART_CH3 = "50053903-74fb-4481-88b3-9919b1676e93"
BUWIZZ_CHAR_UUID_UART_CH4 = "50053904-74fb-4481-88b3-9919b1676e93"


# https://buwizz.com/BuWizz_3.0_API_3.6_web.pdf

COMMANDS = {
    0x20: "Set Device Name",
    # TODO: The rest of these...
    0x36: "Set LED Status",
}


@dataclass
class BuwizzDeviceStatusReport:
    # Device status report
    # Once  enabled  by  writing  1  to  data  CCCD,  the  BuWizz3  device  will  periodically  send  device  status
    # report with the approximate frequency of 20 Hz
    # Byte Array Byte numbers and values:
    # 0 (command) 0x01
    # 1 Status flags - bit mapped to the following functions:
    #   Bit Function
    #       7 unused
    #       6 USB connection status (1 - cable connected)
    #       5 Battery  charging  status  (1  -  battery  is  charging, 0 - battery is full or not charging)
    #       3-4 Battery  level  status  (0  -  empty,  motors  disabled;  1  -  low;  2  -  medium;  3  - full)
    #       2 BLE long range PHY enabled
    #       1 unused
    #       0 error (overcurrent, overtemperature...)
    #
    # 2 Battery voltage (9 V + value * 0,05 V) - range 9,00 V – 15,35 V
    # 3-8 Motor currents, 8-bit value for each motor output (value * 0,015 A) - range 0 - 3,8 A
    # 9 Microcontroller temperature (value in °C)
    # 10-11 Accelerometer x-axis value (left-aligned 12-bit signed value, 0.488 mg/digit)
    # 12-13 Accelerometer y-axis value (left-aligned 12-bit signed value, 0.488 mg/digit)
    # 14-15 Accelerometer z-axis value (left-aligned 12-bit signed value, 0.488 mg/digit)
    # 16 Bootloader response command
    # 17 Bootloader response code
    # 18-20 Bootloader response data (3 bytes)
    # 21 Battery-charge current (mA)
    # 22-53 PoweredUp motor data structure (4x)
    # - Motor type (unsigned 8-bit)
    # - Velocity (signed 8-bit)
    # - Absolute position (unsigned 16-bit)
    # - Position (unsigned 32-bit)
    # 54-67 Optional: PID controller state
    # - Process value (single precision float)
    # - Error (float)
    # - PID output (float)
    # - Integrator state (signed 8-bit int)
    # - Motor output (signed 8-bit int)
    ...


def handle_notify_device_status_report(data: bytearray) -> BuwizzDeviceStatusReport:
    """Decode byte array data into Device Report."""
    return BuwizzDeviceStatusReport()
