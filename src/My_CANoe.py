# Import CANoe module
from py_canoe import CANoe
import time

# create CANoe object
canoe_inst = CANoe()

# open CANoe configuration. Replace canoe_cfg with yours.
canoe_inst.open(canoe_cfg=r'C:\Users\viktoriia.taraniuk\PycharmProjects\Udemy\CANoe\pythonProject1\CANoe_test\CAN_500kBaud_1ch.cfg')

# print installed CANoe application version
#canoe_inst.get_canoe_version_info()

#canoe_inst.open(canoe_cfg=fr'CANoe_test\CAN_500kBaud_1ch.cfg', visible=True, auto_save=False, prompt_user=False)
canoe_inst.start_measurement()

#sig_full_name = canoe_inst.get_signal_full_name(bus='CAN', channel=1, message='msg_OperationTime', signal='Seconds')


sig_val = canoe_inst.get_signal_value(bus='CAN', channel=1, message='msg_OperationTime', signal='Seconds', raw_value=True)
print(f"MY_VALUE: {sig_val} ")

time.sleep(5)

sig_val = canoe_inst.get_signal_value(bus='CAN', channel=1, message='msg_OperationTime', signal='Seconds', raw_value=True)
print(f"MY_VALUE: {sig_val} ")


canoe_inst.stop_measurement()


# get signal value. Replace arguments with your message and signal data.
#sig_val = canoe_inst.get_signal_value('CAN', 1, 'LightState', 'Minutes')
#print(sig_val)

canoe_inst.get_can_bus_statistics(channel=1)

# Stop CANoe Measurement
canoe_inst.stop_measurement()

# Quit / Close CANoe configuration
canoe_inst.quit()