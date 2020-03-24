import os
import subprocess
from random import randint
import sys

_last_ip = None

# for linux
def _get_current_ip_linux(interface):
    assert isinstance(interface, str), "interface invalid"
    
    global _last_ip
    if _last_ip is None:
        p = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
        p.wait()
        contents = p.stdout.read().decode()
        _last_ip = contents.split(interface)[1].split("inet")[1].split(" ")[1]
    return _last_ip

def _change_IP_linux(interface):
    global _last_ip

    current_ip = _get_current_ip_linux(interface)
    end = str(randint(0, 255))
    while(end==current_ip.split(".")[3]):
        end = str(randint(0, 255))
    _last_ip = "{}.{}.{}.{}".format(
        current_ip.split(".")[0],
        current_ip.split(".")[1],
        current_ip.split(".")[2],
        str(end)
    )
    return _last_ip

def _set_ip_linux(interface):
    new_ip = _change_IP_linux(interface)
    os.system("sudo ifconfig {} {}".format(
        interface,
        new_ip
    ))
    p = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
    p.wait()
    print(p.stdout.read().decode())

# for win
def _get_current_ip_win(interface):
    assert isinstance(interface, str), "interface invalid"
    
    global _last_ip
    if _last_ip is None:
        p = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
        p.wait()
        contents = p.stdout.read()
        _last_ip = contents.split(interface)[1].split("IPv4 地址")[1].split(":")[1].split("Subnet")[0].split("\r")[0]
    return _last_ip

def _change_IP_win(interface):
    global _last_ip

    current_ip = _get_current_ip_win(interface)
    end = str(randint(0, 255))
    while(end==current_ip.split(".")[3]):
        end = str(randint(0, 255))
    _last_ip = "{}.{}.{}.{}".format(
        current_ip.split(".")[0],
        current_ip.split(".")[1],
        current_ip.split(".")[2],
        str(end)
    )
    return _last_ip

def _set_ip_win(interface):
    
    new_ip = _change_IP_win(interface)
    gateway = "{}.{}.{}.1".format(
        new_ip.split(".")[0],
        new_ip.split(".")[1],
        new_ip.split(".")[2]
    )
    os.system("netsh interface ip set address name=\"{}\" static {} 255.255.255.0 {} 1".format(
        interface,
        new_ip,
        gateway
    ))
    p = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
    p.wait()
    print(p.stdout.read())
    
if __name__ == "__main__":
    if "linux" in sys.platform:
        _set_ip_linux(sys.argv[1])
    else:
        _set_ip_win(sys.argv[1])
