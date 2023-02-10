echo *** JOR: Sending RTCM from ACM0 to RTK2GO ***

./str2str -in serial://ttyACM0:115200:8:n:1: -out ntrips://rtk2go.com:2101/Umricam
exit 0
