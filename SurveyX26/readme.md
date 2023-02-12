# SurveyX26 - Dredge monitor 2023
A customer requirement exists to conform with an EPA license to monitor dredge activity. 
This project is based on work done in June 2020 which was accepted under the same license.
A 10T strain gauge is mounted either in line with the plough or between the plough tow lines.
The tension is adjusted on the strain gauge such that it shows a low quiescent value and a high value when under load.
The absolute value does not matter, tests show the difference is in metric tonnes, orders of magnitude greater than any noise value. 
During post-processing, these will be translated into digital values (load/no load).

This system is based on:
-	LMS Strain Gauge
-	LMS digital display with RS232 interface
- A single board computer (SBC) used for logging, incorporating a GNSS with integrated IMU. 

This style of GNSS device has been tested in poor signal areas, without a good view of the sky (harbours, piers, caves) and has been found to maintain accurate positioning.

The system is capable of RTK accuracy (c. 1cm), but this does not need to be implemented for this application. Every second, navigational values are logged (UTC, LAT, LONG, SOG, COG) combined with a strain value. These values are also forwarded and logged to a cloud store (AWS) for redundancy. 
This data is post-processed to conform to the presentation style agreed with EPA in 2020.

