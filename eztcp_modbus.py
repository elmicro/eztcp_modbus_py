#!/usr/bin/env python

#-----------------------------------------------------------------------------
#
#   Test example to access an ezTCP Remote I/O-Controller
#   Sollae Systems model CIE-H10 / CIE-H12 / CIE-H14
#   via Modbus/TCP protocol using Python 3
#
#   by Oliver Thamm - Elektronikladen Microcomputer
#   https://github.com/elmicro/eztcp_modbus_py
#
#   Requires EasyModbusTCP/UDP/RTU Python by Stefan Rossmann
#   https://github.com/rossmann-engineering/EasyModbusTCP.PY
#   https://sourceforge.net/projects/easymodbustcp-udp-rtu-python/
#
#   This software is Copyright (C)2017 by ELMICRO - https://elmicro.com
#   and may be freely used, modified and distributed under the terms of
#   the MIT License - see accompanying LICENSE.md for details
#
#-----------------------------------------------------------------------------

'''
CIE-H1x Configuration
---------------------
Network settings:
- use ezManager tool (Windows) to select basic IP settings
  matching your local network configuration
I/O Port settings:
- Modbus/TCP enabled
- Slave
- unit = 1
- output port base = 9
- passive connection
- local port 502
'''

import time
from ModbusClient import *

ip_addr = '192.168.178.222'
tcp_port = 502
addr_out = 9

eztcp = ModbusClient(ip_addr, tcp_port)
eztcp.Connect()
eztcp.WriteSingleCoil(addr_out, True)
time.sleep(1)
eztcp.WriteSingleCoil(addr_out, False)
eztcp.close()
