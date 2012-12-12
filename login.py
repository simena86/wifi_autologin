#!/usr/bin/python
import requests
import sys

#
# AUTO LOGIN TO UCSB NETWORK
#
print "This is an automatic login to ucsb school network"
URL='https://login.wireless.ucsb.edu/login.html' 
EMAIL = 'foo'
PASSWORD = 'bar'

# form post data
headers={'Connection':'keep-alive',
		 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.04 Chromium/18.0.1025.151 Chrome/18.0.1025.151',
         'Referer: https':'//login2.wireless.ucsb.edu/?switch_url=https://login.wireless.ucsb.edu/login.html&ap_mac=00:1e:f7:54:fb:10&client_mac=38:59:f9:30:53:f1&          wlan=UCSB%20Wireless%20Web&redirect=www.linuxmint.com/start/katya/',
		 }

def main():
    # Start a session with persistant cookies
    session = requests.session(config={'verbose': sys.stderr})
    login_data = {
        'username': EMAIL,
        'password': PASSWORD,
        'buttonClicked':'4',
		'redirect_url':'www.linuxmint.com%2Fstart%2Fkatya%2',
		'err_flag':'0',		
    }
    r = session.post(URL, data=login_data, headers=headers, timeout=10.00)

if __name__ == '__main__':
    main()
