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

    current_ip_address = {'NAMESERVER' : 'DIRECCIONIP', 
                          'SERVER1' : '192.168.3.100'
                         }  
    
    for key, value in current_ip_address.items():
        if ping_ip(value):
            print(f"{value} {key} ONLINE ")
            
        else:
            print(f"{value} {key}   OFFLINE")
          
          

