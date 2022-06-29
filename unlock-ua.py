# -*- coding: utf-8 -*-

# open source code 
# get random user_agent by Dekura 
# source api : https://api.apilayer.com
# report bug program nimetuber@gmail.com

##############################
# linux: true/false          #
# windows: true/false        #
# mac: true/false            #
# android: true/false        #
# chrome: true/false         #
# firefox: true/false        #
# mobile: true/false         #
# desktop: true/false        #
##############################

########################################################
# APIKEY DEFAUL: 2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL
#
# JIKA API KEY DI ATAS TIDAK BISA/PROGRAM ERROR SILAHKAN AMBIL KEY SENDIRI DI WEBSITE " https://api.apilayer.com "
########################################################

# Library python #

import os,sys,json 
import requests as req 


# Url & Headers website #

url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}

# Main menu #

os.system('clear')
try:
    response = req.get(url,headers=header)
    if response.status_code == 200:
        print(f"\n\n ✓ user-agent: {response.json()['ua']}")
    else:
        print('\n ! terjadi masalah pada status code');exit()
except req.exceptions.ConnectionError:
    print('\n ! tidak ada jaringan');exit()
