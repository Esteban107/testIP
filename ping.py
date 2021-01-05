#!/usr/bin/env python
import subprocess
import platform
    

def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 2 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False
 
if __name__ == '__main__':
    """current_ip_address = ['192.168.2.1', '192.168.3.1', '192.168.5.1', '192.168.6.1', '192.168.7.1']"""

    current_ip_address = {'OBISPADO' : '192.168.2.1', 
                          'PLAZA VITA' : '192.168.3.1', 
                          'PLANTA 1' : '192.168.5.1', 
                          'PLANTA 2' : '192.168.6.1', 
                          'CEDIS' : '192.168.7.1' }  
    
    for key, value in current_ip_address.items():
        if ping_ip(value):
            print(f"{value} {key} ONLINE ")
            #print(value , ":", current_ip_address[value])
            
        else:
             #print(f"{value} : {current_ip_address.keys()} ONLINE")
            print(f"{value} {key}   OFFLINE")
          
          

