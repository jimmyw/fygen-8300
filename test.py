import fygen
fy = fygen.FYGen('/dev/ttyUSB0', debug_level=1, device_name="fy8300")
#print(fy.get_id())
print(fy.get_model())
fy.set(channel=0, wave='sin', freq_hz=50, enable=True, phase_degrees=0, volts=15)
fy.set(channel=1, wave='sin', freq_hz=50, enable=True, phase_degrees=120, volts=15)
fy.set(channel=2, wave='sin', freq_hz=50, enable=True, phase_degrees=240, volts=15)

