# eztcp_modbus_py
## Internet Remote Switching with ezTCP via Modbus/TCP (Python 3)

by Oliver Thamm - [Elektronikladen Microcomputer](https://elmicro.com)<br>
https://github.com/elmicro/eztcp_modbus_py

### Description

This test example demonstrates how to access an ezTCP Remote I/O-Controller model
[CIE-H10](https://elmicro.com/de/ezcieh10.html) / [CIE-H12](https://elmicro.com/de/ezcieh12.html) /
[CIE-H14](https://elmicro.com/de/ezcieh14.html) (Sollae Systems) via Modbus/TCP protocol using Python 3

### Usage
```
python eztcp_modbus.py
```
### Dependencies

Requires EasyModbusTCP/UDP/RTU Python by Stefan Rossmann:
* https://github.com/rossmann-engineering/EasyModbusTCP.PY
* https://sourceforge.net/projects/easymodbustcp-udp-rtu-python/

To install, just place ZIP contents into same directory.

### CIE-H1x Configuration

#### Network settings
* use ezManager tool (Windows) to select basic IP settings matching your local network configuration

#### I/O Port settings
* Modbus/TCP enabled
* Slave
* unit = 1
* output port base = 9
* passive connection
* local port 502

### Copyright, License
This software is Copyright (C)2017 by ELMICRO - https://elmicro.com<br>
and may be freely used, modified and distributed under the terms<br>
of the MIT License - see accompanying LICENSE.md for details

### References
[1] Wikipedia: [Modbus communications protocol](https://en.wikipedia.org/wiki/Modbus)<br>
[2] Sollae Systems - [ezTCP](https://www.eztcp.com/en/home/)
