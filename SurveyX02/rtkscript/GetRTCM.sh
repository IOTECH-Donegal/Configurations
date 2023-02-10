echo *** JOR: Getting RTCM from RTK2GO and sending to ACM0 ***

./str2str -in ntrip://rtk2go.com:2102/Umricam 
# -out serial://ttyACM0:115200:8:n:1:
exit 0
