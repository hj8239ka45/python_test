#!/usr/bin/env python
'''
Pymodbus Asynchronous Server Example
------------------------------------------------------
The asynchronous server is a high performance implementation using the
twisted library as its backed. This allows it to scale to many thousands
of nodes which can be helpful for testing monitoring software.
'''
##import tkinter as tk
##window = tk.Tk()
##window.title('Modbus_Server')
##window.geometry('300x200')
##
##e = tk.Entry(window,show='*')
##e.pack()
##
##def insert_point():
##    var = e.get()
##    t.insert('insert',var)
##def insert_end():
##    var = e.get()
##    t.insert('end',var)
##
##b1 = tk.Button(window,text='insert point',width=13,height=2,command=insert_point)
##b1.pack()
##b2 = tk.Button(window,text='insert end',width=13,height=2,command=insert_end)
##b2.pack()
##t = tk.Text(window,height=2)
##t.pack()
##window.mainloop()


from pymodbus.server.async import StartTcpServer
from pymodbus.server.async import StartUdpServer
from pymodbus.server.async import StartSerialServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext,ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer,ModbusAsciiFramer
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0,[17]*100),
        co = ModbusSequentialDataBlock(0,[17]*100),
        hr = ModbusSequentialDataBlock(0,[17]*100),
        ir = ModbusSequentialDataBlock(0,[17]*100)
        )

context = ModbusServerContext(slaves = store, single = True)
identity = ModbusDeviceIdentification()
identity.VendorName = 'Pymodbus'
identity.ProductCode= 'PM'
identity.VendorUrl  = 'http://github.com/bashwork/pymodbus/'
identity.ProductName= 'Pymodbus Server'
identity.ModelName  = 'Python Server'
identity.MajorMinorRevision = '1.0'
StartTcpServer( context, identity = identity, address = ("127.0.0.1",5020))




