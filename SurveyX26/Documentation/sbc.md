# SBC for Survey26
SBC is a RPi 3B+ running a generic 32-bit version of Raspbian.
A WittyPi3 board was added for RTC, Power management and auto power.
A Moitessier v1 board is used for GNSS and AIS logging.

1. A USB key is burned with latest Raspbian 32
2. The key is inserted to a USB port and the board booted.
3. Ethernet cable connected.
4. Device name set as Survey26.
5. Standard username and password, see JOR for details.
6. System is shutdown and powered off.
7. A WittyPi3 board is added and the system is powered via this board.
8. Drivers are added using
```Shell
sudo apt update
```
