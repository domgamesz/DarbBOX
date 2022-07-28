#!/usr/bin/env python3
import os
os.system("pip install subprocess") 
import subprocess
import time
import sys
e = 1
cd = os.getcwd()
kool = time.localtime()
coop = time.strftime("%H:%M:%S", kool)
subprocess.call(f"chmod +x darbbox.py", shell=True)
print("Darbbox started at: " + coop)
sss = input("install packages? (y/n): ")
def l():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    for i in range(e):
        sys.stdout.write("▮") # prints a dash for each iteration of loop
        sys.stdout.flush() # ensures bar is displayed incrementally    
    print("    ")
if "y" in sss:
    l()
    subprocess.call("sudo apt-get install -y lolcat", shell=True)
    l()
    e = 1 + 1
    subprocess.call("sudo apt-get install python3-numpy python3-scipy python3-matplotlib ipython3 python3-notebook python3-pandas python3-sympy python3-nose", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install blessed", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install colorama", shell=True)
    l()
    e = e + 1
    subprocess.run(f"pip install matplotlib", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install pygame", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install os-sys", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install pickle-mixin", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install openai", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install pytest-shutil", shell=True)
    l()
    e = e + 1
    subprocess.call("pip install paraphraser", shell=True)
    l()
    e = e + 1
    subprocess.call("pip3 install --user gif-for-cli", shell=True)
    l()
    e = e + 1
    subprocess.call("pip3 install psutil", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install elinks", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt-get install festival", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install pyfestival", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install neofetch", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install vim", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install jp2a", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install imagemagick", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install mpv", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install boxes", shell=True)
    l()
    e = e + 1
    subprocess.call("sudo apt install git", shell=True)
    l()
    subprocess.call("sudo apt-get install curl", shell=True)
    e = e + 1
    subprocess.call("git clone https://github.com/piotrkira/terminal-3d-viewer.git", shell=True)
    l()
    e = e + 1
    
elif "n" in sss:
    print("Starting without installing packages")

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
import time
from blessed import Terminal
term = Terminal()
import psutil
import platform
from datetime import datetime
import os
import random
import time
from pygame import mixer
import shutil
import colorama
import sys
from colorama import Fore, Back, Style
import pickle
from paraphraser import paraphrase
import subprocess
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()
def anything(str):
    text = str
    r = 0
    g = 0
    b = 0
    for letter in str:
        sys.stdout.write((colored(r, g, b, letter)))
        sys.stdout.flush()
        time.sleep(0.0002)
        r = r + 1
        g = g + 1
        b = b + 1
    
anything("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▓█████████░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▓████████████░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▒▓████████████▓▓▒▓░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▓██████████████▒▒▓▓▒▒▒░░░░░░░░░░░
░░░░░░░░░▒▒▒▓▓██████████████▓▓▒▓█▓▒▓▓▓▓▒▒▒░░░░░░░░
░░░░░░░░░▓████████████████▓▒▓▓▓▓▒▓▓▓▓▒▓▓▓▒▓▓▒▒▒░░░
░░░░░░▓█████████████████▓▒▓▓▓▒▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓█▓▓▒░
░░░░▒▓███████████████▓▓▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓░░░
░░░▓██████████████▓▓▓▓▓▓▒▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓█▓▓▓▒░░░░░
░░░█████████████▓▒▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓░░░░░░░░
░░▒██████████▓▓▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▓█▓░░░░░░░░░░
░░▒███████▓▓▒▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓█▓▓▓█▒░░░░░░░░░░░░
░░░▓████▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▓▓█▓▓█▓▒░░░░░░░░░░░░░░
░░░░██▓▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▓█▓▓▓█▓░░░░░░░░░░░░░░░░░
░░░▒██▓▓█▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓█▓▓▓█▓▒░░░░░░░░░░░░░░░░░░░
░░░░███▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓█▓▓██▒░░░░░░░░░░░░░░░░░░░░░░
░░░░░▒▒▓███▓▓▓▓▓▓▓▓█▓▓▓█▓▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▒▓▓██▓▓▓▓▓██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▒▓██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Starting...
""")
def anything(str):


  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.01)
time.sleep(1)
clearConsole()
print(Back.RED + "_________________________________________________________")
print(Back.RESET + " ")
print(Fore.WHITE, """DarbBOX    MADE IN 🐍 PYTHON  
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
    .,,,,,,,,,,,. ...........           ............ .,,,,,,,,,,,.    
    .,. ...   ,,. ...........           ............ .,,   ... .,.    
    .,. .  .. ,,. ...........           ............ .,, ..  . .,.    
    .,.       ,,. ...........           ............ .,,       .,.    
    ............  ...........            ...........  ............                                                                               
type "/help" for a list of commands
""")
print(Back.RED + "_________________________________________________________")
print(Back.RESET + " ")
mixer.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
while True:
    comm = input(Back.RESET + os.getlogin() + " | DarbBOX: ")
    print(Back.RESET + "  ")
    if "/time" in comm:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
    elif "/font" in comm:
        subprocess.run("ls /usr/share/consolefonts", shell=True)
        pop = input("// Font?: ")
        subprocess.run(f"setfont /usr/share/consolefonts/{pop}", shell=True)
    elif "/text" in comm:
        subprocess.call("vim", shell=True)
    elif "dafuqisdis" in comm:
        print("its a seckreat u glizzy gobilin bafoon")
    elif "/files" in comm:
        subprocess.run(f"ls > output.txt", shell=True)
        with open('output.txt') as f:
            contents = f.read()
            print(contents)
    elif "/clear" in comm:
        clearConsole()
        print(Back.RED + "_________________________________________________________")
        print(Back.RESET + " ")
        print(Fore.WHITE, """DarbBOX    MADE IN 🐍 PYTHON
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
    .,,,,,,,,,,,. ...........           ............ .,,,,,,,,,,,.    
    .,. ...   ,,. ...........           ............ .,,   ... .,.    
    .,. .  .. ,,. ...........           ............ .,, ..  . .,.    
    .,.       ,,. ...........           ............ .,,       .,.    
    ............  ...........            ...........  ............                                                                               
type "/help" for a list of commands
""")
        print(Back.RED + "_________________________________________________________")
        print(Back.RESET + " ")
    elif "/print" in comm:
        e = input("// print?: ")
        print(e)
    elif "/date" in comm:
        subprocess.call("cal", shell=True)
    elif "/sys-info" in comm:
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")
        print("="*40, "CPU Info", "="*40)
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")
        print("="*40, "Memory Information", "="*40)
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"Used: {get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")
        print("="*40, "Disk Information", "="*40)
        print("Partitions and Usage:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            print("e")
        #aaaaaaaaaaaaaaaaaaaaaaaaaa    
        continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {get_size(disk_io.read_bytes)}")
        print(f"Total write: {get_size(disk_io.write_bytes)}")
        print("="*40, "Network Information", "="*40)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    elif "/speak" in comm:
        sus = input("// say?: ")
        os.system('echo "{0}" | festival --tts'.format(sus))
    elif "/sprint" in comm:
        a = input("// sprint?: ")
        print(a)
        os.system('echo "{0}" | festival --tts'.format(a))
    elif "/diskspace" in comm:
        total, used, free = shutil.disk_usage(__file__)
        print(total, used, free)
    elif "/color-red" in comm:
        print(Fore.RED, "DarbBOX")
    elif "/color-yellow" in comm:
        print(Fore.YELLOW, "DarbBOX")
    elif "/color-green" in comm:
        print(Fore.GREEN, "DarbBOX")
    elif "/color-blue" in comm:
        print(Fore.BLUE, "DarbBOX")
    elif "/color-purple" in comm:
        print(Fore.MAGENTA, "DarbBOX")
    elif "/color-white" in comm:
        print(Fore.WHITE, "DarbBOX")
    elif "/run" in comm:
        d = input("// run app?: ")
        os.system(d)
    elif "/add" in comm:
        num = int(input("// number?: "))
        numtwo = int(input("// number?: "))
        print(num + numtwo)
    elif "/subtract" in comm:
        num = int(input("// number?: "))
        numtwo = int(input("// number?: "))
        print(num - numtwo)
    elif "/multiply" in comm:
        num = int(input("// number?: "))
        numtwo = int(input("// number?: "))
        print(num * numtwo)
    elif "/devide" in comm:
        num = int(input("// number?: "))
        numtwo = int(input("// number?: "))
        print(num / numtwo)
    elif "/search" in comm:
        subprocess.call("elinks", shell=True)
    elif "/box" in comm:
        ab = input("// box?: ")
        subprocess.call(f"echo {ab} | boxes -d diamonds -a c", shell=True)
    elif "/execute" in comm:
        applessssss = input("// execute?: ")
        subprocess.call(f"python3 {applessssss}", shell=True)
    elif "/update" in comm:
        subprocess.call("sudo apt update", shell=True)
    elif "/upgrade" in comm:
        subprocess.call("sudo apt upgrade", shell=True)
    elif "↑ ↑ ↓ ↓ ← → ← → b a start" in comm:
        print("secret hehehehe")
    elif "/type" in comm:
        typa = input("// type?: ")
        print(" ")
        anything(typa)
        print(" ")
    elif "/write" in comm:
        write = input("// ")
        eamp = input("// save as?: ")
        with open(f"{eamp}.p", "wb" ) as f:
            pickle.dump(write, f)
    elif "/load" in comm:
        aa = input("// open?: ")
        with open(f"{aa}.p", "rb" ) as f:
            i = pickle.load(f)
            print(i)
    elif "\\" in comm:
        print("""

""")
    elif "/weather" in comm:
        subprocess.call("curl wttr.in", shell=True)
    elif "/install" in comm:
        applessssss = input("// install?: ")
        subprocess.call(f"sudo apt install {applessssss}", shell=True)
    elif "#linux" in comm:
        r = input(os.getlogin() + " | Linux: ")
        subprocess.run(f"{r}", shell=True)
    elif "/dir" in comm:
        print("Current working directory: {0}".format(os.getcwd()))
    elif "/sound" in comm:
        mixer.init()
        reeeeeee = input("// file?: ")
        mixer.music.load(f'{reeeeeee}')
        mixer.music.play()
    elif "exit" in comm:
        sys.exit()
    elif "/info" in comm:
        subprocess.run("neofetch", shell=True)
    elif "/media" in comm:
        EE = input("// media?: ")
        if ".png" in EE:
            subprocess.call(f"mpv --no-config --vo=tct {EE}", shell=True)
        elif ".mp4" in EE:
            subprocess.call(f"mpv --no-config --vo=tct {EE}", shell=True)
            clearConsole()
            print(Back.RED + "_________________________________________________________")
            print(Back.RESET + " ")
            print(Fore.WHITE, """DarbBOX    MADE IN 🐍 PYTHON
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
         ,,,,,,,. ...........           ............ .,,,,,,,         
    .,,,,,,,,,,,. ...........           ............ .,,,,,,,,,,,.    
    .,. ...   ,,. ...........           ............ .,,   ... .,.    
    .,. .  .. ,,. ...........           ............ .,, ..  . .,.    
    .,.       ,,. ...........           ............ .,,       .,.    
    ............  ...........            ...........  ............                                                                               
type "/help" for a list of commands
""")
            print(Back.RED + "_________________________________________________________")
            print(Back.RESET + " ")
        else:
            subprocess.call(f"mpv --no-config --vo=tct {EE}", shell=True)
    elif "/3d" in comm:
        import matplotlib as mpl
        from mpl_toolkits.mplot3d import Axes3D
        import numpy as np
        import matplotlib.pyplot as plt
        import subprocess
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
        print("// Input X-Axis Start values:")
        x=list(map(int,input().split(",")))
        print("// Input X-Axis End values:")
        xe=list(map(int,input().split(",")))
        x.sort()
        print("// Input Y-Axis values:")
        y=list(map(int,input().split(",")))
        print("// Input Y-Axis End values:")
        ye=list(map(int,input().split(",")))
        print("// Input Z-Axis values:")
        z=list(map(int,input().split(",")))
        print("// Input Z-Axis End values:")
        ze=list(map(int,input().split(",")))
        for i in range(1):
            ax.plot([x[i], xe[i]], [y[i],ye[i]],zs=[z[i],ze[i]])
        ax.legend()
        plt.savefig('plot.png')
        EE = 'plot.png'
        subprocess.run(f"mogrify -format jpg {EE}", shell=True)
        EEE = EE.replace('.png', '.jpg')
        subprocess.call(f"mpv --no-config --vo=tct {EEE}", shell=True)
    elif "/help" in comm:
        print(Back.RESET + " ")
        print("""
___________________________________
commands:                          
                                   
/color-(color)
/font
/speak                             
/print                             
/sprint                            
/time                              
/add                               
/subtract                          
/multiply                          
/devide                            
/diskspace                         
/run                               
/clear
/date
/weather
/search                            
/type                              
/write                             
/load                              
/box
/sys-info
/execute                           
/update                            
/upgrade                           
/install                           
/dir                               
/sound
/files
/info                              
/media                             
/text                              
#linux                             
___________________________________
""")
        print(Back.RESET + " ")
    else:
        print(Fore.RED + "unknown command")
        print(Fore.WHITE + "")