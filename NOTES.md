Ublox GPS module was used with a BeagleBoneBlack system.

******************************
Useful commands - BeagleBone
******************************
# To check current baud rate
stty -F /dev/tty[##]

# To set baud rate
stty -F /dev/tty[##] [baud rate]

# If using gpsd service - ensure gpsd does not overwrite baud rate settings via the following mod:
# Note: This was tested with gpsd version 3.11-3 (deprecated)
/etc/default/gpsd
GPSD_OPTIONS="-b"

******************************
Useful commands - Ublox
******************************
# To query GPS module version information
gps_com.write('\xb5\x62\x0A\x04\x00\x00\x0E\x34')

# Generate ubx checksum -- credit for this section goes to sdamashek
# Calculates the Fletcher-16 checksum of *cmd*, default modulus 255
ck_a = 0
ck_b = 0

for i in cmd:
    ck_a += ord(i)
    ck_b += ck_a
    ck_a &= 0xff
    ck_b &= 0xff
    print hex(ck_a)
    print hex(ck_b)
return hex(ck_a), hex(ck_b)

