# ble_scan_connect.py:
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev , isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
addr=[]
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr , dev.addrType , dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype , desc , value) in dev.getScanData():
        print (" %s = %s" % (desc,value))

number = input('Enter your device number: ')
print ('Device', number)
num = int (number)
print (addr[num])
#
print ("Connecting...")
dev = Peripheral(addr[num], 'random')
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#
try:
    service = dev.getServiceByUUID(UUID(0xfff0))
    for ch in service.getCharacteristics():
        print(str(ch))
#
    
    ch = dev.getCharacteristics(uuid=UUID(0xfff4))[0]

    desc = ch.getDescriptors(forUUID=0x2902)[0]
    print("Original CCCD:", desc.read())
    desc.write(b"\x00\x02")
    print("Modified CCCD:", desc.read())

    # if ch.supportsRead():
    #     while True:
    #         if dev.waitForNotifications(1.0):
    #             print("notify")

    #if (ch.supportsRead()):
        #print(ch.read())
#
finally:
    dev.disconnect()
