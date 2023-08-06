class SimpleBleDevice(object):
    """This is a conceptual class representation of a simple BLE device
    (GATT Server). 
    
    """

    def __init__(self, client, addr=None, addrType=None, iface=0,
                 data=None, rssi=0, connectable=False, updateCount=0):
        """Constructor method
        """
        
    def disconnect(self):
        """Drops existing connection to device
        """
        super().disconnect()
        self._connected = False
