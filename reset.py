#!/usr/bin/env/python

import serial
import os
import argparse


parser = argparse.ArgumentParser(description='Reset the ublox GPS module NE0-0-01 via binary commands')
parser.add_argument('--bbr', required=True, choices=['hot', 'warm', 'cold'], help='Specify the BBR sections to clear. Options: hot - warm - cold')
args = parser.parse_args()


if args.bbr is None:
    print '*************** \nNo arguments provided - try again. --bbr value is required!'
    print '\n--bbr options: \nhot \nwarm \ncold\n'
    exit()
else:

    try:
        gps_com = serial.Serial('/dev/ttyO5', 115200)
        print 'Resetting GPS...'

        # bbr = 0xffff
        if args.bbr == 'cold':
            print 'Sending cold restart...'
            gps_com.write('\xb5\x62\x06\x04\x04\x00\xff\xff\x00\x00\x0c\x5d')

        # bbr = 0x0000
        elif args.bbr == 'hot':
            print 'Sending hot restart...'
            gps_com.write('\xb5\x62\x06\x04\x04\x00\x00\x00\x00\x00\x0e\x64')

        # bbr = 0x0001
        elif args.bbr == 'warm':
            print 'Sending warm restart...'
            gps_com.write('\xb5\x62\x06\x04\x04\x00\x00\x01\x00\x00\x0f\x67')

        gps_com.close()

    except Exception as e:
        print str(e)

