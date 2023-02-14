# SBC for Survey26
SBC is a RPi 3B+ running a generic 32-bit version of Raspbian.
A WittyPi3 board was added for RTC, Power management and auto power.
A Moitessier v1 board is used for GNSS and AIS logging.

1. A USB key is burned with latest Raspbian32.
2. The key is inserted to a USB port and the board booted.
3. Ethernet cable connected.
6. Device name set as Survey26.
7. Standard username and password, see JOR for details.
8. System is shutdown and powered off.
9. A WittyPi3 board is added and the system is powered via this board.
10. Using Raspberry Pi Configuration GUI, SSH and VNC are enabled, Serial port is enabled, Serial console is disabled.
11. The system is rebooted.

## WittyPi3v2 Configuration
1. A CR2032 battery is added to the board.
2. Drivers are added using
```shell
sudo wget http://www.uugear.com/repo/WittyPi3/install.sh
sudo sh install.sh
```
2. After installation, the SBC is rebooted.
3. The management utility is run.
```shell
cd wittypi/
./wittyPi.sh
```
4. Option 1, write system time to RTC to set the clock.
5. Set the voltage thresholds, depending on the PSU.
6. Set autoshutdown. 
7. I want the system to shut off at 22:00 every day, I use the string **?? 22:00**
8. I want the system to start up at 06:00 every day, I use the string **?? 06:00:00**

## Moitessier Configuration
The simplest way to utilize this board is to isolate pins 27, 28 of the GPIO.
The EEPROM on the Moitessier is prevented from connecting to the RPi and the HAT thinks it is working in standalone mode.

